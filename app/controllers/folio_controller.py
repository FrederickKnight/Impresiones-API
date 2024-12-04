from sqlalchemy import text

from ..src.impresion_conn import (
    impresion_conn
    )

from ..models.models import (
    Folios,
    Clientes,
    Costos_Generales
    )

from datetime import datetime

from ..utils.folio_id_generador import FolioIdGenerador

sesion = impresion_conn()


def folio_controller_get_all():
    folios = sesion.query(Folios).all()
    return folios


def folio_controller_register(folio):
    
    _folio = FolioIdGenerador().generate_ticket_id()
    _id_cliente = None
    _id_costo_general = None
    _fecha = None
    _concepto = None
    
    if "id_cliente" in folio:
        if not (sesion.query(Clientes).filter_by(id_cliente=folio["id_cliente"]).first()):
            return "No se encuentra ese cliente registrado aun"
        _id_cliente = folio["id_cliente"]
    if "id_costo_general" in folio:
        if not (sesion.query(Costos_Generales).filter_by(id_costo_general=folio["id_costo_general"]).first()):
            return "No se encuentra ese costo general registrado aun"
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
    return _folio

def folio_controller_update(folio):
    _id = folio["id"]
    _data = folio
    _folio = sesion.query(Folios).filter_by(id_folio=_id).first()
    
    if "folio" in _data:
        _folio.folio = _data["folio"]
    
    
    sesion.merge(_folio)
    sesion.flush()
    sesion.commit()

def folio_controller_delete_by_id(id):
    
    try:
        _f=sesion.query(Folios).filter_by(id_folio = id).first()
        print(_f)
        sesion.delete(_f)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return "Borrado con exito"
    


def folio_controller_get_by_fecha(fecha):
    
    try:
        _fecha = fecha["fecha"]
    except:
        _fecha = None
        

    folio = sesion.query(Folios).filter_by(fecha=_fecha).all()
    return folio
    