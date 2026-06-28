# 🎙️ Audio, Speech & Voice AI

> Text-to-speech, speech-to-text, voice cloning, music generation, and audio-native LLMs.

---

## Current Landscape (June 2026)

Voice AI has entered its "GPT moment" — real-time voice-to-voice conversations are sub-300ms latency, open-source TTS (Kokoro, Fish Speech) rivals commercial offerings, and audio-native LLMs (Gemini, GPT-5.5 voice mode) understand and generate speech natively without text intermediaries.

---

## 1. SPEECH-TO-TEXT (ASR — Automatic Speech Recognition)

| Model / Service | Type | Key Specs | Link |
|----------------|------|-----------|------|
| **OpenAI Whisper** | Open-source | The standard. 99 languages, multiple sizes (tiny→large-v3). MIT license. ⭐ 75,000+ | https://github.com/openai/whisper |
| **Faster-Whisper** | Open-source | CTranslate2-accelerated Whisper — 4x faster, same accuracy, lower VRAM | https://github.com/SYSTRAN/faster-whisper |
| **WhisperX** | Open-source | Whisper + word-level timestamps + speaker diarization | https://github.com/m-bain/whisperX |
| **Whisper.cpp** | Open-source | C/C++ port for CPU inference, runs on Raspberry Pi | https://github.com/ggerganov/whisper.cpp |
| **Distil-Whisper** | Open-source | 6x faster, 49% smaller, within 1% WER of Whisper large-v3 | https://github.com/huggingface/distil-whisper |
| **Deepgram** | Cloud API | Real-time streaming ASR, Nova-3 model, <300ms latency | https://deepgram.com/ |
| **AssemblyAI** | Cloud API | Universal-2 model, summarization, sentiment, chapters | https://assemblyai.com/ |
| **Google Cloud Speech** | Cloud API | Chirp 2 model, 100+ languages, streaming | https://cloud.google.com/speech-to-text |
| **Azure Speech** | Cloud API | Real-time + batch, custom models, 100+ languages | https://azure.microsoft.com/services/cognitive-services/speech-to-text/ |
| **Speechmatics** | Cloud API | Enterprise-grade, 50+ languages, real-time | https://speechmatics.com/ |
| **Parakeet** (NVIDIA) | Open-source | Fast conformer, CTC/RNNT, near-SOTA on LibriSpeech | https://huggingface.co/nvidia/parakeet-ctc-1.1b |

---

## 2. TEXT-TO-SPEECH (TTS)

### Open-Source TTS (Run Locally)

| Model | Quality | Speed | Key Features | Link |
|-------|---------|-------|-------------|------|
| **Kokoro** | ★★★★★ | Real-time | Best open-source TTS as of 2026. 82M params, natural prosody, multi-language, Apache 2.0. ⭐ 18,000+ [?] | https://github.com/hexgrad/kokoro |
| **Piper** | ★★★★ | Ultra-fast | Lightweight, runs on Raspberry Pi, 30+ languages, designed for home assistants. MIT. ⭐ 9,000+ | https://github.com/rhasspy/piper |
| **Fish Speech** | ★★★★★ | Real-time | Zero-shot voice cloning, multilingual, 500K+ voices on Hugging Face | https://github.com/fishaudio/fish-speech |
| **XTTS v2** (Coqui) | ★★★★ | Near real-time | Zero-shot cloning from 6s of audio. 17 languages. Coqui shut down but model is open. | https://huggingface.co/coqui/XTTS-v2 |
| **Bark** (Suno) | ★★★ | Slow | Can do music, laughter, non-speech — unique. | https://github.com/suno-ai/bark |
| **MeloTTS** | ★★★★ | Fast | High-quality, multi-accent English + multilingual | https://github.com/myshell-ai/MeloTTS |
| **StyleTTS 2** | ★★★★★ | Near real-time | Human-level quality on LJSpeech benchmark | https://github.com/yl4579/StyleTTS2 |
| **Parler-TTS** | ★★★★ | Fast | Describe the voice you want in text → generates matching speech | https://github.com/huggingface/parler-tts |
| **MetaVoice** | ★★★★ | Real-time | Zero-shot cloning, emotional control | https://github.com/metavoiceio/metavoice-src |
| **F5-TTS** | ★★★★★ [?] | Fast | Flow-matching TTS, strong naturalism | https://github.com/SWivid/F5-TTS |

### Commercial TTS

| Service | Key Features | Pricing | Link |
|---------|-------------|---------|------|
| **ElevenLabs** | Best commercial quality. Voice cloning, 32 languages, real-time API, dubbing. | Free tier + $5-330/mo | https://elevenlabs.io/ |
| **Play.ht** | Ultra-realistic, 900+ voices, API | $31-99/mo | https://play.ht/ |
| **Amazon Polly** | AWS-integrated, SSML, Neural voices | Pay per character | https://aws.amazon.com/polly/ |
| **Google Cloud TTS** | WaveNet/Neural2 voices, 220+ voices | Pay per character | https://cloud.google.com/text-to-speech |
| **Azure TTS** | 400+ neural voices, custom voice training | Pay per character | https://azure.microsoft.com/services/cognitive-services/text-to-speech/ |
| **Murf AI** | Studio-quality, voice changer, sync | $19-83/mo | https://murf.ai/ |

