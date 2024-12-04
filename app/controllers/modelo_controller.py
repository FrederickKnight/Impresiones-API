from sqlalchemy import text

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Modelos,
    Tematicas
    )

sesion = impresion_conn()

def modelo_controller_get_all():
    cliente = sesion.query(Modelos).all()
    return cliente

def modelo_controller_register(modelo):
    _nombre = None
    _id_tematica = None
    _descripcion = None
    _direccion_archivo = None
  
    if "nombre" in modelo:
        _nombre = modelo["nombre"]
    if "id_tematica" in modelo:
        _id_tematica = int(modelo["id_tematica"])
        if not (sesion.query(Tematicas).filter_by(id_tematica=_id_tematica).first()):
            return "No se encuentra esa tematica registrada aun"
        
    if "descripcion" in modelo:
        _descripcion = modelo["descripcion"]
    if "direccion_archivo" in modelo:
        _direccion_archivo = modelo["direccion_archivo"]
  
    mModelo = Modelos(
        nombre=_nombre,
        id_tematica=_id_tematica,
        descripcion=_descripcion,
        direccion_archivo=_direccion_archivo
    )
    
    sesion.add(mModelo)
    sesion.commit()
    return f"registrando modelo {modelo["nombre"]}"

def modelo_controller_update(modelo):
    _id = modelo["id"]
    _data = modelo
    _modelo = sesion.query(Modelos).filter_by(id_modelo=_id).first()
    
    if "nombre" in _data:
        _modelo.nombre = _data["nombre"]
    if "id_tematica" in _data:
        if not (sesion.query(Tematicas).filter_by(id_tematica=_data["id_tematica"]).first()):
            return "No se encuentra esa tematica registrada aun"
        _modelo.id_tematica = _data["id_tematica"]
    if "descripcion" in _data:
        _modelo.descripcion = _data["descripcion"]
    if "direccion_archivo" in _data:
        _modelo.direccion_archivo = _data["direccion_archivo"]
    
    
    sesion.merge(_modelo)
    sesion.flush()
    sesion.commit()


def modelo_controller_delete_by_id(id):
    
    try:
        _m=sesion.query(Modelos).filter_by(id_modelo = id).first()
        print(_m)
        sesion.delete(_m)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return "Borrado con exito"
    
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
        return "Borrado con exito"



# filter
def modelo_controller_get_by_id(id):
    modelo = sesion.query(Modelos).filter_by(id_modelo=id).all()
    return modelo

def modelo_controller_get_by_filter(args):
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
            
    modelo = sesion.query(Modelos).from_statement(text(f"SELECT * FROM modelo {_where}")).all()
    return modelo