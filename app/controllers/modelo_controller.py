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
    _nombre = None
    _id_subtematica = None
    _descripcion = None
    _direccion_archivo = None
  
    if "nombre" in modelo:
        _nombre = modelo["nombre"]
    if "id_subtematica" in modelo:
        if not (sesion.query(Subtematicas).filter_by(id_subtematica=modelo["id_subtematica"]).first()):
            return Response({"result":"No se encuentra esa subtematica"}
                            ,status=400,mimetype="application/json")
        
        _id_subtematica = int(modelo["id_subtematica"])

    if "descripcion" in modelo:
        _descripcion = modelo["descripcion"]
    if "direccion_archivo" in modelo:
        _direccion_archivo = modelo["direccion_archivo"]
  
    mModelo = Modelos(
        nombre=_nombre,
        id_subtematica=_id_subtematica,
        descripcion=_descripcion,
        direccion_archivo=_direccion_archivo
    )
    
    sesion.add(mModelo)
    sesion.commit()
    return sesion.query(Modelos).filter_by(id_modelo = mModelo.id_modelo).all()


def modelo_controller_update(modelo):
    _id = modelo["id"]
    _data = modelo
    _modelo = sesion.query(Modelos).filter_by(id_modelo=_id).first()
    
    if "nombre" in _data:
        _modelo.nombre = _data["nombre"]
    if "id_subtematica" in _data:
        print(_data["id_subtematica"])
        if not (sesion.query(Subtematicas).filter_by(id_subtematica=_data["id_subtematica"]).first()):
            return Response(status=404,mimetype="application/json")
        _modelo.id_subtematica = _data["id_subtematica"]
    if "descripcion" in _data:
        _modelo.descripcion = _data["descripcion"]
    if "direccion_archivo" in _data:
        _modelo.direccion_archivo = _data["direccion_archivo"]
    
    
    sesion.merge(_modelo)
    sesion.flush()
    sesion.commit()
    return sesion.query(Modelos).filter_by(id_modelo = _id).all()
    


def modelo_controller_delete_by_id(id):
    
    try:
        _m=sesion.query(Modelos).filter_by(id_modelo = id).first()
        print(_m)
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
        print(query)
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")