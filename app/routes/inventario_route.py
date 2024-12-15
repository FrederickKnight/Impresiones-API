from flask import Blueprint,request

from ..controllers.inventario_controller import (
    inventario_controller_get_all,
    inventario_controller_register,
    inventario_controller_update,
    inventario_controller_delete_by_id,
    inventario_controller_get_by_filter,
)

inventario_bp = Blueprint("inventario",__name__)

@inventario_bp.route("/",methods=["GET"])
def inventario_route_index():
    inventario = inventario_controller_get_all()
    return __inventario_for__(inventario)
    

@inventario_bp.route("/register",methods=["POST"])
def inventario_route_register():
    inventario_request = request.get_json()
    inventario = inventario_controller_register(inventario_request)
    return __inventario_for__(inventario)
    


@inventario_bp.route("/update",methods=["PUT"])
def inventario_route_update():
    #update cliente
    inventario_request = request.get_json()
    inventario = inventario_controller_update(inventario_request)
    return __inventario_for__(inventario)
    


@inventario_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def inventario_route_delete_by_id(id):
    inventario = inventario_controller_delete_by_id(id)
    return __inventario_for__(inventario)
    
    


##
@inventario_bp.route("/filter",methods=["POST"])
def inventario_route_filter():
    args = request.get_json()
    
    inventario = inventario_controller_get_by_filter(args)

    return __inventario_for__(inventario)



## especiales ##
def __inventario_for__(inventario):
    _return = []
        
    try:
        for iv in inventario:
            
            _return.append({
                "id":iv.id_inventario,
                "tipo":iv.tipo,
                "nombre":iv.nombre,
                "descripcion":iv.descripcion,
                "cantidad":iv.cantidad,
                "medicion":iv.medicion
            })
            
        return _return
    except:
        return inventario