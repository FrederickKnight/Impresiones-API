from sqlalchemy import text

from flask import Response

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Clientes
    )

sesion = impresion_conn()


def cliente_controller_get_all():
    return sesion.query(Clientes).all()
     

def cliente_controller_register(cliente):
    _esperados = {
        "nombre":None,
        "email":None,
        "numero":None
    }
    
    _esperados.update({key:cliente[key] for key in _esperados if key in cliente})
  
    mCliente = Clientes(
        nombre=_esperados["nombre"],
        email=_esperados["email"],
        numero=_esperados["numero"],
    )
    sesion.add(mCliente)
    sesion.commit()
    
    return sesion.query(Clientes).filter_by(id_cliente = mCliente.id_cliente).all()
    


def cliente_controller_update(cliente):
    _id = cliente["id"]
    
    _data = cliente
    _cliente = sesion.query(Clientes).filter_by(id_cliente=_id).first()
    
    _esperados = {
        "nombre":None,
        "email":None,
        "numero":None
    }
    
    _esperados.update({key:_data[key] for key in _esperados if key in _data})
    
    _cliente.nombre = _esperados["nombre"]
    _cliente.email = _esperados["email"]
    _cliente.numero = _esperados["numero"]
    
    
    sesion.merge(_cliente)
    sesion.flush()
    sesion.commit()
    
    return sesion.query(Clientes).filter_by(id_cliente = _id).all()
    
def cliente_controller_delete_by_id(_id):
    
    try:
        _c=sesion.query(Clientes).filter_by(id_cliente = _id).first()
        sesion.delete(_c)
        sesion.commit()
        
    except Exception as e:
        return e
    finally:
        return Response(status=200,mimetype="application/json")
    
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
        return Response(status=200,mimetype="application/json")

def cliente_controller_get_by_name(nombre):
    query= sesion.query(Clientes).filter_by(nombre=nombre).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")
    


def cliente_controller_get_by_id(id):
    query= sesion.query(Clientes).filter_by(id_cliente=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")