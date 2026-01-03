from pydantic import BaseModel

class TranscricaoRequest(BaseModel):
    filename: str
