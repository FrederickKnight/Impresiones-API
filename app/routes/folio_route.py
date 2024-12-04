from flask import Blueprint, request

from ..controllers.folio_controller import (
    folio_controller_get_all,
    folio_controller_register,
    folio_controller_update,
    folio_controller_delete_by_id
)


folio_bp = Blueprint("folio",__name__)


@folio_bp.route("/",methods=["GET"])
def folio_route_index():
    folio = folio_controller_get_all()
    _return = __folio_for__(folio)
    return _return  


@folio_bp.route("/register",methods=["POST"])
def folio_route_register():
    folio = request.get_json()
    return folio_controller_register(folio)

# @folio_bp.route("/update",methods=["PUT"])
# def folio_route_update():
#     #update folio
#     folio = request.get_json()
#     folio_controller_update(folio)
#     return "update"

@folio_bp.route("/delete/id/<int:id>",methods=["DELETE"])
def tematica_route_delete_by_id(id):
    return folio_controller_delete_by_id(id)
    


# especial
def __folio_for__(folio):
    _return = []
    
    for f in folio:
        
        _return.append({
            "id":f.id_folio,
            "folio":f.folio,
            "id_cliente":f.id_cliente,
            "id_costo_general":f.id_costo_general,
            "fecha":f.fecha,
            "concepto":f.concepto
        })
        
    return _return
