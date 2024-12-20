from flask import Blueprint, request

from datetime import datetime

from ..controllers.folio_controller import (
    folio_controller_get_all,
    folio_controller_register,
    folio_controller_get_by_folio,
    folio_controller_delete_by_id,
    folio_controller_get_by_fecha,
    folio_controller_get_by_id
)


folio_bp = Blueprint("folio",__name__)


@folio_bp.route("/",methods=["GET"])
def folio_route_index():
    folio = folio_controller_get_all()
    return __folio_for__(folio)


@folio_bp.route("/register",methods=["POST"])
def folio_route_register():
    folio_request = request.get_json()
    folio = folio_controller_register(folio_request)
    return __folio_for__(folio)



@folio_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def folio_route_delete_by_id(id):
    folio =  folio_controller_delete_by_id(id)
    return __folio_for__(folio)


@folio_bp.route("/filter/folio",methods=["POST"])
def folio_route_filter_folio():
    folio_request = request.get_json()
    
    folio = folio_controller_get_by_folio(folio_request)

    return __folio_for__(folio)


@folio_bp.route("/filter/fecha",methods=["POST"])
def folio_route_filter_fecha():
    fecha = request.get_json()
    
    folio = folio_controller_get_by_fecha(fecha)
    
    return __folio_for__(folio)


@folio_bp.route("/filter/id/<id>",methods=["POST"])
def folio_route_filter_material_id(id):
    costogeneral = folio_controller_get_by_id(id)
    
    return __folio_for__(costogeneral)



# especial
def __folio_for__(folio):
    _return = []
        
    try:
        for f in folio:
            _return.append(f.get_dict())
            
        return _return
    except:
        return folio