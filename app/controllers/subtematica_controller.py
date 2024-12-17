from sqlalchemy import text

from flask import Response


from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Subtematicas
    )


sesion = impresion_conn()


def subtematica_controller_get_all():
    return sesion.query(Subtematicas).all()


def subtematica_controller_register(subtematica):
    
    _id_tematica = None
    _nombre = None
    
    if "id_tematica" in subtematica:
        _id_tematica = subtematica["id_tematica"]
    if "nombre" in subtematica:
        _nombre = subtematica["nombre"]
        
    mSubtematica = Subtematicas(
        id_tematica=_id_tematica,
        nombre = _nombre,
    )
    
    sesion.add(mSubtematica)
    sesion.commit()
    return sesion.query(Subtematicas).filter_by(id_subtematica = mSubtematica.id_subtematica).all()
    


def subtematica_controller_update(subtematica):
    _id = subtematica["id"]
    _data = subtematica
    _subtematica = sesion.query(Subtematicas).filter_by(id_subtematica=_id).first()
    
    
    if "id_tematica" in subtematica:
        _subtematica.id_tematica = _data["id_tematica"]
    if "nombre" in subtematica:
        _subtematica.nombre = _data["nombre"]
        

    sesion.merge(_subtematica)
    sesion.flush()
    sesion.commit()
    
    return sesion.query(Subtematicas).filter_by(id_subtematica = _id).all()


def subtematica_controller_delete_by_id(id):
    try:
        _sb=sesion.query(Subtematicas).filter_by(id_subtematica = id).first()
        sesion.delete(_sb)
        sesion.commit()
        
    except Exception as e:
        return e
    finally:
        return Response(status=200,mimetype="application/json")
     


def subtematica_controller_get_by_id(id):
    query = sesion.query(Subtematicas).filter_by(id_subtematica=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")



def subtematica_controller_get_by_filter(args):
    data = args
    
    esperados = ["nombre","id_tematica"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        if esperados[i] in data:
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
    
    query = sesion.query(Subtematicas).from_statement(text(f"SELECT * FROM subtematica {_where}")).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")