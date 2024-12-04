from sqlalchemy import text


from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Clientes
    )

sesion = impresion_conn()


def cliente_controller_get_all():
    cliente = sesion.query(Clientes).all()
    return cliente

def cliente_controller_register(cliente):
    _nombre = None
    _email = None
    _numero = None
  
    if "nombre" in cliente:
        _nombre = cliente["nombre"]
    if "numero" in cliente:
        _numero = cliente["numero"]
    if "email" in cliente:
        _email = cliente["email"]
  
    mCliente = Clientes(
        nombre=_nombre,
        numero=_numero,
        email=_email
    )
    sesion.add(mCliente)
    sesion.commit()
    return f"registrando cliente {cliente["nombre"]}"


def cliente_controller_update(cliente):
    _id = cliente["id"]
    _data = cliente
    _cliente = sesion.query(Clientes).filter_by(id_cliente=_id).first()
    
    if "nombre" in _data:
        _cliente.nombre = _data["nombre"]
    if "email" in _data:
        _cliente.email = _data["email"]
    if "numero" in _data:
        _cliente.numero = _data["numero"]
    
    
    sesion.merge(_cliente)
    sesion.flush()
    sesion.commit()
    
def cliente_controller_delete_by_id(id):
    
    try:
        _c=sesion.query(Clientes).filter_by(id_cliente = id).first()
        print(_c)
        sesion.delete(_c)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return "Borrado con exito"
    
def cliente_controller_delete(cliente):
    _data = cliente
    
    try:
        if "id" in _data:
            _c=sesion.query(Clientes).filter_by(id_cliente = _data["id"]).first()
            sesion.delete(_c)
            sesion.commit()
        elif "nombre" in _data:
            _c=sesion.query(Clientes).filter_by(nombre = _data["nombre"]).first()
            sesion.delete(_c)
            sesion.commit()
        else:
            return "No se tienen los datos necesarios"
        
    except Exception as e:
        return e
    finally:
        return "Borrado con exito"

def cliente_controller_get_by_name(nombre):
    cliente = sesion.query(Clientes).filter_by(nombre=nombre).all()
    return cliente


def cliente_controller_get_by_id(id):
    cliente = sesion.query(Clientes).filter_by(id_cliente=id).all()
    return cliente