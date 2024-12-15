from flask import Blueprint,request

from ..controllers.inventario_material_controller import (
    inventario_controller_get_all,
    inventario_controller_register,
    inventario_controller_update,
    inventario_controller_delete_by_id,
    inventario_controller_get_by_filter,
)

inventario_material_bp = Blueprint("inventariomaterial",__name__)

@inventario_material_bp.route("/",methods=["GET"])
def inventario_route_index():
    _inventario = inventario_controller_get_all()
    return __inventario_for__(_inventario)
    

@inventario_material_bp.route("/register",methods=["POST"])
def inventario_route_register():
    inventario_request = request.get_json()
    inventario = inventario_controller_register(inventario_request)
    return __inventario_for__(inventario)


@inventario_material_bp.route("/update",methods=["PUT"])
def inventario_route_update():
    inventario_request = request.get_json()
    inventario = inventario_controller_update(inventario_request)
    return __inventario_for__(inventario)
    
    


@inventario_material_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def inventario_route_delete_by_id(id):
    inventario = inventario_controller_delete_by_id(id)
    return __inventario_for__(inventario)
    
    


##
@inventario_material_bp.route("/filter",methods=["POST"])
def inventario_route_filter():
    args = request.get_json()
    
    inventario = inventario_controller_get_by_filter(args)
    
    return __inventario_for__(inventario)




## especiales ##
def __inventario_for__(inventario):
    _return = []
    
    for iv in inventario:
        
        _return.append({
            "id":iv.id_inventario,
            "id_material":iv.id_material,
            "cantidad":iv.cantidad,
        })
        
    return _return