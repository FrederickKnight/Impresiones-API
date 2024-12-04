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
    _return = __tematica_for__(tematica)
    return _return  


@tematica_bp.route("/register",methods=["POST"])
def tematica_route_register():
    tematica = request.get_json()
    return tematica_controller_register(tematica)

@tematica_bp.route("/update",methods=["PUT"])
def tematica_route_update():
    #update tematica
    tematica = request.get_json()
    tematica_controller_update(tematica)
    return "update"

@tematica_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def tematica_route_delete_by_id(id):
    return tematica_controller_delete_by_id(id)
    

@tematica_bp.route("/delete",methods=["DELETE"])
def tematica_route_delete():
    tematica = request.get_json()
    return tematica_controller_delete(tematica)


# Filter

@tematica_bp.route("/filter/id/<id>",methods=["POST"])
def modelo_route_filter_id(id):
    #Retornar el filtrado de la tabla tematica por id
    tematica = tematica_controller_get_by_id(id)
    
    _return = __tematica_for__(tematica)
    return _return


@tematica_bp.route("/filter/nombre/<nombre>",methods=["POST"])
def modelo_route_filter_nombre(nombre):
    #Retornar el filtrado de la tabla tematica por nombre
    tematica = tematica_controller_get_by_nombre(nombre)
    
    _return = __tematica_for__(tematica)
    return _return

## especial ##
def __tematica_for__(tematica):
    _return = []
    
    for ml in tematica:
        
        _return.append({
            "id":ml.id_tematica,
            "nombre":ml.nombre
        })
        
    return _return
