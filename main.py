from flask import Flask

#blueprints routes
from app.routes import (
    cliente_route,
    modelo_route,
    tematica_route,
    material_route,
    costogeneral_route,
    folio_route,
    venta_route,
    inventario_route,
    inventario_material_route,
    error_folio_route,
    subtematica_route
)



app = Flask(__name__)

#blueprints
app.register_blueprint(cliente_route.cliente_bp,url_prefix="/api/cliente")
app.register_blueprint(modelo_route.modelo_bp,url_prefix="/api/modelo")
app.register_blueprint(tematica_route.tematica_bp,url_prefix="/api/tematica")
app.register_blueprint(subtematica_route.subtematica_bp,url_prefix="/api/subtematica")
app.register_blueprint(material_route.material_bp,url_prefix="/api/material")
app.register_blueprint(costogeneral_route.costogeneral_bp,url_prefix="/api/costogeneral")
app.register_blueprint(folio_route.folio_bp,url_prefix="/api/folio")
app.register_blueprint(venta_route.venta_bp,url_prefix="/api/venta")
app.register_blueprint(inventario_route.inventario_bp,url_prefix="/api/inventario")
app.register_blueprint(inventario_material_route.inventario_material_bp,url_prefix="/api/inventariomaterial")
app.register_blueprint(error_folio_route.error_folio_bp,url_prefix="/api/errorfolio")


if __name__ == "__main__":
    
    app.run(debug=True)
    