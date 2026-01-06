import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app/core
APP_DIR = os.path.dirname(BASE_DIR)                    # sobe para app/

UPLOAD_DIR = os.path.join(APP_DIR, "audios")           # pode manter fora do app se quiser
TRANSCRICOES_DIR = os.path.join(APP_DIR, "transcricoes")  # agora dentro de app/

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TRANSCRICOES_DIR, exist_ok=True)
