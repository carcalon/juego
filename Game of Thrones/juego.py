##Game of Thrones


def info():
    """
    Este es un procedimiento que consiste en sacar por pantalla la información inicial del juego.
    :return: None
    """
    import textwrap
    intro = 'Cargando el juego...\n' \
            'Perteneces a la Guardia de la Noche.\n'\
            'Llevas semanas andando al otro lado del muro,\n'\
            'en una expedición para detectar posibles salvajes...\n' \
            'Tienes varias opciones para llegar a un poblado en el que a lo mejor' \
            'puedes descansar durante esta noche.' \
            'Debes pensar qué ruta escoger para llegar al poblado.'
    print(textwrap.fill(intro))

def random_ruta():
    import random
    escenarios = ('bosque', 'camino del rey', 'tundra')
    eleccion = list(random.sample(population=escenarios, k=2))
    return eleccion

def pedir_ruta():
    ruta = -1
    eleccion = random_ruta()
    valor_valido = 'Necesito un valor que esté en la lista de posibles rutas.'
    while ruta not in eleccion:
        ruta = input('Elige entre las siguientes rutas: ' + str(eleccion)).lower()
        if ruta not in eleccion:
            print(valor_valido)
    return ruta

def elige_ruta(pedir_ruta):
    import random
    if pedir_ruta == 'tundra':
        msj_tundra()
        print('\n')
        lanzar = 0
        cuadrantes = (1, 2, 3, 4)
        punto = random.choice(cuadrantes)
        try:
            while punto != lanzar:
                lanzar = int(input('Escribe un número entre el 1 y el 4 (inclusive) para dirigir la lanza.'))
                if punto == lanzar:
                    print('Has dado con el salvaje!'
                          'Sigue caminando y llegarás al poblado...')
                elif punto != lanzar:
                    print('No has dado con el salvaje!'
                          'Puedes volver a intentarlo.')
        except ValueError:
            msj_error_numeros()
    elif pedir_ruta == 'bosque':
         msj_niños()
    elif pedir_ruta == 'camino del rey':
         msj_rey()

def obtener_mas_vida(pedir_ruta):
    salud = {'guardian': 50}
    if pedir_ruta == 'bosque':
        salud['guardian'] += 5
        print('Has conseguido 5 puntos de vida!')
    elif pedir_ruta == 'camino del rey':
        print('Has conseguido 2 puntos de vida!')
        salud['guardian'] += 3
    return salud

def info_2():
    import textwrap
    intro = "\n" \
            "Has conseguido llegar al poblado!\n" \
            "Éste tiene 5 cabañas.\n" \
            "Debes elegir en qué cabaña entrarás.\n" \
            "Si está vacía podrás descansar... pero" \
            "corres el riesgo de encontrarte con un salvaje y morir..."
    print(textwrap.fill(intro))

def ocupantes():
    """
    Esta función sirve para asignar a las cabañas el tipo de ocupantes que tienen.
    :return:
    """
    import random
    tipo = ('amigo', 'enemigo', 'vacio')
    cabanas = []
    elegido = random.choices(population=tipo, k=5)
    cabanas.append(elegido)
    print(cabanas[0])
    return cabanas[0]

def pedir_numero():
    rango = [1, 2, 3, 4, 5]
    pregunta = 0
    mensaje_error = 'Necesito un valor tipo integer entre 1 y 5 (ambos inclusive)'
    while pregunta not in rango:
        try:
            pregunta = int(input('Elige de 1 a 5 en qué cabaña quieres entrar'))
            if pregunta not in rango:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
    return pregunta

def entrada_cabaña():
    poblado = ocupantes()
    pregunta = pedir_numero()
    pelea = poblado[pregunta - 1]
    if pelea == 'enemigo':
        msj_enemigo()
    else:
        msj_has_ganado()
    return pelea

def enemigo(salud):
    entrar = entrada_cabaña()
    if entrar == 'enemigo':
        lucha_o = lucha()
        vidas(salud, lucha_o)

def lucha():
    quieres_luchar = -1
    si_no = ['si', 'no']
    while quieres_luchar not in si_no:
        quieres_luchar = input('¿Quieres luchar? (si/no)').lower()
        if quieres_luchar == si_no[0]:
            print('\n')
            print('Genial! Comenzamos...')
            print('\n')
        elif quieres_luchar == si_no[1]:
            msj_desertor()
        elif quieres_luchar not in si_no:
            msj_error()
    return quieres_luchar

def vidas(salud, lucha):
    if lucha == 'si':
        salud['caminante'] = 40
        prob_golpear = (0.4, 0.6)
        quien = ('guardian', 'caminante')
        fuerza = tuple(range(10, 16))
        ataque = 'si'
        while (list(salud.values())[0] > 0) and (list(salud.values())[1] > 0) and (ataque == 'si'):
            salud = cuerpo_vidas(salud, prob_golpear, quien, fuerza)
            if (list(salud.values())[0] <= 0) or (list(salud.values())[1] <= 0):
                ataque = 'no'
            else:
                ataque = atacar()

