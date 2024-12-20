from flask import Blueprint, request
from datetime import datetime

from ..controllers.costogeneral_controller import (
    costo_general_controller_get_all,
    costo_general_controller_register,
    costo_general_controller_get_by_id,
    costo_general_controller_get_by_material,
    costo_general_controller_delete_by_id,
    costo_general_controller_get_by_fecha,
)


costogeneral_bp = Blueprint("costogeneral",__name__)


@costogeneral_bp.route("/",methods=["GET"])
def costo_general_route_index():
    costogeneral = costo_general_controller_get_all()
    return __costo_general_for__(costogeneral)
      

@costogeneral_bp.route("/register",methods=["POST"])
def tematica_route_register():
    costogeneral_request = request.get_json()
    costogeneral = costo_general_controller_register(costogeneral_request)
    return __costo_general_for__(costogeneral)

@costogeneral_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def costo_general_route_delete_by_id(id):
    costogeneral = costo_general_controller_delete_by_id(id)
    return __costo_general_for__(costogeneral)

# filter

@costogeneral_bp.route("/filter/id/<id>",methods=["POST"])
def costo_general_route_filter_id(id):
    
    costogeneral = costo_general_controller_get_by_id(id)
    
    return __costo_general_for__(costogeneral)
    

@costogeneral_bp.route("/filter/id_material/<id>",methods=["POST"])
def costo_general_route_filter_material_id(id):
    
    costogeneral = costo_general_controller_get_by_material(id)
    
    return __costo_general_for__(costogeneral)
    

@costogeneral_bp.route("/filter/fecha",methods=["POST"])
def costo_general_route_filter_fecha():
    fecha = request.get_json()
    
    
    costogeneral = costo_general_controller_get_by_fecha(fecha)
    
    return __costo_general_for__(costogeneral)
    


# especial
def __costo_general_for__(costogeneral):
    
    _return = []
    
    try:
        for cg in costogeneral:
            
            fecha_date = datetime.strftime(cg.fecha,"%Y-%m-%d")
            
            _return.append(cg.get_dict())
            
        return _return
    except:
        return costogeneral
