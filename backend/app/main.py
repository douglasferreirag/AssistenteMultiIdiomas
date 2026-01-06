from fastapi import FastAPI

from app.core.cors import setup_cors
from app.core.static import setup_static_files
from app.routes import include_routes

app = FastAPI()

# Configurações
setup_cors(app)
setup_static_files(app)
include_routes(app)
