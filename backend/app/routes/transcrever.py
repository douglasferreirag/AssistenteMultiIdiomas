from fastapi import APIRouter, HTTPException
import os
from app.models.transcricao import TranscricaoRequest
from app.services.whisper_service import transcrever_audio
from app.utils.file_utils import salvar_transcricao
from app.core.config import TRANSCRICOES_DIR, UPLOAD_DIR

router = APIRouter(
    prefix="/transcricoes",
    tags=["Transcrições"]
)


@router.post("")
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



@router.get("/{audio_filename}")
def get_transcricao(audio_filename: str):
    # segurança: remove qualquer path
    clean_name = os.path.basename(audio_filename)

    # troca extensão para .txt
    base_name = os.path.splitext(clean_name)[0]
    txt_filename = f"{base_name}.txt"

    txt_path = os.path.join(TRANSCRICOES_DIR, txt_filename)

    if not os.path.exists(txt_path):
        raise HTTPException(status_code=404, detail="Transcrição não encontrada")

    with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
        texto = f.read()

    return {
        "texto": texto,
        "arquivo_txt": txt_filename
    }
