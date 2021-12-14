from CargaDatos import DccAmbientes, DccArenas, DccObjetos, DccTributos, \
    Tributo, Ambiente
from menus import mostrar_inicio, mostrar_arenas, mostrar_tributos, mostrar_principal
from parametros import POPULARIDAD_ACCION_HEROICA, PROBABILIDAD_EVENTO, \
    PONDERADOR_AUMENTAR_FUERZA, PRECIPITACIONES_MONTAÑA, PRECIPITACIONES_BOSQUE, \
        HUMEDAD_PLAYA, ENERGIA_BOLITA, ENERGIA_ACCION_HEROICA, AUMENTAR_ENERGIA, \
            VELOCIDAD_VIENTOS_PLAYA, VELOCIDAD_VIENTOS_BOSQUE, AUMENTAR_INGENIO, \
                AUMENTAR_AGILIDAD
from clases import Arena, Personaje, Playa, Montana, Bosque, Tributo, resumen_dccapitolio
from sys import exit

def mostrar_tributos(tributos):
    opciones_tributo = [str(i) for i in range(1, len(tributos) + 1)]
    contador = 1
    print("\n*** Seleccion de tributo ***")
    print("----------------------------")
    for tributo in tributos:
        print(f"[{contador}] Tributo: {tributo.nombre} | \
Distrito: {tributo.distrito} ")
        contador += 1
    opcion_tributo = input("\nEscoja su tributo: ")  
    while opcion_tributo == '0' or opcion_tributo not in opciones_tributo:
        print(f"La opcion escogida no es valida, por favor escoja\
 una opcion entre 1 y {len(tributos)}")
        opcion_tributo = input("Escoja su tributo: ")
    personaje = tributos.pop(int(opcion_tributo)-1)
    tributo_elegido = Personaje(nombre = personaje.nombre, distrito = personaje.distrito, \
        edad = personaje.edad, vida = personaje.vida, energia = personaje.energia, \
            agilidad = personaje.agilidad, fuerza = personaje.fuerza, ingenio = personaje.ingenio, \
                popularidad = personaje.popularidad, objetos = personaje.objetos)
    print(f"\nEl tributo escogido por usted fue {tributo_elegido.nombre}")
    conjunto_tributos = [tributo_elegido, tributos]
    return conjunto_tributos
    
def mostrar_arenas(arenas):
    opciones_arenas = [str(i) for i in range(1, len(arenas) + 1)]
    print("\n*** Seleccion de arena ***")
    print("--------------------------")
    print(" ")
    for arena in range(1, len(arenas) + 1):
        print(f"[{arena}] Arena: {arenas[arena - 1][0]} | \
Dificultad: {(arenas[arena - 1][1])}")
    opcion_arena = input("\nEscoja su arena: ")
    while opcion_arena == '0' or opcion_arena not in opciones_arenas:
        print(f"La opcion escogida no es valida, por favor elija\
una opcion entre 1 y {len(arenas)}")
        opcion_arena = input("Escoja su arena: ")
    arena_elegida = arenas[int(opcion_arena)-1]
    print(f"\nLa arena escogida por usted fue {arena_elegida[0]}")

    return arena_elegida

def mostrar_inicio(ambiente, tributos, arena, objetos):
    print("""
*** Menú de Inicio ***
----------------------
[1] Iniciar partida
[2] Salir""")

    opcion_inicio = input("\nElija su opcion: ")
    opciones_inicio= ['1', '2']
    while opcion_inicio not in opciones_inicio:
        print("La opcion que selecciono no es valida")
        opcion_inicio = input("Elija su opcion: ")
        
    if opcion_inicio == "1":
        conjunto_tributos = mostrar_tributos(tributos)
        arena_seleccionada = mostrar_arenas(arena)
        arena_seleccionada[0] = Arena(arena_seleccionada[0], arena_seleccionada[1], \
            arena_seleccionada[2], conjunto_tributos[0], conjunto_tributos[1], \
                ambiente)
        mostrar_principal(conjunto_tributos[0], conjunto_tributos[1], arena_seleccionada[0], \
            ambiente, ambiente[0])
        
    elif opcion_inicio == '2':
        print("Muchas gracias por jugar DCCapitolio!")
        exit()
        
