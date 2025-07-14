def record_audio(file_path, duration=None):
    try:
        if duration:
            print(f"🎙️ Запись в течение {duration} секунд...")
            recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS)
            sd.wait()
        else:
            print("🎙️ Запись... Нажмите Ctrl+C для остановки.")
            recording = []
            while True:
                data = sd.rec(int(SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS)
                sd.wait()
                recording.append(data)
    except KeyboardInterrupt:
        print("⛔ Запись остановлена пользователем.")
        if not recording:
            print("⚠️ Запись пустая. Файл не будет сохранён.")
            return
        if isinstance(recording, list):
            recording = np.concatenate(recording, axis=0)

    # Проверка и преобразование формы массива
    if recording is None or len(recording) == 0:
        print("⚠️ Пустая запись. Пропускаем сохранение.")
        return

    if recording.ndim == 1:
        recording = recording.reshape(-1, 1)

    sf.write(file_path, recording, SAMPLE_RATE)
    print(f"✅ Файл сохранён: {file_path}")
