# Our main file.

import speech_recognition as sr

# Cria um reconhecedor de voz
r = sr.Recognizer()

# Abrir o microfone para captura de áudio
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Definir o microfone como fonte de áudio

        print(r.recognize_google(audio, language='pt'))