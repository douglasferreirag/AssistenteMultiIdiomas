let mediaRecorder;
let audioChunks = [];

// =====================
// Gravação de áudio
// =====================
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const audioSelect = document.getElementById("audioSelect");
const resultado = document.getElementById("resultado");
const transcreverButton = document.getElementById("transcrever");

startButton.addEventListener("click", async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  audioChunks = [];

  mediaRecorder.ondataavailable = (event) => {
    audioChunks.push(event.data);
  };

  mediaRecorder.start();

  startButton.disabled = true;
  stopButton.disabled = false;
});

stopButton.addEventListener("click", () => {
  mediaRecorder.stop();

  mediaRecorder.onstop = async () => {
    const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
    const formData = new FormData();
    formData.append("audio", audioBlob, "request_audio.wav");

    await fetch("http://127.0.0.1:8000/upload-audio", {
      method: "POST",
      body: formData
    });

    alert("Áudio enviado com sucesso!");
    carregarAudios();
  };

  startButton.disabled = false;
  stopButton.disabled = true;
});

// =====================
// Listar áudios gravados
// =====================
async function carregarAudios() {
  const response = await fetch("http://127.0.0.1:8000/audios");
  const audios = await response.json();

  audioSelect.innerHTML = "";

  audios.forEach((audio) => {
    const option = document.createElement("option");
    option.value = audio;
    option.textContent = audio;
    audioSelect.appendChild(option);
  });
}

// =====================
// Transcrever áudio
// =====================
transcreverButton.addEventListener("click", async () => {
  const filename = audioSelect.value;

  if (!filename) {
    alert("Selecione um áudio");
    return;
  }

  resultado.textContent = "⏳ Transcrevendo...";

  const response = await fetch("http://127.0.0.1:8000/transcrever", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ filename })
  });

  const data = await response.json();
  resultado.textContent = data.texto;
});

// Carrega os áudios ao abrir a página
carregarAudios();
