import re
import random
import acciones as ac

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response

def message_probability(user_message, palabras_reconocidas, respuesta_unica=False, palabra_requerida=[]):
    mensaje_certeza=0
    has_required_words=True

    for word in user_message:
        if word in palabras_reconocidas:
            mensaje_certeza+=1

    percentage = float(mensaje_certeza) / float(len(palabras_reconocidas))

#----------------------------------------------------------------- no jodere con eso por ahora
    for word in palabra_requerida:
        if word not in user_message:
            has_required_words=False
            break
    if has_required_words or respuesta_unica:
        return int(percentage * 100)
    else:
        return 0
#----------------------------------------------------------------------------------------------



def check_all_message(message):
    highest_prob={}

    def response(ejecutar_metodo, lista_de_palabras, respuesta_unica = False, palabra_requerida=[]):
        nonlocal highest_prob

        highest_prob[ejecutar_metodo] = message_probability(message, lista_de_palabras, respuesta_unica, palabra_requerida)

    response(hola(),['hola','klk','saludos','buenas','dime a ver','que onda','heo','que tal','hey'], respuesta_unica = True)

    response(estas(),['encuentras','te','va','estás','como','sientes','estas','cómo'],respuesta_unica = True)

    response('apagar()',['apagar','apaga','te', 'detener','apagarse','dormir', 'parar', 'cesar', 'finalizar', 'cancelar', 'desactivar', 'desconectar',
                        'cerrar', 'terminar'],respuesta_unica = True)

    response(ac.chatgpt(message),['puede','llegar','alguien','a','la','podría','poder',],respuesta_unica = True)



    #response('Estoy bien y tu?',['como','estas','va','encuentras','sientes'],palabra_requerida=['como'])
    #response('me la suda la verdad, ese tigueronsillo es mi hijo en valorant', ['gente','no anda', 'importa', 'te vale'],palabra_requerida=['gente'])


    best_match = max(highest_prob,key=highest_prob.get)


    return desconocido() if highest_prob[best_match] < 1 else best_match



def desconocido():


    response=['Puedes decirlo de nuevo', 'no entendi ni verga', 'no estoy seguro de lo que quieres', 'buscalo en google a ver que tal'][random.randrange(4)]
    return response




def hola():
    return 'hola'



def estas():

    return 'estoy bien'