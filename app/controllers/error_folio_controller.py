from sqlalchemy import text


from ..src.impresion_conn import (
    impresion_conn
    )

from flask import Response

from ..models.models import (
    ErrorFolios
    )

sesion = impresion_conn()


def error_folio_controller_get_all():
    return sesion.query(ErrorFolios).all()


def error_folio_controller_register(error_folio):
    _id_folio = None
    _id_modelo = None
    _merma = None
    _descripcion = None
    _costo_reajustado = None
    
    
    if "id_folio" in error_folio:
        _id_folio = error_folio["id_folio"]
    if "id_modelo" in error_folio:
        _id_modelo = error_folio["id_modelo"]
    if "merma" in error_folio:
        _merma = error_folio["merma"]
    if "descripcion" in error_folio:
        _descripcion = error_folio["descripcion"]
    if "costo_reajustado" in error_folio:
        _costo_reajustado = error_folio["costo_reajustado"]
    
  
    mError_folio = ErrorFolios(
        id_folio=_id_folio,
        id_modelo=_id_modelo,
        merma=_merma,
        descripcion=_descripcion,
        costo_reajustado=_costo_reajustado
        
    )
    
    sesion.add(mError_folio)
    sesion.commit()
    return sesion.query(ErrorFolios).filter_by(id_error=mError_folio.id_error).all()



def error_folio_controller_update(error_folio):
    _id = error_folio["id"]
    _data = error_folio
    _error = sesion.query(ErrorFolios).filter_by(id_error=_id).first()
    
    if "id_folio" in _data:
        _error.id_folio = _data["id_folio"]
    if "id_modelo" in _data:
        _error.id_modelo = _data["id_modelo"]
    if "merma" in _data:
        _error.merma = _data["merma"]
    if "descripcion" in _data:
        _error.descripcion = _data["descripcion"]
    if "costo_reajustado" in _data:
        _error.costo_reajustado = _data["costo_reajustado"]
    
    sesion.merge(_error)
    sesion.flush()
    sesion.commit()
    return sesion.query(ErrorFolios).filter_by(id_error=_id).all()
    
    
def error_folio_controller_delete_by_id(id):
    
    try:
        _i=sesion.query(ErrorFolios).filter_by(id_error = id).first()
        sesion.delete(_i)
        sesion.commit()
        
    except Exception as e:
        return e
    
    finally:
        return Response(status=200,mimetype="application/json")

    
    

def error_folio_controller_get_by_filter(args):
    data = args
    esperados = ["id_folio","id_modelo","merma","costo_reajustado"]
    _where = 'where '
    
    x= 0
    for i in range(len(esperados)):
        
        if esperados[i] in data:
            if x > 0:
                _where += " and "
            x += 1
            _where += f'{esperados[i]} = "{data[esperados[i]]}"'
            
            
    query = sesion.query(ErrorFolios).from_statement(text(f"SELECT * FROM error_folio {_where}")).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")


def error_folio_controller_get_by_id(id):
    query = sesion.query(ErrorFolios).filter_by(id_error=id).all()
    if len(query) > 0:
        return query
    elif len(query) <= 0:
        return Response(status=404,mimetype="application/json")