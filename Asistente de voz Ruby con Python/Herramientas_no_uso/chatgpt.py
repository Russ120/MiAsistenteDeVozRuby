import openai
import config

# aqui se iguala la key de la libreria a la key mia que esta en otra carpeta la config
openai.api_key = config.api_key

# contexto del asistente    ojo se inicializa con este contexto pero se cambia por otro mas abajo
messages = [{"role": "system",
             "content": "eres un asistente personal, que resuelve dudas, busca soluciones, asiste en cualquier oficio, se encarga de explicar de forma concreta y con ejemplos"}]

while True:

    # pregunta al asistente
    content = input("¿Sobre que quieres hablar? ")

    # esto es para que se detenga
    if content == "exit":
        break

    # aqui se inicializa de nuevo y se le añade otra consulta esto es para contextualizar de nuevo con la pregunta hecha
    # esto es una contextualizacion de lo que se ha hablado y eso se le pasa a lo de abajo para que la respuesta este acertada
    messages.append({"role": "user", "content": content})

    # esta es la respuesta del asistente, aqui se le manda la pregunta se le ubica el modelo de openai y en mensajes se le pasa messages que dice
    # quien le pregunta y se le manda en content la pregunta, esto devolverá la respuesta
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                             messages=messages)

    # guarda la respuesta, busca en respuesta, chices[0] osea la respuesta con indice 0 la primera,
    # se busca dentro de esa respuesta el mensaje y dentro del mensaje se solicita solo el contenido y todo eso se guarda en respuesta_content
    respuesta_content = respuesta.choices[0].message.content

    # contexto
    # esto para que se quede con la repespuesta anterior que me dio y tenga un contexto de lo que ya me ha dicho
    # el rol cambia y es assistant ya que el mismo fue que lo dio y el content cambia a la respuesta que el me dio despues de ser depurada claro
    messages.append({"role": "assistant", "content": respuesta_content})

    # Imprime la respuesta
    print(respuesta_content)