import os
from fastapi.staticfiles import StaticFiles

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AUDIOS_DIR = os.path.join(BASE_DIR, "audios")

def setup_static_files(app):
    app.mount(
        "/audios",
        StaticFiles(directory=AUDIOS_DIR),
        name="audios"
    )
