from flask import Blueprint, request

from ..controllers.venta_controller import (
    venta_controller_get_all,
    venta_controller_register,
    venta_controller_get_by_filter,
    venta_controller_delete_by_id,
    venta_controller_get_by_id
)

venta_bp = Blueprint("venta",__name__)


@venta_bp.route("/",methods=["GET"])
def venta_route_index():
    venta = venta_controller_get_all()
    return __venta_for__(venta)


@venta_bp.route("/register",methods=["POST"])
def venta_route_register():
    venta_request = request.get_json()
    venta = venta_controller_register(venta_request)
    return __venta_for__(venta)



@venta_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def venta_route_delete_by_id(id):
    venta = venta_controller_delete_by_id(id)
    return __venta_for__(venta)

    

# Filter

@venta_bp.route("/filter/id/<id>",methods=["POST"])
def venta_route_filter_id(id):
    #Retornar el filtrado de la tabla venta por id
    venta = venta_controller_get_by_id(id)
    
    return __venta_for__(venta)


@venta_bp.route("/filter",methods=["POST"])
def cliente_route_filter():
    
    args = request.get_json()
    
    venta = venta_controller_get_by_filter(args)
    
    return __venta_for__(venta)




## especial ##
def __venta_for__(venta):
    _return = []
    
    try:
        for v in venta:
            
            _return.append(v.get_dict())
            
        return _return
    except:
        return venta
