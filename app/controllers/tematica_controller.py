from sqlalchemy import text

from flask import Response

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Tematicas
    )


sesion = impresion_conn()

def tematica_controller_get_all():
    tematica = sesion.query(Tematicas).all()
    return tematica


def tematica_controller_register(tematica):
    _nombre = None
  
    if "nombre" in tematica:
        _nombre = tematica["nombre"]
        
    mTematica = Tematicas(
        nombre=_nombre
    )
    
    sesion.add(mTematica)
    sesion.commit()
    return sesion.query(Tematicas).filter_by(id_tematica = mTematica.id_tematica).all()
    

def tematica_controller_update(tematica):
    _id = tematica["id"]
    _data = tematica
    _tematica = sesion.query(Tematicas).filter_by(id_tematica=_id).first()
    
    if "nombre" in _data:
        _tematica.nombre = _data["nombre"]
    
    
    sesion.merge(_tematica)
    sesion.flush()
    sesion.commit()
    return sesion.query(Tematicas).filter_by(id_tematica = _id).all()
    

def tematica_controller_delete_by_id(id):
    
    try:
        _t=sesion.query(Tematicas).filter_by(id_tematica = id).first()
        sesion.delete(_t)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")
    
def tematica_controller_delete(tematica):
    _data = tematica
    
    try:
        if "id" in _data:
            _t=sesion.query(Tematicas).filter_by(id_tematica = _data["id"]).first()
            sesion.delete(_t)
            sesion.commit()
        elif "nombre" in _data:
            _t=sesion.query(Tematicas).filter_by(nombre = _data["nombre"]).first()
            sesion.delete(_t)
            sesion.commit()
        else:
            return "No se tienen los datos necesarios"
        
    except Exception as e:
        return e
    finally:
        return Response(status=200,mimetype="application/json")

    
def tematica_controller_get_by_id(id):
    query = sesion.query(Tematicas).filter_by(id_tematica=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")

def tematica_controller_get_by_nombre(nombre):
    query = sesion.query(Tematicas).filter_by(nombre=nombre).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")