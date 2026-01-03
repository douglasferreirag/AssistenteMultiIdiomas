import os
import shutil
from datetime import datetime
import uuid
from fastapi import UploadFile
from app.core.config import UPLOAD_DIR, TRANSCRICOES_DIR

def salvar_audio(audio: UploadFile) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    uid = uuid.uuid4().hex[:8]
    filename = f"audio_{timestamp}_{uid}.wav"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    return filename

def salvar_transcricao(texto: str, nome_audio: str) -> str:
    nome_txt = os.path.splitext(nome_audio)[0] + ".txt"
    caminho_txt = os.path.join(TRANSCRICOES_DIR, nome_txt)

    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(texto)

    return nome_txt
