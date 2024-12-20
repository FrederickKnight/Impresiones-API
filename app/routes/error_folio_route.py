from flask import Blueprint,request

from ..controllers.error_folio_controller import (
    error_folio_controller_get_all,
    error_folio_controller_register,
    error_folio_controller_update,
    error_folio_controller_delete_by_id,
    error_folio_controller_get_by_filter,
    error_folio_controller_get_by_id
)

error_folio_bp = Blueprint("errorfolio",__name__)

@error_folio_bp.route("/",methods=["GET"])
def error_folio_route_index():
    error_folio = error_folio_controller_get_all()
    return __error_folio_for__(error_folio)

@error_folio_bp.route("/register",methods=["POST"])
def error_folio_route_register():
    error_folio_request = request.get_json()
    error_folio = error_folio_controller_register(error_folio_request)
    return __error_folio_for__(error_folio)


@error_folio_bp.route("/update",methods=["PUT"])
def error_folio_route_update():
    error_folio_request = request.get_json()
    error_folio = error_folio_controller_update(error_folio_request)
    return __error_folio_for__(error_folio)
    

@error_folio_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def error_folio_route_delete_by_id(id):
    error_folio = error_folio_controller_delete_by_id(id)
    return __error_folio_for__(error_folio)


##
@error_folio_bp.route("/filter",methods=["POST"])
def error_folio_route_filter():
    args = request.get_json()
    
    error_folio = error_folio_controller_get_by_filter(args)
    
    return __error_folio_for__(error_folio)


@error_folio_bp.route("/filter/id/<id>",methods=["POST"])
def error_folio_route_filter_id(id):
    
    costogeneral = error_folio_controller_get_by_id(id)
    
    return __error_folio_for__(costogeneral)
    



## especiales ##
def __error_folio_for__(error_folio):
    _return = []
        
    try:
        for er in error_folio:
            
            _return.append(er.get_dict())
            
        return _return
    except:
        return error_folio