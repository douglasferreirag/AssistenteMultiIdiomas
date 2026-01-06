let mediaRecorder;
let audioChunks = [];

// =====================
// Elementos
// =====================
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const audioSelect = document.getElementById("audioSelect");
const audioPlayer = document.getElementById("audioPlayer");
const playButton = document.getElementById("playAudio");
const resultadoDiv = document.getElementById("transcricao");
const transcreverButton = document.getElementById("transcrever");

// =====================
// Estado inicial
// =====================
playButton.disabled = true;
transcreverButton.disabled = true;

// =====================
// Gravação de áudio
// =====================
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

    await fetch("http://127.0.0.1:8000/audios", {
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
  try {
    const response = await fetch("http://127.0.0.1:8000/audios");

    if (!response.ok) {
      console.error("Erro ao listar áudios");
      return;
    }

    const audios = await response.json();

    audioSelect.innerHTML = "";

    const defaultOption = document.createElement("option");
    defaultOption.value = "";
    defaultOption.textContent = "Selecione um áudio";
    defaultOption.disabled = true;
    defaultOption.selected = true;

    audioSelect.appendChild(defaultOption);

    audios.forEach((audio) => {
      const option = document.createElement("option");
      option.value = audio;
      option.textContent = audio;
      audioSelect.appendChild(option);
    });

    

  } catch (error) {
    console.error("Erro ao carregar áudios:", error);
  }
}

// =====================
// Tocar áudio
// =====================
playButton.addEventListener("click", () => {
  if (!audioPlayer.src) return;
  audioPlayer.play().catch(console.error);
 
});

// =====================
// Seleção de áudio
// =====================
audioSelect.addEventListener("change", async () => {
  const filename = audioSelect.value;

  if (!filename) {
    // Nenhum áudio selecionado → desativa tudo
    playButton.disabled = true;
    transcreverButton.disabled = true;
    audioPlayer.style.display = "none";
    audioPlayer.src = "";
    resultadoDiv.textContent = "";
    return;
  }

  // 🔹 Áudio selecionado → libera botões
  playButton.disabled = false;
  transcreverButton.disabled = false;

  // 🔹 Configura player
  audioPlayer.src = `http://127.0.0.1:8000/audios/${encodeURIComponent(filename)}`;
  audioPlayer.style.display = "block";
  audioPlayer.load(); // garante que o player carregue o arquivo

  // 🔹 Carrega transcrição se existir
  await carregarTranscricao(filename);
});

// =====================
// Transcrever áudio
// =====================
transcreverButton.addEventListener("click", async () => {
  const filename = audioSelect.value;
  if (!filename) return;

  resultadoDiv.textContent = "Transcrevendo...";
  transcreverButton.disabled = true;

  const response = await fetch("http://127.0.0.1:8000/transcricoes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ filename })
  });

  const data = await response.json();
  resultadoDiv.textContent = data.texto;
});

// =====================
// Carregar transcrição existente
// =====================
async function carregarTranscricao(audioFile) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/transcricoes/${audioFile}`
    );

    if (!response.ok) {
      resultadoDiv.textContent = "Nenhuma transcrição encontrada.";
      return;
    }

    const data = await response.json();
    resultadoDiv.textContent = data.texto;

  } catch (error) {
    console.error(error);
    resultadoDiv.textContent = "Erro ao carregar transcrição.";
  }
}

// =====================
// 🔥 GARANTE QUE CARREGA AO ABRIR A PÁGINA
// =====================
document.addEventListener("DOMContentLoaded", carregarAudios);
