from flask import Blueprint, request

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
    _return = __costo_general_for__(costogeneral)
    return _return  

@costogeneral_bp.route("/register",methods=["POST"])
def tematica_route_register():
    costogeneral = request.get_json()
    return costo_general_controller_register(costogeneral)


@costogeneral_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def costo_general_route_delete_by_id(id):
    return costo_general_controller_delete_by_id(id)


# filter

@costogeneral_bp.route("/filter/id/<id>",methods=["POST"])
def costo_general_route_filter_id(id):
    #Retornar el filtrado de la tabla costo_general por id
    costogeneral = costo_general_controller_get_by_id(id)
    
    _return = __costo_general_for__(costogeneral)
    return _return

@costogeneral_bp.route("/filter/id_material/<id>",methods=["POST"])
def costo_general_route_filter_material_id(id):
    #Retornar el filtrado de la tabla costo_general por material id
    costogeneral = costo_general_controller_get_by_material(id)
    
    _return = __costo_general_for__(costogeneral)
    return _return

@costogeneral_bp.route("/filter/fecha",methods=["POST"])
def costo_general_route_filter_fecha():
    fecha = request.get_json()
    #Retornar el filtrado de la tabla costo_general por fecha
    costogeneral = costo_general_controller_get_by_fecha(fecha)
    
    _return = __costo_general_for__(costogeneral)
    return _return


# especial
def __costo_general_for__(costogeneral):
    
    _return = []
    
    for cg in costogeneral:
        
        _return.append({
            "id":cg.id_costo_general,
            "fecha":cg.fecha,
            "id_material":cg.id_material,
            "desgaste":cg.desgaste,
            "electricidad":cg.electricidad,
            "riesgo_fallo_menor":cg.riesgo_fallo_menor,
            "riesgo_fallo_mediano":cg.riesgo_fallo_mediano,
            "riesgo_fallo_mayor":cg.riesgo_fallo_mayor,
            "margen":cg.margen
        })
        
        
    return _return