---

## 3. VOICE CLONING & CONVERSION

| Tool | Type | Description | Link |
|------|------|-------------|------|
| **RVC (Retrieval-based Voice Conversion)** | Open-source | Real-time voice conversion, huge community. The standard for voice cloning. ⭐ 28,000+ | https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI |
| **OpenVoice** (MyShell) | Open-source | Instant voice cloning, tone/style transfer | https://github.com/myshell-ai/OpenVoice |
| **GPT-SoVITS** | Open-source | Few-shot voice cloning TTS (1 min of audio → clone) | https://github.com/RVC-Boss/GPT-SoVITS |
| **Resemble AI** | Commercial | Real-time voice cloning API, deepfake detection | https://resemble.ai/ |
| **Respeecher** | Commercial | Hollywood-grade voice conversion (used in films) | https://respeecher.com/ |

---

## 4. MUSIC GENERATION

| Tool | Type | Description | Link |
|------|------|-------------|------|
| **Suno** | Commercial | Text-to-full-song (vocals, instruments, lyrics). Dominant consumer music AI. | https://suno.com/ |
| **Udio** | Commercial | Competing with Suno, strong quality | https://udio.com/ |
| **MusicGen** (Meta) | Open-source | Text-to-music, 3.3B params, Apache 2.0 | https://github.com/facebookresearch/audiocraft |
| **AudioCraft** (Meta) | Open-source | Suite: MusicGen + AudioGen + EnCodec | https://github.com/facebookresearch/audiocraft |
| **Stable Audio** (Stability AI) | Commercial/Open | Text-to-audio/music, open weights available | https://stableaudio.com/ |
| **AIVA** | Commercial | AI music composition for media/games | https://aiva.ai/ |
| **Soundraw** | Commercial | Royalty-free AI music, customizable | https://soundraw.io/ |
| **Riffusion** | Open-source | Spectogram-based music gen (Stable Diffusion for audio) | https://github.com/riffusion/riffusion |
| **Mubert** | Commercial | Real-time generative music streaming | https://mubert.com/ |

---

## 5. AUDIO-NATIVE LLMs & VOICE-TO-VOICE

The new paradigm: models that natively process and generate audio tokens (not text→TTS pipelines).

| Model / Platform | Type | Key Feature | Link |
|-----------------|------|------------|------|
| **GPT-5.5 Voice Mode** | Commercial | Native voice conversation, sub-200ms latency, emotional awareness | https://openai.com/ |
| **Gemini Live** | Commercial | Real-time voice + video conversation with Gemini | https://gemini.google.com/ |
| **Claude Voice** | Commercial | Voice conversations in Claude apps | https://anthropic.com/ |
| **Moshi** (Kyutai) | Open-source | First open-source real-time voice-to-voice LLM. Full duplex (can talk and listen simultaneously). | https://github.com/kyutai-labs/moshi |
| **Ultravox** (Fixie AI) | Open-source | Audio-native LLM that directly processes speech tokens | https://github.com/fixie-ai/ultravox |
| **Qwen2-Audio** | Open-source | Native audio understanding in Qwen family | https://github.com/QwenLM/Qwen2-Audio |
| **Hume AI** | Commercial | Emotionally intelligent voice AI, measures tone/sentiment | https://hume.ai/ |

---

## 6. SOUND EFFECTS & AUDIO TOOLS

| Tool | Description | Link |
|------|-------------|------|
| **ElevenLabs Sound Effects** | Text-to-SFX generation | https://elevenlabs.io/sound-effects |
| **AudioGen** (Meta) | Text-to-general-audio (not music) | https://github.com/facebookresearch/audiocraft |
| **Demucs** (Meta) | Music source separation (vocals/drums/bass/other) | https://github.com/facebookresearch/demucs |
| **AudioSeal** (Meta) | Watermarking AI-generated audio | https://github.com/facebookresearch/audioseal |
| **Descript** | AI-powered audio/video editor with transcript editing | https://descript.com/ |
| **Adobe Podcast** | AI noise removal, room echo fix | https://podcast.adobe.com/ |

---

## 7. REAL-TIME / LOW-LATENCY VOICE INFRA

For building voice agents and conversational AI:

| Tool | Description | Link |
|------|-------------|------|
| **LiveKit** | Open-source WebRTC infra for real-time voice AI agents | https://github.com/livekit/livekit |
| **Vapi** | Voice AI platform — build phone/web voice agents | https://vapi.ai/ |
| **Bland AI** | AI phone calling agent platform | https://bland.ai/ |
| **Retell AI** | Build voice AI agents with <800ms latency | https://retellai.com/ |
| **Vocode** | Open-source voice agent framework | https://github.com/vocodedev/vocode-python |
| **Pipecat** (Daily) | Open-source framework for voice/multimodal AI agents | https://github.com/pipecat-ai/pipecat |

---

*Last updated: June 2026. [?] = unverified.*
