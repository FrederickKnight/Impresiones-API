from sqlalchemy import text

from flask import Response
from datetime import datetime

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Costos_Generales,
    Materiales
    )


sesion = impresion_conn()


def costo_general_controller_get_all():
    return sesion.query(Costos_Generales).all()
    

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
            return Response({"result":"No se encuentra ese material"}
                            ,status=400,mimetype="application/json")
            
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
    return sesion.query(Costos_Generales).filter_by(id_costo_general=mCostogeneral.id_costo_general).all()
    
    
def costo_general_controller_delete_by_id(id):
    
    try:
        _cg=sesion.query(Costos_Generales).filter_by(id_costo_general = id).first()
        sesion.delete(_cg)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")


#filter
def costo_general_controller_get_by_id(id):
    query = sesion.query(Costos_Generales).filter_by(id_costo_general=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")


def costo_general_controller_get_by_fecha(fecha):
    
    try:
        data_fecha = datetime.strptime(fecha["fecha"],"%Y-%m-%d")
        _fecha = data_fecha.strftime("%Y-%m-%d")
    except:
        _fecha = None
    
    query = sesion.query(Costos_Generales).where(text(f'fecha = "{_fecha}"')).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")
    


def costo_general_controller_get_by_material(id_material):
    print(id_material)
    query = sesion.query(Costos_Generales).filter_by(id_material=id_material).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")