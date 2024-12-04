from flask import Blueprint, request

from ..controllers.modelo_controller import (
    modelo_controller_get_all,
    modelo_controller_register,
    modelo_controller_get_by_filter,
    modelo_controller_get_by_id,
    modelo_controller_delete_by_id,
    modelo_controller_delete,
    modelo_controller_update
)

modelo_bp = Blueprint("modelo",__name__)


@modelo_bp.route("/",methods=["GET"])
def modelo_route_index():
    modelo = modelo_controller_get_all()
    _return = __modelo__for(modelo)
    return _return

@modelo_bp.route("/register",methods=["POST"])
def modelo_route_register():
    modelo = request.get_json()
    return modelo_controller_register(modelo)

@modelo_bp.route("/update",methods=["PUT"])
def modelo_route_update():
    #update modelo
    modelo = request.get_json()
    modelo_controller_update(modelo)
    return "update"

@modelo_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def modelo_route_delete_by_id(id):
    return modelo_controller_delete_by_id(id)
    
    
@modelo_bp.route("/delete",methods=["DELETE"])
def modelo_route_delete():
    cliente = request.get_json()
    return modelo_controller_delete(cliente)


# filters
@modelo_bp.route("/filter",methods=["POST"])
def modelo_route_filter():
    args = request.get_json()
    
    modelo = modelo_controller_get_by_filter(args)
    
    _return = __modelo__for(modelo)

    return _return

@modelo_bp.route("/filter/id/<id>",methods=["POST"])
def modelo_route_filter_id(id):
    #Retornar el filtrado de la tabla modelo por id
    modelo = modelo_controller_get_by_id(id)
    
    _return = __modelo__for(modelo)
    return _return

## especiales ##
def __modelo__for(modelo):
    _return = []
    
    for ml in modelo:
        
        _return.append({
            "id":ml.id_modelo,
            "nombre":ml.nombre,
            "id_tematica":ml.id_tematica,
            "descripcion":ml.descripcion,
            "direccion_archivo":ml.direccion_archivo
        })
        
    return _return