def cuerpo_vidas(salud, prob_golpear, quien, fuerza):
    import random
    fuerza_golpe = random.choice(fuerza)
    a_quien_golpear = random.choices(population=quien, weights=prob_golpear, k=1)[0]
    salud[a_quien_golpear] = salud[a_quien_golpear] - fuerza_golpe
    msj_vidas(salud, a_quien_golpear, fuerza_golpe)
    return salud

def msj_vidas(salud, a_quien_golpear, fuerza_golpe):
    if (list(salud.values())[0] <= 0) or (list(salud.values())[1] <= 0):
        print('El ' + a_quien_golpear + ' ha muerto!\nFin de la partida')
    elif (list(salud.values())[0] > 0) or (list(salud.values())[1] > 0):
        print('El ' + a_quien_golpear + ' ha sido golpeado, restándole ' + str(fuerza_golpe) + ' puntos de vida.' +
              '\nEl estado de la salud es: ' + str(salud))

def atacar():
    ataque = -1
    si_no = ('si', 'no')
    while ataque not in si_no:
        ataque = input('¿Quieres atacar de nuevo? (si/no)').lower()
        if ataque not in si_no:
            print('\n')
            msj_error()
        elif ataque == si_no[0]:
            print('Adelante!\n')
        elif ataque == si_no[1]:
            msj_desertor()
    return ataque

def msj_has_muerto():
    print('Has muerto!\nTe has encontrado con un enemigo!')

def msj_enemigo():
    print('En esta cabaña hay un enemigo!')

def msj_has_ganado():
    print('Bien! En esta cabaña puedes descansar')

def msj_error():
    print('Necesito un valor si/no.\nPor favor, introduce un valor válido.')

def msj_error_numeros():
    print('Necesito un valor entre 1 y 4 (inclusive)')

def msj_desertor():
    print('\n')
    print('Eres un desertor!\nHas muerto por cobarde!')

def msj_niños():
    import textwrap
    mensaje = 'Has elegido la ruta del bosque.\n' \
              'Vas atravesando el bosque poco a poco, cruzando riachuelos,\n' \
              'árboles altos y deshojados y a lo lejos escuchas algo moverse entre la maleza...\n' \
              'Son los hijos del bosque, originarios de Poniente que solían vivir en' \
              'armonía con la naturalezanhasta la llegada de los Primeros Hombres.\n' \
              'Como ven que no pretendes atacarlos, te han regalado una punta de vidriagón\n.' \
              'Bien!'
    print(textwrap.fill(mensaje))

def msj_rey():
    import textwrap
    mensaje = 'Has elegido la ruta del camino del rey.\n' \
              'Es un sendero seguro y conocido.\n' \
              'A lo lejos, parece que ves una posada en la que podrás comer un plato caliente.'
    print(textwrap.fill(mensaje))

def msj_tundra():
    import textwrap
    mensaje = 'Has elegido la ruta de la tundra.\n' \
              'Atravesando un páramo a lo lejos, parece que observas algo...\n' \
              'Es un Salvaje! Pero está dado la espalda y no te ha visto...\n' \
              'Intenta matarlo con tu lanza antes de que se de la vuelta.\n'
    print(textwrap.fill(mensaje))

def seguir_juego():
    seguir_jugando = -1
    si_no = ('si', 'no')
    while seguir_jugando not in si_no:
        seguir_jugando = input('¿Quieres jugar otra partida? (si/no)').lower()
        if seguir_jugando not in si_no:
            print('\n')
            msj_error()
    return seguir_jugando

def procedimiento_cabanas(salud):
    info_2()
    print('\n')
    enemigo(salud)
    print('\n')

def procedimiento_rutas():
    info()
    pedir_ruta_o = pedir_ruta()
    elige_ruta(pedir_ruta=pedir_ruta_o)
    salud_o = obtener_mas_vida(pedir_ruta=pedir_ruta_o)
    return salud_o

def got():
    """
    Esta funcion ejecuta el juego de GOT. Un guardian de la noche está exhausto caminando más allá del muro.
    Ha encontrado un poblado con 5 cabañas. Si en la cabaña hay un enemigo, muere. Si está vacía o hay un amigo, vive.
    :return:
    """
    seguir_jugando = 'si'
    while seguir_jugando.lower() == 'si':
        salud_o = procedimiento_rutas()
        procedimiento_cabanas(salud=salud_o)
        seguir_jugando = seguir_juego()

if __name__ == '__main__':
    got()
