import whisper

# Model pequeno = menos criatividade
model = whisper.load_model("small")

def transcrever_audio(audio_path: str) -> str:
    result = model.transcribe(
        audio_path,
        language="pt",
        task="transcribe",

        # 🔒 Controle de alucinação
        temperature=0,
        condition_on_previous_text=False,
        no_speech_threshold=0.5,
        logprob_threshold=-1.0,
        compression_ratio_threshold=2.0,

        # 🎯 Prompt extremamente restritivo
        initial_prompt=(
            "Transcreva apenas o que for falado. "
            "Não complete frases. "
            "Não invente palavras. "
            "Não corrija datas, números ou horários. "
            "Se algo não estiver claro, transcreva de forma literal."
        ),

        # ⛔ Evita inferência longa
        beam_size=1,
        best_of=1
    )

    texto = result.get("text", "").strip()

    return texto