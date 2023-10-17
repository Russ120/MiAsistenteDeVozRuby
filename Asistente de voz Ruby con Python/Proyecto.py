import random
import datetime
import acciones as ac

activado = False

while True:

    if not activado:
        if ac.escuchar_palabra_activacion():
            ac.hablar("Sí, ¿en qué puedo ayudarte?")
            activado = True




    else:
        comando = ac.escuchar_comando()
        if comando == "":#-------------------------------------------------
            ac.hablar("jiji")




        elif 'apagar' in comando or 'apagarse' in comando or 'dormir' in comando or 'apaga' in comando:#-------------
            ac.hablar("hasta pronto,   Apagado.....")
            break



        elif 'reproduce' in comando or 'reproducir' in comando:#-------------------------------------------------

            while comando == 'reproduce' or comando == 'reproducir':
                ac.hablar("te escucho")
                comando = ac.escuchar_comando()
            ac.rep_music_on_yt(comando)



        elif 'hora' in comando:#-------------------------------------------------
            horas = datetime.datetime.now().strftime('%H')
            minutos = datetime.datetime.now().strftime('%M')
            ac.hablar("Son las: " + horas + 'con ' + minutos + ' minutos')



        elif 'consulta' in comando:#-------------------------------------------------
            while True:
                ac.hablar("¿sii?")
                content = ac.escuchar_comando()
                content = content.lower()


                while content == 'consulta' or content =='consulta consulta' or content =='consulta consulta consulta':
                    ac.hablar("te escucho")
                    content = ac.escuchar_comando()

                if 'ya' in content or 'esta bien' in content or 'basta' in content or 'gracias' in content or 'eso es todo' in content or 'ok' in content or 'apagar' in content:
                    ac.hablar("fue un gusto")
                    break

                else:
                    busqueda = ac.chatgpt(content)
                    # busqueda = ac.search_google(content)
                    if busqueda == "vacio":
                        ac.hablar("pregunta de nuevo")



        elif 'cómo estás' in comando or 'cómo te sientes' in comando or 'cómo andas' in comando or 'cómo está' in comando :
            response = \
                ['Estoy bien y lista para ayudar', 'hace mucha calor, pero aqui estamos',
                'De maravilla, en que puedo servirte?',
                'estoy bien, un poco inexistente, pero en que puedo ayudarte'][random.randrange(4)]
            print(response)
            ac.hablar(response)



        elif 'pantalla' in comando or 'captura' in comando or 'screenshot' in comando or 'captúrame' in comando:
            ac.captura()


        elif 'crea' in comando or 'crear' in comando or 'abre' in comando or 'abrir' in comando or 'ábrelos' in comando \
                or 'abras' in comando:
            ac.palabras_coincidentes(comando)
            ac.hablar('okey')


        elif 'calcula' in comando or 'calcular' in comando or 'calcules' in comando or 'calculé' in comando or 'calcúlame' in comando:
            ac.hablar(ac.calcular(comando))

        else:
            ac.hablar("No entendi tu comando.")