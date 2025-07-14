import argparse
import os
import datetime
import sounddevice as sd
import soundfile as sf
import whisper
import librosa

# Папка для вывода и настройки
OUTPUT_DIR = "output"
AUDIO_FILENAME = "recorded_audio.wav"
SAMPLE_RATE = 16000
CHANNELS = 1

# Создаём папку для результатов, если её нет
os.makedirs(OUTPUT_DIR, exist_ok=True)

def record_audio(file_path, duration=None):
    print("Началась запись... (Ctrl+C — чтобы остановить)")
    try:
        if duration:
            recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS)
            sd.wait()
        else:
            print("Запись без указания длительности — жмите Ctrl+C, когда хватит.")
            frames = []
            with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS,
                                callback=lambda indata, frames, time, status: frames.append(indata.copy())):
                while True:
                    pass
            recording = b''.join(frames)
        sf.write(file_path, recording, SAMPLE_RATE)
        print(f"Аудио сохранено в: {file_path}")
    except KeyboardInterrupt:
        print("\nЗапись остановлена пользователем.")
        try:
            sf.write(file_path, recording, SAMPLE_RATE)
            print(f"Аудио сохранено в: {file_path}")
        except Exception as e:
            print("Ошибка при сохранении:", e)
    except Exception as e:
        print("Ошибка при записи:", e)

def transcribe_audio(audio_file):
    print(f"\nНачинаем расшифровку: {audio_file}")
    try:
        model = whisper.load_model("base")
        audio_data, _ = librosa.load(audio_file, sr=SAMPLE_RATE)
        result = model.transcribe(audio_data)
        text = result.get("text", "").strip()
        if text:
            print("\nРасшифровка текста:\n")
            print(text)
        else:
            print("Не удалось получить текст.")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_file = os.path.join(OUTPUT_DIR, f"transcript_{timestamp}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text if text else "Текст не распознан.")
        print(f"\nРезультат сохранён: {output_file}")
    except Exception as e:
        print("Ошибка при расшифровке:", e)

if __name__ == "__main__":
    print("Скрипт для записи и расшифровки речи (Whisper)")
    print("   Запуск: --mode mic [--duration 60] или --mode file --input path_to_audio.wav\n")

    parser = argparse.ArgumentParser(description="Запись и расшифровка речи")
    parser.add_argument("--mode", choices=["mic", "file"], required=True, help="Режим: mic — запись, file — файл")
    parser.add_argument("--input", help="Путь к аудиофайлу (для режима file)")
    parser.add_argument("--duration", type=int, help="Длительность записи в секундах (для режима mic)")
    args = parser.parse_args()

    audio_path = os.path.join(OUTPUT_DIR, AUDIO_FILENAME)

    if args.mode == "mic":
        record_audio(audio_path, duration=args.duration)
        transcribe_audio(audio_path)
    elif args.mode == "file":
        if not args.input or not os.path.isfile(args.input):
            print("Укажите корректный путь к файлу через --input")
        else:
            transcribe_audio(args.input)
