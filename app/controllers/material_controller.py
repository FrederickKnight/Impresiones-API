from sqlalchemy import text

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Materiales
    )


sesion = impresion_conn()

def material_controller_get_all():
    material = sesion.query(Materiales).all()
    return material


def material_controller_register(material):
    _nombre = None
    _marca = None
    _medicion = None
  
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
    return f"registrando modelo {material["nombre"]}"

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

def material_controller_delete_by_id(id):
    
    try:
        _m=sesion.query(Materiales).filter_by(id_material = id).first()
        print(_m)
        sesion.delete(_m)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return "Borrado con exito"
    
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
        return "Borrado con exito"
    

def material_controller_get_by_id(id):
    material = sesion.query(Materiales).filter_by(id_material=id).all()
    return material

def material_controller_get_by_nombre(nombre):
    material = sesion.query(Materiales).filter_by(nombre=nombre).all()
    return material

def material_controller_get_by_marca(marca):
    material = sesion.query(Materiales).filter_by(marca=marca).all()
    return material