from sqlalchemy import text

from flask import Response
from datetime import datetime

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    CostosGenerales,
    Materiales
    )


sesion = impresion_conn()


def costo_general_controller_get_all():
    return sesion.query(CostosGenerales).all()
    

def costo_general_controller_register(costogeneral):
    
    _esperados = {
        "fecha":None,
        "id_material":None,
        "desgaste":None,
        "electricidad":None,
        "riesgo_fallo_menor":None,
        "riesgo_fallo_mediano":None,
        "riesgo_fallo_mayor":None,
        "margen":None
    }
    
    if "id_material" in costogeneral:
        if not (sesion.query(Materiales).filter_by(id_material=costogeneral["id_material"]).first()):
            return Response({"result":"No se encuentra ese material"}
                            ,status=400,mimetype="application/json")
            
    _esperados.update({key:costogeneral[key] for key in _esperados if key in costogeneral})
        
    mCostogeneral = CostosGenerales(
        fecha=datetime.strptime(_esperados["fecha"], "%Y-%m-%d").date(),
        id_material = _esperados["id_material"],
        desgaste=_esperados["desgaste"],
        electricidad=_esperados["electricidad"],
        riesgo_fallo_menor=_esperados["riesgo_fallo_menor"],
        riesgo_fallo_mediano=_esperados["riesgo_fallo_mediano"],
        riesgo_fallo_mayor=_esperados["riesgo_fallo_mayor"],
        margen=_esperados["margen"]
    )
    
    sesion.add(mCostogeneral)
    sesion.commit()
    return sesion.query(CostosGenerales).filter_by(id_costo_general=mCostogeneral.id_costo_general).all()
    
    
def costo_general_controller_delete_by_id(id):
    
    try:
        _cg=sesion.query(CostosGenerales).filter_by(id_costo_general = id).first()
        sesion.delete(_cg)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")


#filter
def costo_general_controller_get_by_id(id):
    query = sesion.query(CostosGenerales).filter_by(id_costo_general=id).all()
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
    
    query = sesion.query(CostosGenerales).where(text(f'fecha = "{_fecha}"')).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")
    


def costo_general_controller_get_by_material(id_material):
    print(id_material)
    query = sesion.query(CostosGenerales).filter_by(id_material=id_material).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")