from app.routes import audio
from app.routes import transcrever


def include_routes(app):
    app.include_router(audio.router)
    app.include_router(transcrever.router)
 
