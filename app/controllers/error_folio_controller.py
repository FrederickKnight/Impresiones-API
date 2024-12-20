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
    
    _esperados = {
        "id_folio":None,
        "id_modelo":None,
        "merma":None,
        "descripcion":None,
        "costo_reajustado":None
    }
    
    _esperados.update({key:error_folio[key] for key in _esperados if key in error_folio})
  
    mError_folio = ErrorFolios(
        id_folio=_esperados["id_folio"],
        id_modelo=_esperados["id_modelo"],
        merma=_esperados["merma"],
        descripcion=_esperados["descripcion"],
        costo_reajustado=_esperados["costo_reajustado"]
    )
    
    sesion.add(mError_folio)
    sesion.commit()
    return sesion.query(ErrorFolios).filter_by(id_error=mError_folio.id_error).all()



def error_folio_controller_update(error_folio):
    _id = error_folio["id"]
    _data = error_folio
    _error = sesion.query(ErrorFolios).filter_by(id_error=_id).first()
    
    _esperados = {
        "id_folio":None,
        "id_modelo":None,
        "merma":None,
        "descripcion":None,
        "costo_reajustado":None
    }
    
    _esperados.update({key:_data[key] for key in _esperados if key in _data})
    
    _error.id_folio = _esperados["id_folio"]
    _error.id_modelo = _esperados["id_modelo"]
    _error.merma = _esperados["merma"]
    _error.descripcion = _esperados["descripcion"]
    _error.costo_reajustado = _esperados["costo_reajustado"]
    
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