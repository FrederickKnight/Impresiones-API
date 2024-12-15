from sqlalchemy import text

from ..src.impresion_conn import (
    impresion_conn
    )


from flask import Response
from datetime import datetime


from ..models.models import (
    Folios,
    Clientes,
    Costos_Generales
    )

from ..utils.folio_id_generador import FolioIdGenerador

sesion = impresion_conn()


def folio_controller_get_all():
    return sesion.query(Folios).all()


def folio_controller_register(folio):
    
    _folio = FolioIdGenerador().generate_ticket_id()
    _id_cliente = None
    _id_costo_general = None
    _fecha = None
    _concepto = None
    
    if "id_cliente" in folio:
        if not (sesion.query(Clientes).filter_by(id_cliente=folio["id_cliente"]).first()):
            return Response({"result":"No se encuentra ese cliente"}
                            ,status=400,mimetype="application/json")
        _id_cliente = folio["id_cliente"]
        
    if "id_costo_general" in folio:
        if not (sesion.query(Costos_Generales).filter_by(id_costo_general=folio["id_costo_general"]).first()):
            return Response({"result":"No se encuentra ese costo general"}
                            ,status=400,mimetype="application/json")
        _id_costo_general = folio["id_costo_general"]
        
    if "fecha" in folio:
        _fecha = folio["fecha"]
    if "concepto" in folio:
        _concepto = folio["concepto"]
        
    mFolio = Folios(
        folio=_folio,
        id_cliente = _id_cliente,
        id_costo_general = _id_costo_general,
        fecha = datetime.strptime(_fecha, "%Y-%m-%d").date(),
        concepto = _concepto
    )
    
    sesion.add(mFolio)
    sesion.commit()
    return sesion.query(Folios).filter_by(id_folio=mFolio.id_folio).all()
    
def folio_controller_delete_by_id(id):
    
    try:
        _f=sesion.query(Folios).filter_by(id_folio = id).first()
        print(id)
        sesion.delete(_f)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")

    
def folio_controller_get_by_folio(folio):
    try:
        _folio = folio["folio"]
    except:
        _folio = None
    
    query = sesion.query(Folios).filter_by(folio=_folio).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")
    


def folio_controller_get_by_fecha(fecha):
    
    try:
        data_fecha = datetime.strptime(fecha["fecha"],"%Y-%m-%d")
        _fecha = data_fecha.strftime("%Y-%m-%d")
    except:
        _fecha = None
        

    query = sesion.query(Folios).where(text(f'fecha = "{_fecha}"')).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")
    
def folio_controller_get_by_id(id):
    query = sesion.query(Folios).filter_by(id_folio=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")
