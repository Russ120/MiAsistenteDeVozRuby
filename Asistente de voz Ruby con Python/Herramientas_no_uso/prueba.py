import speech_recognition as sr
import threading


def reconocer_audio(audio):
    # Crear un reconocedor de voz
    r = sr.Recognizer()

    try:
        # Realizar el reconocimiento de voz
        texto = r.recognize_google(audio, language='es-ES')
        print("Comando detectado: " + texto)
        return texto.lower()
    except sr.UnknownValueError:
        return ""


def escuchar_comando():
    # Crear un reconocedor de voz
    r = sr.Recognizer()

    # Ajustar la configuración para un mejor reconocimiento
    with sr.Microphone() as source:
        print("Te escucho....")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.energy_threshold = 300  # Reducir el umbral de energía para detectar sonidos más suaves

    # Comenzar el reconocimiento en un hilo separado
    escucha_thread = threading.Thread(target=realizar_reconocimiento, args=(r,))


    escucha_thread.start()


def realizar_reconocimiento(recognizer):
    with sr.Microphone() as source:
        audio = recognizer.listen(source, timeout=5)

    texto = reconocer_audio(audio)

    return texto


# Ejemplo de uso:
comando = escuchar_comando()
print("Texto reconocido:", comando)






#def escuchar_comando():

    #with sr.Microphone() as source:
        #print("Te escucho....")

        #r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 1000
        #r.dynamic_energy_threshold = False

        #audio = r.listen(source)
    #try:
        #texto = r.recognize_google(audio, language='es-ES')
        #print("comando detectado..." + texto)
        #return texto.lower()
    #except sr.UnknownValueError:
        #return ""












def reconocer_audio(audio):
    # Crear un reconocedor de voz
    r = sr.Recognizer()

    try:
        # Realizar el reconocimiento de voz
        texto = r.recognize_google(audio, language='es-ES')
        print("Comando detectado: " + texto)
        return texto.lower()
    except sr.UnknownValueError:
        return ""


def escuchar_comando():
    # Crear un reconocedor de voz
    r = sr.Recognizer()

    # Ajustar la configuración para un mejor reconocimiento
    with sr.Microphone() as source:
        print("Te escucho....")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.energy_threshold = 300  # Reducir el umbral de energía para detectar sonidos más suaves

    # Comenzar el reconocimiento en un hilo separado
    escucha_thread = threading.Thread(target=realizar_reconocimiento, args=(r,))
    escucha_thread.start()


def realizar_reconocimiento(recognizer):
    with sr.Microphone() as source:
        audio = recognizer.listen(source, timeout=5)

    texto = reconocer_audio(audio)
    return texto











def depuracion(content):
    if content != "":
        split_message = content.split()
        content = '+'.join(split_message)
        print(content)
        return content
    else:
        return content