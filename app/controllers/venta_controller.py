from sqlalchemy import text

from flask import Response


from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Ventas
    )

sesion = impresion_conn()


def venta_controller_get_all():
    return sesion.query(Ventas).all()

def venta_controller_register(venta):
    
    _esperados = {
        "id_folio":None,
        "id_modelo":None,
        "id_material":None,
        "cantidad_material":None,
        "tiempo_impresion":None,
        "costo_total":None,
        "descuento":None,
        "costo_aplicado":None,
        "id_costo_general":None
    }
    
    _esperados.update({key:venta[key] for key in _esperados if key in venta})
    
    mVenta = Ventas(
        id_folio=_esperados["id_folio"],
        id_modelo = _esperados["id_modelo"],
        id_material = _esperados["id_material"],
        id_costo_general = _esperados["id_costo_general"],
        cantidad_material = _esperados["cantidad_material"],
        tiempo_impresion = _esperados["tiempo_impresion"],
        costo_total = _esperados["costo_total"],
        descuento = _esperados["descuento"],
        costo_aplicado = _esperados["costo_aplicado"],
    )
    
    sesion.add(mVenta)
    sesion.commit()
    return sesion.query(Ventas).filter_by(id_venta = mVenta.id_venta).all()
    

def venta_controller_delete_by_id(id):
    try:
        _v=sesion.query(Ventas).filter_by(id_venta = id).first()
        sesion.delete(_v)
        sesion.commit()
        
    except Exception as e:
        return e
    finally:
        return Response(status=200,mimetype="application/json")
     
# filter
def venta_controller_get_by_id(id):
    query = sesion.query(Ventas).filter_by(id_venta=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")

def venta_controller_get_by_filter(args):
    data = args
    
    esperados = ["id_folio","id_modelo","id_costo_general","id_material","cantidad_material","tiempo_impresion","costo_total","descuento","costo_aplicado"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        if esperados[i] in data:
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
            
    query = sesion.query(Ventas).from_statement(text(f"SELECT * FROM venta {_where}")).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")