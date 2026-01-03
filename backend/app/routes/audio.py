import os
from fastapi import APIRouter, UploadFile, File
from app.utils.file_utils import salvar_audio
from app.core.config import UPLOAD_DIR

router = APIRouter()

@router.post("/upload-audio")
async def upload_audio(audio: UploadFile = File(...)):
    filename = salvar_audio(audio)
    return {"file": filename}

@router.get("/audios")
def listar_audios():
    if not os.path.exists(UPLOAD_DIR):
        return []

    return [
        f for f in os.listdir(UPLOAD_DIR)
        if f.endswith((".wav", ".mp3", ".m4a"))
    ]