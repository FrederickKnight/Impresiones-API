from sqlalchemy import text

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Costos_Generales,
    Materiales
    )

from datetime import datetime


sesion = impresion_conn()


def costo_general_controller_get_all():
    costogeneral = sesion.query(Costos_Generales).all()
    return costogeneral


def costo_general_controller_register(costogeneral):
    _fecha = None
    _id_material = None
    _desgaste = None
    _electricidad = None
    _riesgo_fallo_menor = None
    _riesgo_fallo_mediano = None
    _riesgo_fallo_mayor = None
    _margen = None
  
    if "fecha" in costogeneral:
        _fecha = costogeneral["fecha"]
    if "id_material" in costogeneral:
        if not (sesion.query(Materiales).filter_by(id_material=costogeneral["id_material"]).first()):
            return "No se encuentra ese material registrado aun"
        _id_material = costogeneral["id_material"]
    if "desgaste" in costogeneral:
        _desgaste = costogeneral["desgaste"] 
    if "electricidad" in costogeneral:
        _electricidad = costogeneral["electricidad"] 
    if "riesgo_fallo_menor" in costogeneral:
        _riesgo_fallo_menor = costogeneral["riesgo_fallo_menor"] 
    if "riesgo_fallo_mediano" in costogeneral:
        _riesgo_fallo_mediano = costogeneral["riesgo_fallo_mediano"] 
    if "riesgo_fallo_mayor" in costogeneral:
        _riesgo_fallo_mayor = costogeneral["riesgo_fallo_mayor"] 
    if "margen" in costogeneral:
        _margen = costogeneral["margen"] 
        
        
    mCostogeneral = Costos_Generales(
        fecha=datetime.strptime(_fecha, "%Y-%m-%d").date(),
        id_material = _id_material,
        desgaste=_desgaste,
        electricidad=_electricidad,
        riesgo_fallo_menor=_riesgo_fallo_menor,
        riesgo_fallo_mediano=_riesgo_fallo_mediano,
        riesgo_fallo_mayor=_riesgo_fallo_mayor,
        margen=_margen
    )
    
    sesion.add(mCostogeneral)
    sesion.commit()
    return f"registrando costo general"
    
    
def costo_general_controller_delete_by_id(id):
    
    try:
        _cg=sesion.query(Costos_Generales).filter_by(id_costo_general = id).first()
        print(_cg)
        sesion.delete(_cg)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return "Borrado con exito"


#filter
def costo_general_controller_get_by_id(id):
    costogeneral = sesion.query(Costos_Generales).filter_by(id_costo_general=id).all()
    return costogeneral


def costo_general_controller_get_by_fecha(fecha):
    
    try:
        _fecha = fecha["fecha"]
    except:
        _fecha = None
        

    costogeneral = sesion.query(Costos_Generales).filter_by(fecha=_fecha).all()
    return costogeneral


def costo_general_controller_get_by_material(id_material):
    costogeneral = sesion.query(Costos_Generales).filter_by(id_material=id_material).all()
    return costogeneral