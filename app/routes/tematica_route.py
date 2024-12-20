from flask import Blueprint, request

from ..controllers.tematica_controller import (
    tematica_controller_get_all,
    tematica_controller_register,
    tematica_controller_update,
    tematica_controller_delete_by_id,
    tematica_controller_delete,
    tematica_controller_get_by_id,
    tematica_controller_get_by_nombre
)


tematica_bp = Blueprint("tematica",__name__)


@tematica_bp.route("/",methods=["GET"])
def tematica_route_index():
    tematica = tematica_controller_get_all()
    return __tematica_for__(tematica)
    


@tematica_bp.route("/register",methods=["POST"])
def tematica_route_register():
    tematica_request = request.get_json()
    tematica = tematica_controller_register(tematica_request)
    return __tematica_for__(tematica)
    

@tematica_bp.route("/update",methods=["PUT"])
def tematica_route_update():
    tematica_request = request.get_json()
    tematica = tematica_controller_update(tematica_request)
    return __tematica_for__(tematica)
    
    

@tematica_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def tematica_route_delete_by_id(id):
    tematica =  tematica_controller_delete_by_id(id)
    return __tematica_for__(tematica)

    

@tematica_bp.route("/delete",methods=["DELETE"])
def tematica_route_delete():
    tematica_request = request.get_json()
    tematica = tematica_controller_delete(tematica_request)
    return __tematica_for__(tematica)



# Filter

@tematica_bp.route("/filter/id/<id>",methods=["POST"])
def modelo_route_filter_id(id):
    
    tematica = tematica_controller_get_by_id(id)
    
    return  __tematica_for__(tematica)


@tematica_bp.route("/filter/nombre/<nombre>",methods=["POST"])
def modelo_route_filter_nombre(nombre):
    
    tematica = tematica_controller_get_by_nombre(nombre)
    
    return __tematica_for__(tematica)

## especial ##
def __tematica_for__(tematica):
    _return = []
    
    try:
        for ml in tematica:
            
            _return.append(ml.get_dict())
            
        return _return
    except:
        return tematica