import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import openai
import config
import re
import threading
import pyautogui
import random
from PIL import ImageGrab
import subprocess


# instanciando Configuración del reconocimiento de voz
r = sr.Recognizer()

# instanciando libreria del habla de voz
engine = pyttsx3.init()

# configuracion voz
voices = engine.getProperty('voices')
velocidadDeVoz = 130
engine.setProperty('voice', voices[2].id)
#engine.setProperty('rate',velocidadDeVoz, voices[2].id)


#-----------------------------------------------------------------------------------------------------
#validar palabra clave
def escuchar_palabra_activacion():
    try:
        print("DI Rubí para activarme....")
        texto = escuchar_comando()

        if 'rubí' in texto or 'loca' in texto or 'rubi' in texto or 'Rubí' in texto or 'ruby' in texto or 'Rubi' in texto or 'Rúbi' in texto:
            return True
        if 'ok' in texto or 'okey' in texto or 'esta bien' in texto or 'hola' in texto or 'que lo que' in texto:
            return True
        else:
            return False
    except sr.UnknownValueError:
        return False


#---------------------------------------------------------------------------------------------------------
#Escuchar
def escuchar_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # Reducir la duración para ajustar el umbral de ruido
        r.energy_threshold = 300  # Reducir el umbral de energía para capturar comandos más silenciosos
        r.dynamic_energy_threshold = False

        print("Te escucho....")

        try:
            # Escuchar durante 5 segundos (puedes ajustar el valor según tus necesidades)
            #audio = r.listen(source, timeout=5, phrase_time_limit=5)
            audio = r.listen(source,timeout=100,phrase_time_limit=10)

            texto = r.recognize_google(audio, language='es-ES')
            print("Comando detectado: " + texto)
            return texto.lower()
        except sr.UnknownValueError:
            print("No se pudo reconocer el comando.")
            return ""
        except sr.RequestError as e:
            print("Error en la solicitud a Google Speech Recognition: {0}".format(e))
            return ""


#----------------------------------------------------------------------------------------------------------
#hablar
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()


#----------------------------------------------------------------------------------------------------------
#reproducir en youtube
def rep_music_on_yt(comando):
    if 'wesley' in comando or 'eiezer' in comando or 'wagner' in comando:
        cancion = "cancion gay"
        hablar("Reproduciendo cancion de wesley, eliezer y gu agner")
        pywhatkit.playonyt(cancion)

    else:
        cancion = comando.replace('reproduce', '')
        hablar("Reproduciendo " + cancion)
        pywhatkit.playonyt(cancion)


#-----------------------------------------------------------------------------------------------------------
#buscar en google
def search_google(content):
    #comando = escuchar_comando()
    #hablar("Mi banco de datos solo lleva a septiembre del 2021, pero ¿si quieres te llevo a google?")
    #if comando == 'si' or comando == 'esta bien' or comando == 'ok':
        try:
            if content == "":
                vacio = "vacio"
                return vacio
            else:
                pywhatkit.search(content)
                hablar("Viendo... "+content)
        except:
            hablar("Error de red")
    #else:
        #hablar('ok')


#----------------------------------------------------------------------------------------------------------
#Bucar en Chatgpt
def chatgpt(content):
    openai.api_key = config.api_key
    messages = [{"role": "system",
                "content": "eres un asistente personal, que resuelve dudas, busca soluciones, asiste en cualquier oficio, se encarga de explicar de forma concreta, corta y con ejemplos, tu das respuestas cortas,/"
                "Rusbel Rodriguez Paulino es tu padre tu creador es Rusbel, tu te llamas Rubí"}]

    messages.append({"role": "user", "content": content})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    respuesta_content = respuesta.choices[0].message.content
    messages.append({"role": "assistant", "content": respuesta_content})


    if 'Lo siento,' in respuesta_content or 'No puedo responder esa pregunta' in respuesta_content:
        search_google(content)

    else: hablar(respuesta_content)


#----------------------------------------------------------------------------------------------------------
#captura de pantalla
def captura():
    hablar("Capturando pantalla...")
    captura_pantalla = ImageGrab.grab()
    ruta_guardado = config.ubicacion+"/captura_pantalla.png"
    diferenciador = 1

    while True:
        try:
            if os.path.exists(ruta_guardado):
                diferenciador += 1
                ruta_guardado = f"{config.ubicacion}/captura_pantalla{diferenciador}.png"
            else:
                captura_pantalla.save(ruta_guardado)
                captura_pantalla.show()
                break
        except:
            hablar("Error de red")


#--------------------------------------------------------------------------------------------------------------
#abrir programas de mi pc

#este recibe la direccion del programa que se debe abrir
def abrir_programa(nombre_programa):
    try:
        # Intenta abrir el programa usando el comando del sistema operativo adecuado
        subprocess.Popen(nombre_programa)
        print(f"El programa '{nombre_programa}' se ha abierto correctamente.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el programa '{nombre_programa}'.")
    except Exception as e:
        print(f"Error al abrir el programa: {e}")


#ubica si el texto para ver si tiene palabra o programa clave
def palabras_coincidentes(cadena):

    #para agregar un programa primero inserta sus palabras claves en este array redondea a su alrededor
    programas = ["valorant", "valora", "valoran", "valor",
                "bloc", "notas", "libreta", "nota", "blog"]

    palabras_cadena = cadena.split()
    try:
        for palabra in palabras_cadena:
            if palabra in programas:
                distribuidor_de_funciones(palabra.lower())

        #print('No se encontro palabra clave para abrir algun programa')
    except:
        print('error al obtener palabra clave')


#ubica el metodo para abrir el programa que es
def distribuidor_de_funciones(palabra):
    if palabra == 'valorant' or palabra == 'valora' or palabra == 'valoran' or palabra == 'valor':
        print('ejecutandose valorant')
        abrir_programa('"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live')

    elif palabra == 'bloc' or palabra == 'blog' or palabra == 'notas' or palabra == 'libreta':
        print('ejecutandose un bloc de notas')
        abrir_programa('notepad.exe')

    #pala agregar otro programa se pone aqui su identificador para que se ejecute el
    #busca en la lupita de la barra de tareas el programa click derecho abre su ubicacion
    #arriba de el click derecho propiedades y ahi copia su ubicacion luego prueba si abre con esa o ve cortandola
    #pero antes debes poner sus coincidentes arriba para que mande esa palabra para acá

    else:
        print('No se encontró metodo para el programa: '+ palabra)


#-----------------------------------------------------------------------------------------------------------
#Calculadora

#Limpiar letras de un string esto es para  calcular solo deja los signos y los numeros
def eliminar_caracteres_no_numericos_y_operadores(cadena):

    # Definimos una expresión regular que buscará todos los caracteres que no sean números o signos de operación (+, -, *, /).
    patron = r'[^0-9+\-*/]'
    # Utilizamos la función sub de re para reemplazar todos los caracteres que coincidan con la expresión regular por una cadena vacía.
    cadena_limpia = re.sub(patron, '', cadena)
    return cadena_limpia

#calcular
def calcular(cadena):
    operacion = eliminar_caracteres_no_numericos_y_operadores(cadena)
    result = eval(operacion)

    return result


