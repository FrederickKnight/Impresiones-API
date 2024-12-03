from flask import (
    Flask,
    request,
    Blueprint
    )

#blueprints routes
from app.routes.cliente_route import (
    cliente_bp,
    )


app = Flask(__name__)

#blueprints
app.register_blueprint(cliente_bp,url_prefix="/api/cliente")


if __name__ == "__main__":
    
    app.run(debug=True)
    