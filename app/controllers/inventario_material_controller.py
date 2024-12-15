from sqlalchemy import text

from flask import Response

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    InventarioMaterial,
    Materiales
    )

sesion = impresion_conn()


def inventario_controller_get_all():
    inventario = sesion.query(InventarioMaterial).all()
    return inventario


def inventario_controller_register(inventario):
    _id_material = None
    _cantidad = None
    
    if "id_material" in inventario:
        if not (sesion.query(Materiales).filter_by(id_material=inventario["id_material"]).first()):
            return Response({"result":"No se encuentra ese material"}
                            ,status=400,mimetype="application/json")
        _id_material = inventario["id_material"]
    if "cantidad" in inventario:
        _cantidad = inventario["cantidad"]
    
  
    mInventario = InventarioMaterial(
        id_material=_id_material,
        cantidad=_cantidad,
        
    )
    
    sesion.add(mInventario)
    sesion.commit()
    return sesion.query(InventarioMaterial).filter_by(id_inventario = mInventario.id_inventario).all()


def inventario_controller_update(inventario):
    _id = inventario["id"]
    _data = inventario
    _inventario = sesion.query(InventarioMaterial).filter_by(id_inventario=_id).first()
    
    if "id_material" in _data:
        print(_data["id_material"])
        if not (sesion.query(Materiales).filter_by(id_material=_data["id_material"]).first()):
            return Response({"result":"No se encuentra ese material"}
                            ,status=400,mimetype="application/json")
        _inventario.id_material = _data["id_material"]
    if "cantidad" in _data:
        _inventario.cantidad = _data["cantidad"]
    
    
    sesion.merge(_inventario)
    sesion.flush()
    sesion.commit()
    
    return sesion.query(InventarioMaterial).filter_by(id_inventario = _id).all()
    
    
def inventario_controller_delete_by_id(id):
    
    try:
        _i=sesion.query(InventarioMaterial).filter_by(id_inventario = id).first()
        sesion.delete(_i)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")
    
    

def inventario_controller_get_by_filter(args):
    data = args
    
    esperados = ["id_material","cantidad"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        if esperados[i] in data:
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
            
    query = sesion.query(InventarioMaterial).from_statement(text(f"SELECT * FROM inventario_material {_where}")).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")


def inventario_controller_get_by_id(id):
    query = sesion.query(InventarioMaterial).filter_by(id_inventario=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")