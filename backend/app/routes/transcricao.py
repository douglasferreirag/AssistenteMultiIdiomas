import os
from fastapi import APIRouter, HTTPException
from app.models.transcricao import TranscricaoRequest
from app.services.whisper_service import transcrever_audio
from app.utils.file_utils import salvar_transcricao
from app.core.config import UPLOAD_DIR

router = APIRouter()

@router.post("/transcrever")
def transcrever(req: TranscricaoRequest):
    audio_path = os.path.join(UPLOAD_DIR, req.filename)

    if not os.path.exists(audio_path):
        raise HTTPException(status_code=404, detail="Áudio não encontrado")

    texto = transcrever_audio(audio_path)
    arquivo_txt = salvar_transcricao(texto, req.filename)

    return {
        "texto": texto,
        "arquivo_txt": arquivo_txt
    }
