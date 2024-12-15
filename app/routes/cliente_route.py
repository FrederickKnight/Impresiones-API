from flask import Blueprint,request,Response

from ..controllers.cliente_controller import (
    cliente_controller_get_all,
    cliente_controller_get_by_name,
    cliente_controller_get_by_id,
    cliente_controller_register,
    cliente_controller_update,
    cliente_controller_delete,
    cliente_controller_delete_by_id
)

cliente_bp = Blueprint("cliente",__name__)

@cliente_bp.route("/",methods=["GET"])
def cliente_route_index():
    #Retornar toda la lista de clientes
    cliente = cliente_controller_get_all()
    return __cliente_for__(cliente)

@cliente_bp.route("/register",methods=["POST"])
def cliente_route_register():
    #register cliente
    cliente_request = request.get_json()
    cliente = cliente_controller_register(cliente_request)
    return __cliente_for__(cliente)

@cliente_bp.route("/update",methods=["PUT"])
def cliente_route_update():
    #update cliente
    cliente_request = request.get_json()
    cliente = cliente_controller_update(cliente_request)
    return __cliente_for__(cliente)
    

@cliente_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def cliente_route_delete_by_id(id):
    cliente =  cliente_controller_delete_by_id(id)
    return __cliente_for__(cliente)
    
@cliente_bp.route("/delete",methods=["DELETE"])
def cliente_route_delete():
    cliente_request = request.get_json()
    cliente =  cliente_controller_delete(cliente_request)
    return __cliente_for__(cliente)

# Funciones para obtener a los clientes por filtros

@cliente_bp.route("/filter/nombre/<nombre>",methods=["POST"])
def cliente_route_filter_name(nombre):
    #Retornar el filtrado de la tabla cliente por nombre
    cliente = cliente_controller_get_by_name(nombre)
    
    return __cliente_for__(cliente)

@cliente_bp.route("/filter/id/<id>",methods=["POST"])
def cliente_route_filter_id(id):
    #Retornar el filtrado de la tabla cliente por id
    cliente = cliente_controller_get_by_id(id)
    
    return __cliente_for__(cliente)




## especiales ##
def __cliente_for__(clientes):
    _return = []
    
    try:
        
        for cl in clientes:
            
            _return.append({
                "id":cl.id_cliente,
                "nombre":cl.nombre,
                "email":cl.email,
                "numero":cl.numero
            })
            
        return _return
    except:
        return clientes