from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil
from datetime import datetime
import uuid
import whisper

# ======================
# App
# ======================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# Pastas
# ======================
UPLOAD_DIR = "audios"
TRANSCRICOES_DIR = "transcricoes"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TRANSCRICOES_DIR, exist_ok=True)

# ======================
# Whisper
# ======================
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

