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
    return __modelo__for(modelo)

@modelo_bp.route("/register",methods=["POST"])
def modelo_route_register():
    modelo_request = request.get_json()
    modelo = modelo_controller_register(modelo_request)
    return __modelo__for(modelo)
    

@modelo_bp.route("/update",methods=["PUT"])
def modelo_route_update():
    #update modelo
    modelo_request = request.get_json()
    modelo = modelo_controller_update(modelo_request)
    return __modelo__for(modelo)
    
    

@modelo_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def modelo_route_delete_by_id(id):
    modelo =  modelo_controller_delete_by_id(id)
    return __modelo__for(modelo)

    
    
@modelo_bp.route("/delete",methods=["DELETE"])
def modelo_route_delete():
    modelo_request = request.get_json()
    modelo =  modelo_controller_delete(modelo_request)
    return __modelo__for(modelo)



# filters
@modelo_bp.route("/filter",methods=["POST"])
def modelo_route_filter():
    args = request.get_json()
    
    modelo = modelo_controller_get_by_filter(args)
    
    return __modelo__for(modelo)

@modelo_bp.route("/filter/id/<id>",methods=["POST"])
def modelo_route_filter_id(id):
    #Retornar el filtrado de la tabla modelo por id
    modelo = modelo_controller_get_by_id(id)
    return __modelo__for(modelo)

## especiales ##
def __modelo__for(modelo):
    _return = []
    
    try:
        for ml in modelo:
            
            _return.append({
                "id":ml.id_modelo,
                "nombre":ml.nombre,
                "id_subtematica":ml.id_subtematica,
                "descripcion":ml.descripcion,
                "direccion_archivo":ml.direccion_archivo
            })
            
        return _return
    except:
        return modelo
