from sqlalchemy import text

from flask import Response

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Inventario
    )

sesion = impresion_conn()


def inventario_controller_get_all():
    inventario = sesion.query(Inventario).all()
    return inventario


def inventario_controller_register(inventario):
    _nombre = None
    _tipo = None
    _descripcion = None
    _cantidad = None
    _medicion = None
    
    if "nombre" in inventario:
        _nombre = inventario["nombre"]
    if "tipo" in inventario:
        _tipo = inventario["tipo"]
    if "descripcion" in inventario:
        _descripcion = inventario["descripcion"]
    if "cantidad" in inventario:
        _cantidad = inventario["cantidad"]
    if "medicion" in inventario:
        _medicion = inventario["medicion"]
    
  
    mInventario = Inventario(
        nombre=_nombre,
        tipo=_tipo,
        descripcion=_descripcion,
        cantidad=_cantidad,
        medicion=_medicion
        
    )
    
    sesion.add(mInventario)
    sesion.commit()
    return sesion.query(Inventario).filter_by(id_inventario = mInventario.id_inventario).all()



def inventario_controller_update(inventario):
    _id = inventario["id"]
    _data = inventario
    _inventario = sesion.query(Inventario).filter_by(id_inventario=_id).first()
    
    if "nombre" in _data:
        _inventario.nombre = _data["nombre"]
    if "tipo" in _data:
        _inventario.tipo = _data["tipo"]
    if "descripcion" in _data:
        _inventario.descripcion = _data["descripcion"]
    if "cantidad" in _data:
        _inventario.cantidad = _data["cantidad"]
    if "medicion" in _data:
        _inventario.medicion = _data["medicion"]
    
    
    sesion.merge(_inventario)
    sesion.flush()
    sesion.commit()
    return sesion.query(Inventario).filter_by(id_inventario = _id).all()
    
    
def inventario_controller_delete_by_id(id):
    
    try:
        _i=sesion.query(Inventario).filter_by(id_inventario = id).first()
        print(_i)
        sesion.delete(_i)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")
        
    
    

def inventario_controller_get_by_filter(args):
    data = args
    
    esperados = ["nombre","tipo","medicion"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        if esperados[i] in data:
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
            
    query = sesion.query(Inventario).from_statement(text(f"SELECT * FROM inventario {_where}")).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")


def inventario_controller_get_by_id(id):
    query = sesion.query(Inventario).filter_by(id_inventario=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")