def mostrar_principal(tributo_elegido: Personaje, tributos, arena_elegida: Arena, \
    ambientes, ambiente_actual):
    arenas = DccArenas("arenas.csv").cargar_arenas()
    objetos = DccObjetos("objetos.csv").cargar_objetos()
    print("""
    *** Menú Principal ***
    ----------------------
    [1] Simulacion hora
    [2] Mostrar estado del tributo
    [3] Utilizar objeto
    [4] Resumen DCCapitolio
    [5] Volver
    [6] Salir\n""")
    opcion_principal = input("Elija su opción: ")
    opciones_principal = ['1', '2', '3', '4', '5', '6']
    while opcion_principal not in opciones_principal:
        print("La opcion que selecciono no es valida")
        opcion_principal = input("Elija su opcion: ")

    if opcion_principal == '1':
        resultado = simular_hora(tributo_elegido, tributos, arena_elegida, ambientes, ambiente_actual)
        arena_elegida.ejecutar_evento(ambiente_actual)
        arena_elegida.encuentros()
        if type(resultado) == list:
            if resultado[1] == '2':
                tributos = resultado[0]
        if tributo_elegido.vida > 0 and len(tributos) >= 1:
            indice = ambientes.index(ambiente_actual)
            if indice == (len(ambientes) - 1):
                proximo_ambiente = ambientes[0]
        
            else:
                proximo_ambiente= ambientes[indice + 1]

            ambiente_actual = proximo_ambiente
            
        elif tributo_elegido.vida > 0 and len(tributos) == 0:
            print("El juego ha acabado debido a que tu tributo ha ganado")
            exit()
        
        elif tributo_elegido.vida <= 0 and len(tributos) > 0:
            tributo_elegido.esta_vivo = False
            print("El juego ha acabado debido a que tu tributo ha quedado sin vida")
            exit()

        mostrar_principal(tributo_elegido, tributos, arena_elegida, \
            ambientes, ambiente_actual)

    elif opcion_principal == '2':
        tributo_elegido.mostrar_estado()
        mostrar_principal(tributo_elegido, tributos, arena_elegida, \
            ambientes, ambiente_actual)

    elif opcion_principal == '3':
        tributo_elegido.utilizar_objeto(arena_elegida)
        mostrar_principal(tributo_elegido, tributos, arena_elegida, \
            ambientes, ambiente_actual)

    elif opcion_principal == '4':
        resumen_dccapitolio(tributo_elegido, arena_elegida, tributos, \
            ambiente_actual, ambientes)
        mostrar_principal(tributo_elegido, tributos, arena_elegida, \
            ambientes, ambiente_actual)

    elif opcion_principal == '5':
        ambientes = DccAmbientes("ambientes.csv").cargar_ambientes()
        arenas = DccArenas("arenas.csv").cargar_arenas()
        tributos = DccTributos("tributos.csv").cargar_tributos()
        objetos = DccObjetos("objetos.csv").cargar_objetos()
        mostrar_inicio(ambientes, tributos, arenas, objetos)

    elif opcion_principal == '6':
        print("Gracias por participar del DCCapitolio")
        exit()

def simular_hora(tributo_elegido : Personaje, tributos : list, arena: Arena, \
    ambientes: list, ambiente_actual):
    print("""
    *** Simulacion de hora ***
    --------------------------
    [1] Acción heroica
    [2] Atacar a un tributo
    [3] Pedir objeto a patrocinadores
    [4] Hacerse bolita
    [5] Salir\n""")

    opcion_simulacion = input("Elija su opción: ")
    opciones_simulacion = ['1', '2', '3', '4', '5']

    while opcion_simulacion not in opciones_simulacion:
        print("Opcion ingresada invalida")
        mostrar_principal(tributo_elegido, tributos, arena, ambientes, ambiente_actual)
    
    if opcion_simulacion == '1':
        tributo_elegido.accion_heroica()

    elif opcion_simulacion == '2':
        lista_tributos = []
        tributo_elegido.atacar(tributos)

        for tributo in tributos:
            if tributo.vida > 0:
                lista_tributos.append(tributo)
            else:
                tributo.esta_vivo = False
        tributos = lista_tributos
        if len(tributos) == 0:
            print("Has ganado el juego")
            exit()
        lista = [tributos, '2']

        return lista


    elif opcion_simulacion == '3':
        tributo_elegido.pedir_objeto()

    elif opcion_simulacion == '4':
        tributo_elegido.energia += ENERGIA_BOLITA
        print(f"Se hizo bolita de pana y recupero {ENERGIA_BOLITA} de energia")
        tributo_elegido.modificar_energia()
    
    elif opcion_simulacion == '5':
        print("Garsias por jugar al DCCapitolio")
        exit()
        
