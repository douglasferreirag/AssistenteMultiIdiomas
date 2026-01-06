# Assistente de Voz Multi-Idiomas com Whisper e ChatGPT

📍 Branch: `PropostaInicial`

Este projeto apresenta a **proposta inicial de um assistente de voz inteligente e multilíngue**, capaz de receber áudios, realizar transcrição automática e gerar respostas utilizando modelos de inteligência artificial.

A aplicação combina **reconhecimento de fala** com **IA generativa**, servindo como base para futuras evoluções como TTS, automação e integração com outros sistemas.

---

## 🎯 Objetivo

O principal objetivo do projeto é demonstrar:

- Integração prática com **modelos de IA**
- Processamento de áudio de forma automatizada
- Separação clara entre frontend e backend
- Organização de um fluxo completo: áudio → texto → resposta inteligente

O foco desta proposta não é apenas o resultado final, mas a **construção de uma base técnica sólida**, extensível e reutilizável.

---

## 🧠 O que o sistema faz

De forma resumida, o assistente funciona assim:

1. O usuário envia um áudio
2. O sistema transcreve o áudio automaticamente
3. O texto é processado por um modelo de linguagem
4. Uma resposta contextual é gerada
5. A transcrição pode ser reaproveitada futuramente

Esse fluxo permite interações em **diferentes idiomas**, aproveitando o suporte multilíngue do Whisper.

---

## 🤖 Inteligência Artificial no Projeto

O projeto utiliza dois componentes principais de IA:

### 🎙️ Whisper (OpenAI)
- Responsável pela transcrição de áudio
- Suporte a múltiplos idiomas
- Configurado para reduzir alucinações e manter fidelidade ao áudio

### 💬 ChatGPT
- Processa o texto transcrito
- Gera respostas coerentes e contextualizadas
- Permite evolução futura para diálogos mais longos e personalizados

---

## 🖥️ Interface com o Usuário

O frontend foi pensado para ser simples e funcional, permitindo:

- Envio ou gravação de áudio
- Visualização da transcrição
- Recebimento da resposta gerada pela IA
- Controle de ações repetidas (ex.: evitar retrabalho de transcrição)

---

## ⚙️ Execução do Projeto

O projeto já conta com ambiente virtual Python configurado e pode ser executado localmente com poucos passos:

- Ativar o ambiente virtual
- Instalar dependências
- Configurar a chave da OpenAI
- Iniciar o backend
- Executar o frontend

Esse setup facilita testes, manutenção e futuras melhorias.

---

## 📌 Estado Atual

- ✅ Pipeline de transcrição funcional
- ✅ Integração com IA generativa
- ✅ Comunicação frontend ↔ backend
- 🚧 Interface em evolução
- 🚧 Novas funcionalidades planejadas

---

## 🚀 Possíveis Evoluções

Algumas extensões naturais do projeto incluem:


- Cache inteligente de transcrições
- Histórico de conversas
- Autenticação de usuários
- Logs e métricas
- Deploy em nuvem

---

## 🧩 Considerações Finais

Este projeto foi desenvolvido com foco em **aprendizado, arquitetura e integração com IA**, servindo como base para aplicações mais complexas envolvendo voz, linguagem natural e automação.

Ele demonstra domínio de conceitos modernos de desenvolvimento e uso prático de inteligência artificial em aplicações reais.
