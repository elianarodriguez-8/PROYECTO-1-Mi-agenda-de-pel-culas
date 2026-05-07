"""
Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    pelicula = {}
    pelicula["nombre"] = nombre
    pelicula["genero"] = genero
    pelicula["duracion"] = duracion
    pelicula["anio"] = anio
    pelicula["clasificacion"] = clasificacion
    pelicula["hora"] = hora
    pelicula["dia"] = dia
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    nombre = nombre_pelicula.strip().lower()
    for peli in [p1, p2, p3, p4, p5]:
        if peli["nombre"].lower() == nombre:
            return peli
    return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    bd = [p1, p2, p3, p4, p5]
    pelicula_mas_larga = bd[0]

    for pelicula in bd:
        if pelicula["duracion"] > pelicula_mas_larga["duracion"]:
            pelicula_mas_larga = pelicula

    return pelicula_mas_larga
 
def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    total = (p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"])
    
    promedio = total // 5  
    
    horas = promedio // 60
    minutos = promedio % 60
    
    return str(horas).zfill(2) + ":" + str(minutos).zfill(2)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    resultado = ""

    if p1["anio"] > anio:
        resultado += p1["nombre"] + ", "
    if p2["anio"] > anio:
        resultado += p2["nombre"] + ", "
    if p3["anio"] > anio:
        resultado += p3["nombre"] + ", "
    if p4["anio"] > anio:
        resultado += p4["nombre"] + ", "
    if p5["anio"] > anio:
        resultado += p5["nombre"] + ", "

    if resultado == "":
        return "Ninguna"
    
    return resultado[:-2] 

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    contador = 0
    
    if p1["clasificacion"].strip() == "18+":
        contador += 1
    if p2["clasificacion"].strip() == "18+":
        contador += 1
    if p3["clasificacion"].strip() == "18+":
        contador += 1
    if p4["clasificacion"].strip() == "18+":
        contador += 1
    if p5["clasificacion"].strip() == "18+":
        contador += 1
    
    return contador

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    if nueva_hora < 0 or nueva_hora > 2359:
        return False
    
    if nueva_hora % 100 >= 60:
        return False
    peliculas = [p1, p2, p3, p4, p5]

    duracion = peli["duracion"]

    nueva_inicio = (nueva_hora // 100) * 60 + (nueva_hora % 100)
    nueva_fin = nueva_inicio + duracion

    for p in peliculas:
        if p != peli and p["dia"].lower() == nuevo_dia.lower():

            inicio = (p["hora"] // 100) * 60 + (p["hora"] % 100)
            fin = inicio + p["duracion"]

            if not (nueva_fin <= inicio or nueva_inicio >= fin):
                return False
    dias_validos = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

    if nuevo_dia.lower() not in dias_validos:
        return False
    if control_horario:

        genero = peli["genero"].lower()

        if "documental" in genero and nueva_hora >= 2200:
            return False

        if "drama" in genero and nuevo_dia.lower() == "viernes":
            return False
        dias_semana = ["lunes","martes","miercoles","jueves","viernes"]

        if nuevo_dia.lower() in dias_semana:
            if nueva_hora >= 2300 or nueva_hora < 600:
                return False

    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia

    return True
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    genero = peli["genero"].lower()
    clasificacion = peli["clasificacion"]

    if edad_invitado >= 18:
        return True
    
    if "documental" in genero:
        return True

    if edad_invitado <= 10:
        if "familiar" in genero:
            return True
        else:
            return False

    if edad_invitado < 15:
        if "terror" in genero:
            return False

    if clasificacion == "18+" and edad_invitado < 18:
        return autorizacion_padres
    if clasificacion == "16+" and edad_invitado < 16:
        return autorizacion_padres
    if clasificacion == "13+" and edad_invitado < 13:
        return autorizacion_padres
    if clasificacion == "7+" and edad_invitado < 7:
        return autorizacion_padres
    
def duracion_promedio_8_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict) -> str:
    total = (p1["duracion"] + p2["duracion"] + p3["duracion"] +  p4["duracion"] + p5["duracion"] + p6["duracion"] + p7["duracion"] + p8["duracion"])

    promedio = total // 8
    horas = promedio // 60
    minutos = promedio % 60

    return str(horas).zfill(2) + ":" + str(minutos).zfill(2)

    return True










