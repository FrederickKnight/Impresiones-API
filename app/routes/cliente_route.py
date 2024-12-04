from flask import Blueprint,request

from ..controllers.cliente_controller import (
    cliente_controller_get_all,
    cliente_controller_get_by_filter,
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
    _return = __cliente_for__(cliente)
    return _return

@cliente_bp.route("/register",methods=["POST"])
def cliente_route_register():
    #register cliente
    cliente = request.get_json()
    return cliente_controller_register(cliente)


@cliente_bp.route("/update",methods=["PUT"])
def cliente_route_update():
    #update cliente
    cliente = request.get_json()
    cliente_controller_update(cliente)
    return "update"

@cliente_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def cliente_route_delete_by_id(id):
    return cliente_controller_delete_by_id(id)
    
@cliente_bp.route("/delete",methods=["DELETE"])
def cliente_route_delete():
    cliente = request.get_json()
    return cliente_controller_delete(cliente)

# Funciones para obtener a los clientes por filtros

@cliente_bp.route("/filter",methods=["POST"])
def cliente_route_filter():
    #introducir args por medio de json en request
    #Retornar el filtrado de la tabla cliente, ya sea por nombre, email o numero o id
    args = request.get_json()
    
    cliente = cliente_controller_get_by_filter(args)
    
    _return = __cliente_for__(cliente)

    return _return

@cliente_bp.route("/filter/nombre/<nombre>",methods=["POST"])
def cliente_route_filter_name(nombre):
    #Retornar el filtrado de la tabla cliente por nombre
    cliente = cliente_controller_get_by_name(nombre)
    
    _return = __cliente_for__(cliente)

    return _return

@cliente_bp.route("/filter/id/<id>",methods=["POST"])
def cliente_route_filter_id(id):
    #Retornar el filtrado de la tabla cliente por id
    cliente = cliente_controller_get_by_id(id)
    
    _return = __cliente_for__(cliente)
    return _return




## especiales ##
def __cliente_for__(clientes):
    _return = []
    
    for cl in clientes:
        
        _return.append({
            "id":cl.id_cliente,
            "nombre":cl.nombre,
            "email":cl.email,
            "numero":cl.numero
        })
        
    return _return