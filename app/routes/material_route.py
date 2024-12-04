from flask import Blueprint, request

from ..controllers.material_controller import (
    material_controller_get_all,
    material_controller_update,
    material_controller_register,
    material_controller_delete,
    material_controller_delete_by_id,
    material_controller_get_by_id,
    material_controller_get_by_filter
)


material_bp = Blueprint("material",__name__)


@material_bp.route("/",methods=["GET"])
def material_route_index():
    material = material_controller_get_all()
    _return = __material_for__(material)
    return _return



@material_bp.route("/register",methods=["POST"])
def material_route_register():
    material = request.get_json()
    return material_controller_register(material)

@material_bp.route("/update",methods=["PUT"])
def material_route_update():
    #update tematica
    material = request.get_json()
    material_controller_update(material)
    return "update"

@material_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def material_route_delete_by_id(id):
    return material_controller_delete_by_id(id)
    

@material_bp.route("/delete",methods=["DELETE"])
def material_route_delete():
    material = request.get_json()
    return material_controller_delete(material)


# Filter

@material_bp.route("/filter/id/<id>",methods=["POST"])
def modelo_route_filter_id(id):
    #Retornar el filtrado de la tabla material por id
    material = material_controller_get_by_id(id)
    
    _return = __material_for__(material)
    return _return


@material_bp.route("/filter",methods=["POST"])
def material_route_filter():
    #introducir args por medio de json en request
    #Retornar el filtrado de la tabla material, con cualquer arg
    args = request.get_json()
    
    material = material_controller_get_by_filter(args)
    
    _return = __material_for__(material)

    return _return


# especial

def __material_for__(material):
    _return = []
    
    for ml in material:
        
        _return.append({
            "id":ml.id_material,
            "nombre":ml.nombre,
            "marca":ml.marca,
            "color":ml.color,
            "medicion":ml.medicion
        })
        
    return _return
