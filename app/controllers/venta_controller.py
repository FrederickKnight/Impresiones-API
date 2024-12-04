from sqlalchemy import text

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Ventas
    )

sesion = impresion_conn()


def venta_controller_get_all():
    venta = sesion.query(Ventas).all()
    return venta


def venta_controller_register(venta):
    
    _id_folio = None
    _id_modelo = None
    _id_material = None
    _cantidad_material = None
    _tiempo_impresion = None
    _costo_total = None
    _descuento = None
    _costo_aplicado = None
    
    if "id_folio" in venta:
        _id_folio = venta["id_folio"]
    if "id_modelo" in venta:
        _id_modelo = venta["id_modelo"]
    if "id_material" in venta:
        _id_material = venta["id_material"]
    if "cantidad_material" in venta:
        _cantidad_material = venta["cantidad_material"]
    if "tiempo_impresion" in venta:
        _tiempo_impresion = venta["tiempo_impresion"]
    if "costo_total" in venta:
        _costo_total = venta["costo_total"]
    if "descuento" in venta:
        _descuento = venta["descuento"]
    if "costo_aplicado" in venta:
        _costo_aplicado = venta["costo_aplicado"]
        
    mVenta = Ventas(
        id_folio=_id_folio,
        id_modelo = _id_modelo,
        id_material = _id_material,
        cantidad_material = _cantidad_material,
        tiempo_impresion = _tiempo_impresion,
        costo_total = _costo_total,
        descuento = _descuento,
        costo_aplicado = _costo_aplicado,
    )
    
    sesion.add(mVenta)
    sesion.commit()
    return f"registrando venta con {venta["costo_aplicado"]}"

def venta_controller_delete_by_id(id):
    ########### Arreglar erorr  #########
    try:
        _v=sesion.query(Ventas).filter_by(id_venta = id)
        print(_v)
        sesion.delete(_v)
        sesion.commit()
        
    except Exception as e:
        return e
    finally:
        return "Borrado con exito"
     
# filter
def venta_controller_get_by_id(id):
    tematica = sesion.query(Ventas).filter_by(id_venta=id).all()
    return tematica


def venta_controller_get_by_filter(args):
    data = args
    
    esperados = ["id_folio","id_modelo","id_material","cantidad_material","tiempo_impresion","costo_total","descuento","costo_aplicado"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        if esperados[i] in data:
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
            
    venta = sesion.query(Ventas).from_statement(text(f"SELECT * FROM venta {_where}")).all()
    return venta