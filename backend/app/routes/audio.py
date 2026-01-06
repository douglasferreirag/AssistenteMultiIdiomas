import os
import mimetypes
from fastapi import APIRouter, Request, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.utils.file_utils import salvar_audio
from app.core.config import UPLOAD_DIR

router = APIRouter(
    prefix="/audios",  # prefixo base
    tags=["Áudios"]
)




# =====================
# Upload de áudio
# POST /audios/upload
# =====================

@router.post("")  # rota base → POST /audios
async def upload_audio(audio: UploadFile = File(...)):
    filename = salvar_audio(audio)  # vai salvar em app/audios
    return {"file": filename}


# =====================
# Listar áudios
# GET /audios
# =====================
@router.get("")
def listar_audios():
    if not os.path.exists(UPLOAD_DIR):
        return []

    return [
        f for f in os.listdir(UPLOAD_DIR)
        if f.lower().endswith((".wav", ".mp3", ".m4a"))
    ]

# =====================
# Servir áudio
# GET /audios/{filename}
# =====================
@router.get("/{filename}")
def get_audio(filename: str):
    # segurança: remove qualquer caminho estranho
    clean_name = os.path.basename(filename)

    # caminho completo
    audio_path = os.path.join(UPLOAD_DIR, clean_name)

    # valida se existe
    if not os.path.isfile(audio_path):
        raise HTTPException(status_code=404, detail="Áudio não encontrado")

    # define tipo MIME correto
    media_type, _ = mimetypes.guess_type(audio_path)
    media_type = media_type or "audio/wav"

    return FileResponse(
        path=audio_path,
        media_type=media_type,
        filename=clean_name
    )