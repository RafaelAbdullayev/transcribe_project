
Transcribe Project - Распознавание речи с микрофона или аудиофайла
==================================================================

Описание:
----------
Простой CLI-инструмент для записи звука с микрофона и последующей расшифровки (транскрибации) речи с помощью модели Whisper от OpenAI. Также поддерживается транскрибация готового аудиофайла.

Структура проекта:
-------------------
transcribe_project/
│
├── transcribe.py        - Главный исполняемый скрипт
├── output/              - Папка для сохранения аудио и текста
│   ├── recorded_audio.wav
│   └── transcript_YYYYMMDD_HHMM.txt
└── README.txt           - Инструкция

Установка:
-----------
1. Установи зависимости:
   pip install -r requirements.txt

   (Если файла requirements.txt нет — установи вручную:
   pip install openai-whisper sounddevice soundfile librosa)

2. Убедись, что установлен ffmpeg.

Использование:
---------------
1. Запись с микрофона и транскрибация:
   python transcribe.py --mode mic --duration 60

   (где --duration — длительность записи в секундах)

2. Транскрибация из аудиофайла:
   python transcribe.py --mode file --input путь_к_файлу.wav

Результат:
-----------
- Аудио сохраняется в папке output/ как recorded_audio.wav
- Расшифровка сохраняется как transcript_YYYYMMDD_HHMM.txt

Автор:
-------
Абдуллаев Рафаэль



Запуск программ

Открой командную строку или терминал.

Перейди в папку с проектом (если ты еще этого не сделал).

Пример: cd C:\transcribe_project

Запусти скрипт с нужными аргументами:

Для записи с микрофона (например, 600 секунд  (10 минут) ): >>   python transcribe.py --mode mic --duration 600

Для записи с микрофона (например, 15 секунд):  >>   python transcribe.py --mode mic --duration 15

Обработка готового аудиофайла:  >>>   python transcribe.py --mode file --input path/to/audio.wav



И.Т.Д


Требования

Python 3.8+
Виртуальное окружение (рекомендуется)
Установленные библиотеки:

bash
pip install sounddevice soundfile librosa openai-whisper

