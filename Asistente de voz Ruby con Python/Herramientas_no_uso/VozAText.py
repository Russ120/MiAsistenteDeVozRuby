import random
import re

# Libreria para reconocer lo que hablo
import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = False
        r.adjust_for_ambient_noise(source)

        print("Di algo: ")

        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        text = text.lower()

        if 'como estas' in text or 'como te sientes hoy' in text or 'como andas' in text:
            response = \
                ['Estoy bien y lista para ayudar', 'hace mucha calor, pero aqui estamos',
                 'De maravilla en que puedo servirte',
                 'estoy bien un poco inexistente, pero en que puedo ayudarte'][random.randrange(4)]
            print('hola')
            print(response)

        if 'cerrar' in text:
            break



        if 'calcula' in text or 'calcular' in text:



            def eliminar_caracteres_no_numericos_y_operadores(cadena):
                # Definimos una expresión regular que buscará todos los caracteres que no sean números o signos de operación (+, -, *, /).
                patron = r'[^0-9+\-*/]'
                # Utilizamos la función sub de re para reemplazar todos los caracteres que coincidan con la expresión regular por una cadena vacía.
                cadena_limpia = re.sub(patron, '', cadena)
                return cadena_limpia

                print(text)
                result = eval(text)
                print(result)




            # Ejemplo de uso:
            cadena_original = "12a3+b4-5/c6"
            cadena_limpia = eliminar_caracteres_no_numericos_y_operadores(cadena_original)
            print(cadena_limpia)  # Salida: "123+4-5/6"




        print("Has dicho: " + text)
    except:
        print("Lo siento, no te he entendido")


