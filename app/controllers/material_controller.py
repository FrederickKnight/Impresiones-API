from sqlalchemy import text

from flask import Response

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Materiales
    )


sesion = impresion_conn()

def material_controller_get_all():
    return sesion.query(Materiales).all()


def material_controller_register(material):
    _nombre = None
    _marca = None
    _medicion = None
    _color = None
  
    if "nombre" in material:
        _nombre = material["nombre"]
    if "marca" in material:
        _marca = material["marca"]
    if "medicion" in material:
        _medicion = material["medicion"]
    if "color" in material:
        _color = material["color"]
        
    mMaterial = Materiales(
        nombre=_nombre,
        marca = _marca,
        medicion = _medicion,
        color = _color
    )
    
    sesion.add(mMaterial)
    sesion.commit()
    return sesion.query(Materiales).filter_by(id_material = mMaterial.id_material).all()

def material_controller_update(material):
    _id = material["id"]
    _data = material
    _material = sesion.query(Materiales).filter_by(id_material=_id).first()
    
    if "nombre" in _data:
        _material.nombre = _data["nombre"]
    if "marca" in _data:
        _material.marca = _data["marca"]
    if "medicion" in _data:
        _material.medicion = _data["medicion"]
    if "color" in material:
        _material.color = material["color"]
    
    sesion.merge(_material)
    sesion.flush()
    sesion.commit()
    
    return sesion.query(Materiales).filter_by(id_material = _id).all()

def material_controller_delete_by_id(id):
    
    try:
        _m=sesion.query(Materiales).filter_by(id_material = id).first()
        sesion.delete(_m)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")
    
def material_controller_delete(material):
    _data = material
    
    try:
        if "id" in _data:
            _m=sesion.query(Materiales).filter_by(id_tematica = _data["id"]).first()
            sesion.delete(_m)
            sesion.commit()
        elif "nombre" in _data and "marca" in _data: 
            _m=sesion.query(Materiales).filter_by(nombre = _data["nombre"],marca=_data["marca"]).first()
            sesion.delete(_m)
            sesion.commit()
        else:
            return "No se tienen los datos necesarios"
        
    except Exception as e:
        return e
    finally:
        return Response(status=200,mimetype="application/json")
    

def material_controller_get_by_id(id):
    query = sesion.query(Materiales).filter_by(id_material=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")


def material_controller_get_by_filter(args):
    data = args
    
    esperados = ["nombre","marca","color","medicion"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        if esperados[i] in data:
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
    
    query = sesion.query(Materiales).from_statement(text(f"SELECT * FROM material {_where}")).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")