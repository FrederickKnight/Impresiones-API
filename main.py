from flask import (
    Flask,
    request,
    Blueprint
    )

#blueprints routes
from app.routes import (
    cliente_route,
    modelo_route,
    tematica_route,
    material_route,
    costogeneral_route,
    folio_route,
    venta_route
)



app = Flask(__name__)

#blueprints
app.register_blueprint(cliente_route.cliente_bp,url_prefix="/api/cliente")
app.register_blueprint(modelo_route.modelo_bp,url_prefix="/api/modelo")
app.register_blueprint(tematica_route.tematica_bp,url_prefix="/api/tematica")
app.register_blueprint(material_route.material_bp,url_prefix="/api/material")
app.register_blueprint(costogeneral_route.costogeneral_bp,url_prefix="/api/costogeneral")
app.register_blueprint(folio_route.folio_bp,url_prefix="/api/folio")
app.register_blueprint(venta_route.venta_bp,url_prefix="/api/venta")


if __name__ == "__main__":
    
    app.run(debug=True)
    