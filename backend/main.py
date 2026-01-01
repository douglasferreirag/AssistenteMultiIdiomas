from pathlib import Path
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil
from datetime import datetime
import uuid
import whisper

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "audios"
os.makedirs(UPLOAD_DIR, exist_ok=True)

model = whisper.load_model("base")

# ======================
# Upload de áudio
# ======================
@app.post("/upload-audio")
async def upload_audio(audio: UploadFile = File(...)):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    uid = uuid.uuid4().hex[:8]
    filename = f"audio_{timestamp}_{uid}.wav"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    return {"file": filename}

# ======================
# Listar áudios
# ======================
@app.get("/audios")
def list_audios():
    files = sorted(os.listdir(UPLOAD_DIR))
    return {"audios": files}

# ======================
# Transcrição
# ======================
# Pastas
BASE_DIR = Path(__file__).parent
AUDIOS_DIR = BASE_DIR / "audios"

# Carrega o modelo uma única vez
model = whisper.load_model("small")


class TranscribeRequest(BaseModel):
    filename: str


@app.post("/transcribe")
def transcribe_audio(data: TranscribeRequest):
    record_file = AUDIOS_DIR / data.filename

    if not record_file.exists():
        raise HTTPException(
            status_code=404,
            detail="Arquivo de áudio não encontrado"
        )

    result = model.transcribe(
        str(record_file),
        fp16=False,
        language="pt"
    )

    transcription = result["text"]

    return {
        "text": transcription
    }