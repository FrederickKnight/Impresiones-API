from sqlalchemy import text

from flask import Response

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Modelos,
    Subtematicas
    )

sesion = impresion_conn()

def modelo_controller_get_all():
    cliente = sesion.query(Modelos).all()
    return cliente

def modelo_controller_register(modelo):
    if "id_subtematica" in modelo:
        if not (sesion.query(Subtematicas).filter_by(id_subtematica=modelo["id_subtematica"]).first()):
            return Response({"result":"No se encuentra esa subtematica"}
                            ,status=400,mimetype="application/json")
    _esperados = {
        "nombre":None,
        "id_subtematica":None,
        "descripcion":None,
        "direccion_archivo":None
    }
    
    _esperados.update({key:modelo[key] for key in _esperados if key in modelo})
    
    mModelo = Modelos(
        nombre=_esperados["nombre"],
        id_subtematica=_esperados["id_subtematica"],
        descripcion=_esperados["descripcion"],
        direccion_archivo=_esperados["direccion_archivo"]
    )
    
    sesion.add(mModelo)
    sesion.commit()
    return sesion.query(Modelos).filter_by(id_modelo = mModelo.id_modelo).all()


def modelo_controller_update(modelo):
    _id = modelo["id"]
    _data = modelo
    _modelo = sesion.query(Modelos).filter_by(id_modelo=_id).first()
    
    if "id_subtematica" in _data:
        if not (sesion.query(Subtematicas).filter_by(id_subtematica=_data["id_subtematica"]).first()):
            return Response(status=404,mimetype="application/json")
    
    _esperados = {
        "nombre":None,
        "id_subtematica":None,
        "descripcion":None,
        "direccion_archivo":None
    }
    
    _esperados.update({key:_data[key] for key in _esperados if key in _data})
    
    _modelo.nombre = _esperados["nombre"]
    _modelo.id_subtematica = _esperados["id_subtematica"]
    _modelo.descripcion = _esperados["descripcion"]
    _modelo.direccion_archivo = _esperados["direccion_archivo"]
    
    sesion.merge(_modelo)
    sesion.flush()
    sesion.commit()
    return sesion.query(Modelos).filter_by(id_modelo = _id).all()
    

def modelo_controller_delete_by_id(id):
    
    try:
        _m=sesion.query(Modelos).filter_by(id_modelo = id).first()
        sesion.delete(_m)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")
        
    
def modelo_controller_delete(modelo):
    _data = modelo
    
    try:
        if "id" in _data:
            _m=sesion.query(Modelos).filter_by(id_modelo = _data["id"]).first()
            sesion.delete(_m)
            sesion.commit()
        elif "nombre" in _data:
            _m=sesion.query(Modelos).filter_by(nombre = _data["nombre"]).first()
            sesion.delete(_m)
            sesion.commit()
        else:
            return "No se tienen los datos necesarios"
        
    except Exception as e:
        return e
    finally:
        return Response(status=200,mimetype="application/json")
       
       
# filter
def modelo_controller_get_by_id(id):
    query = sesion.query(Modelos).filter_by(id_modelo=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")


def modelo_controller_get_by_filter(args):
    data = args
    
    esperados = ["nombre","id_subtematica"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        if esperados[i] in data:                
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
            
    query = sesion.query(Modelos).from_statement(text(f"SELECT * FROM modelo {_where}")).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")