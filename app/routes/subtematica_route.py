from flask import Blueprint, request

from ..controllers.subtematica_controller import (
    subtematica_controller_get_all,
    subtematica_controller_register,
    subtematica_controller_update,
    subtematica_controller_get_by_id,
    subtematica_controller_get_by_filter,
    subtematica_controller_delete_by_id
)

subtematica_bp = Blueprint("subtematica",__name__)


@subtematica_bp.route("/",methods=["GET"])
def subtematica_route_index():
    subtematica = subtematica_controller_get_all()
    return __subtematica_for__(subtematica)


@subtematica_bp.route("/register",methods=["POST"])
def subtematica_route_register():
    subtematica_request = request.get_json()
    subtematica = subtematica_controller_register(subtematica_request)
    return __subtematica_for__(subtematica)

@subtematica_bp.route("/update",methods=["PUT"])
def subtematica_route_update():
    subtematica_request = request.get_json()
    subtematica = subtematica_controller_update(subtematica_request)
    return __subtematica_for__(subtematica)

@subtematica_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def subtematica_route_delete_by_id(id):
    subtematica = subtematica_controller_delete_by_id(id)
    return __subtematica_for__(subtematica)
    

@subtematica_bp.route("/filter/id/<id>",methods=["POST"])
def subtematica_route_filter_id(id):
    
    subtematica = subtematica_controller_get_by_id(id)
    
    return __subtematica_for__(subtematica)
    


@subtematica_bp.route("/filter",methods=["POST"])
def subtematica_route_filter():
    
    args = request.get_json()
    subtematica = subtematica_controller_get_by_filter(args)
    return __subtematica_for__(subtematica)






## especial ##
def __subtematica_for__(subtematica):
    _return = []
    
    try:
        for sb in subtematica:
            
            _return.append(sb.get_dict())
            
        return _return
    except:
        return subtematica
