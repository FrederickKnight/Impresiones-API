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
    return  __material_for__(material)
    

@material_bp.route("/register",methods=["POST"])
def material_route_register():
    material_request = request.get_json()
    material = material_controller_register(material_request)
    return __material_for__(material)

@material_bp.route("/update",methods=["PUT"])
def material_route_update():
    #update tematica
    material_request = request.get_json()
    material = material_controller_update(material_request)
    return __material_for__(material)

@material_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def material_route_delete_by_id(id):
    material = material_controller_delete_by_id(id)
    return __material_for__(material)
    

@material_bp.route("/delete",methods=["DELETE"])
def material_route_delete():
    material_request = request.get_json()
    material = material_controller_delete(material_request)
    return __material_for__(material)


# Filter

@material_bp.route("/filter/id/<id>",methods=["POST"])
def modelo_route_filter_id(id):
    
    material = material_controller_get_by_id(id)
    
    return __material_for__(material)
    


@material_bp.route("/filter",methods=["POST"])
def material_route_filter():
    
    args = request.get_json()
    
    material = material_controller_get_by_filter(args)
    
    return __material_for__(material)



# especial

def __material_for__(material):
    _return = []
    
    try:
        for ml in material:
            
            _return.append({
                "id":ml.id_material,
                "nombre":ml.nombre,
                "marca":ml.marca,
                "color":ml.color,
                "medicion":ml.medicion
            })
            
        return _return
    except:
        return material