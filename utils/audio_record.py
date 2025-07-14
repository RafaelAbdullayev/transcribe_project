def record_audio(duration=5):
    try:
        print("🎙️ Запись началась...")
        recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS)
        sd.wait()
        if recording.ndim == 1:  # иногда так бывает на некоторых системах
            recording = recording.reshape(-1, 1)
        sf.write(AUDIO_FILE, recording, SAMPLE_RATE)
        print(f"✅ Запись завершена и сохранена в {AUDIO_FILE}")
    except KeyboardInterrupt:
        print("⛔ Запись прервана пользователем (Ctrl+C)")
