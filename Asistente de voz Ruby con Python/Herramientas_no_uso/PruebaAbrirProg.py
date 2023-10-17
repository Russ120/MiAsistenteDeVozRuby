import subprocess

def abrir_programa(nombre_programa):
    try:
        # Intenta abrir el programa usando el comando del sistema operativo adecuado
        subprocess.Popen(nombre_programa)
        print(f"El programa '{nombre_programa}' se ha abierto correctamente.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el programa '{nombre_programa}'.")
    except Exception as e:
        print(f"Error al abrir el programa: {e}")





def palabras_coincidentes(cadena):

    #para agregar un programa primero inserta sus palabras claves en este array redondea a su alrededor
    programas = ["valorant", "valora", "valoran", "valor",
                 "bloc", "notas", "libreta", "nota", "blog"]

    palabras_cadena = cadena.split()
    try:
        for palabra in palabras_cadena:
            if palabra in programas:
                distribuidor_de_funciones(palabra.lower())
                break
        #print('No se encontro palabra clave para abrir algun programa')
    except:
        print('error al obtener palabra clave')




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



# Ejemplo de uso
content = "Crea, abre es un Valoront de blog dE texto con algunas palabras.".lower()

if 'crea' in content or 'crear' in content or 'abre' in content or 'abrir' in content:
    palabras_coincidentes(content)
