from parametros import AUMENTAR_AGILIDAD, AUMENTAR_ENERGIA, AUMENTAR_INGENIO, \
 COSTO_OBJETO, ENERGIA_ACCION_HEROICA, HUMEDAD_PLAYA, PONDERADOR_AUMENTAR_FUERZA, \
POPULARIDAD_ACCION_HEROICA, PRECIPITACIONES_BOSQUE, PROBABILIDAD_EVENTO, \
 VELOCIDAD_VIENTOS_BOSQUE, VELOCIDAD_VIENTOS_PLAYA, \
     NUBOSIDAD_MONTAÑA, PRECIPITACIONES_MONTAÑA
from random import choice, choices, sample
from CargaDatos import DccObjetos, DccTributos, DccArenas

class Ambiente:
    def __init__(self, nombre, evento):
        self.nombre = nombre
        self.evento = evento

    def calcular_daño(self, tributos):
        daño_evento = 0
        for tributo in tributos:
            tributo.vida -= daño_evento

class Playa(Ambiente):
    def __init__(self, nombre, evento):
        super().__init__(nombre, evento)
        self.nombre = nombre
        self.evento = evento
    
    def calcular_daño(self, tributos):
        tributos_dañados = []
        tributo_seleccionado = []
        daño_evento = 0
        pesos_eventos = [PROBABILIDAD_EVENTO, PROBABILIDAD_EVENTO, \
                PROBABILIDAD_EVENTO]
        evento_aleatorio = choices(self.evento,k = 1, weights = pesos_eventos)
        if evento_aleatorio == 'tsunami':
            daño_evento = 9
            
        elif evento_aleatorio == 'marea roja':
            daño_evento = 3

        elif evento_aleatorio == 'huracán':
            daño_evento = 10

        daño_ambiente = max(5, (0.4 * \
            (HUMEDAD_PLAYA if self.nombre == 'playa' else 0) + \
                0.2 * ((VELOCIDAD_VIENTOS_BOSQUE if self.nombre == 'bosque' else 0) \
                    + (VELOCIDAD_VIENTOS_PLAYA if self.nombre == 'playa' else 0)) \
                        + 0.1 * ((PRECIPITACIONES_BOSQUE if self.nombre == 'bosque' else 0) \
                            + PRECIPITACIONES_MONTAÑA if self.nombre == 'montaña' else 0) \
                                + (NUBOSIDAD_MONTAÑA if self.nombre == 'montaña' else 0) \
                                    + daño_evento )/5)
        if type(tributos) == list:
            for tributo in tributos:
                tributo.vida -= daño_ambiente
                tributos_dañados.append([tributo.nombre, daño_ambiente, tributo.vida])
            return tributos_dañados

        
        else:
            tributos.vida -= daño_ambiente
            tributo_seleccionado = [tributos.nombre, daño_ambiente, tributos.vida]
            return tributo_seleccionado

class Bosque(Ambiente):
    def __init__(self, nombre, evento):
        super().__init__(nombre, evento)
        self.nombre = nombre
        self.evento = evento
    
    def calcular_daño(self, tributos):
        tributos_dañados = []
        tributo_seleccionado = []
        daño_evento = 0
        pesos_eventos = [PROBABILIDAD_EVENTO, PROBABILIDAD_EVENTO, \
                PROBABILIDAD_EVENTO]
        evento_aleatorio = choices(self.evento,k = 1, weights = pesos_eventos)

        if evento_aleatorio == 'incendio':
            daño_evento = 5

        elif evento_aleatorio == 'tormenta eléctrica':
            daño_evento = 4
            
        elif evento_aleatorio == 'gas venenoso':
            daño_evento = 8

        daño_ambiente = max(5, (0.4 * \
            (HUMEDAD_PLAYA if self.nombre == 'playa' else 0) + \
                0.2 * ((VELOCIDAD_VIENTOS_BOSQUE if self.nombre == 'bosque' else 0) \
                    + (VELOCIDAD_VIENTOS_PLAYA if self.nombre == 'playa' else 0)) \
                        + 0.1 * ((PRECIPITACIONES_BOSQUE if self.nombre == 'bosque' else 0) \
                            + PRECIPITACIONES_MONTAÑA if self.nombre == 'montaña' else 0) \
                                + (NUBOSIDAD_MONTAÑA if self.nombre == 'montaña' else 0) \
                                    + daño_evento )/5)
        if type(tributos) == list:
            for tributo in tributos:
                tributo.vida -= daño_ambiente
                tributos_dañados.append([tributo.nombre, daño_ambiente, tributo.vida])
            return tributos_dañados

        
        else:
            tributos.vida -= daño_ambiente
            tributo_seleccionado = [tributos.nombre, daño_ambiente, tributos.vida]
            return tributo_seleccionado

class Montana(Ambiente):
    def __init__(self, nombre, evento):
        super().__init__(nombre, evento)
        self.nombre = nombre
        self.evento = evento
    
    def calcular_daño(self, tributos):
        tributos_dañados = []
        tributo_seleccionado = []
        daño_evento = 0
        pesos_eventos = [PROBABILIDAD_EVENTO, PROBABILIDAD_EVENTO, \
                PROBABILIDAD_EVENTO]
        evento_aleatorio = choices(self.evento,k = 1, weights = pesos_eventos)

        if evento_aleatorio == 'avalancha':
                daño_evento = 6
            
        elif evento_aleatorio == 'tormenta de nieve':
            daño_evento = 5

        elif evento_aleatorio == 'erupción volcánica':
            daño_evento = 10

        daño_ambiente = max(5, (0.4 * \
            (HUMEDAD_PLAYA if self.nombre == 'playa' else 0) + \
                0.2 * ((VELOCIDAD_VIENTOS_BOSQUE if self.nombre == 'bosque' else 0) \
                    + (VELOCIDAD_VIENTOS_PLAYA if self.nombre == 'playa' else 0)) \
                        + 0.1 * ((PRECIPITACIONES_BOSQUE if self.nombre == 'bosque' else 0) \
                            + PRECIPITACIONES_MONTAÑA if self.nombre == 'montaña' else 0) \
                                + (NUBOSIDAD_MONTAÑA if self.nombre == 'montaña' else 0) \
                                    + daño_evento )/5)
        if type(tributos) == list:
            for tributo in tributos:
                tributo.vida -= daño_ambiente
                tributos_dañados.append([tributo.nombre, daño_ambiente, tributo.vida])
            return tributos_dañados

        
        else:
            tributos.vida -= daño_ambiente
            tributo_seleccionado = [tributos.nombre, daño_ambiente, tributos.vida]
            return tributo_seleccionado

class Tributo:
    def __init__(self, nombre, distrito, edad, vida, energia, \
agilidad, fuerza, ingenio, popularidad, objetos):
        
        self.nombre = nombre
        self.distrito = distrito
        self.edad = edad
        self.vida = vida
        self.energia = energia
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.ingenio = ingenio
        self.popularidad = popularidad
        self.esta_vivo = True
        self.mochila = []
        self.peso = 0
        self.objetos = objetos

    def atacar(self, tributos):
        if type(tributos) == list:
            opciones_ataque = [str(i) for i in range(1, len(tributos) + 1)]
            print("*** Seleccion tributos a atacar ***")
            for tributo in range(1, len(tributos) + 1):
                print(f"[{tributo}] | Nombre: {(tributos[tributo-1]).nombre}")
            print("")
            tributo_a_atacar = input("Seleccione el tributo que desea atacar: ")
            while tributo_a_atacar not in opciones_ataque:
                print("La opcion que eligio no esta entre las disponibles, por favor\
    escoja denuevo")
                tributo_a_atacar = input("Seleccione el tributo que desea atacar: ")
            tributo = tributos[int(tributo_a_atacar) - 1]

            daño_producido = min(90, max(5, ((60 * self.fuerza + 40 * self.agilidad\
    + 40 * self.ingenio - 30 * self.peso) / self.edad)))

            tributo.vida -= daño_producido
            tributo.vida = round(tributo.vida)
            if tributo.vida > 0:
                print(f"{self.nombre} le ha quitado {daño_producido} a {tributo.nombre} \
dejandolo con {tributo.vida} de vida")
            
            elif tributo.vida <= 0:
                print(f"{self.nombre} le ha quitado {daño_producido} a {tributo.nombre} \
provocando su muerte")

        else:
            daño_producido = min(90, max(5, ((60 * self.fuerza + 40 * self.agilidad\
    + 40 * self.ingenio - 30 * self.peso) / self.edad)))

            tributos.vida -= daño_producido
            tributos.vida = round(tributos.vida)
            if tributos.vida > 0:
                print(f"{self.nombre} le ha quitado {daño_producido} a {tributos.nombre} \
dejandolo con {tributos.vida} de vida")
            elif tributos.vida <= 0:
                print(f"{self.nombre} le ha quitado {daño_producido} a {tributos.nombre} \
provocando su muerte")

    def utilizar_objeto(self, arena_seleccionada):
        contador = 1
        if len(self.mochila) > 1:
            for objeto in self.mochila:
                print(f"[{contador}] [{objeto.nombre}] | Tipo: [{objeto.tipo}]")
                contador += 1
            seleccion_objeto = input("Seleccione el objeto que desea utilizar: ")
            opciones_seleccion = [str(i) for i in range (1, len(self.mochila) + 1)]

            contador = 0
            
            while seleccion_objeto not in opciones_seleccion:
                print("La opcion ingresada es invalida\n")
                self.utilizar_objeto(arena_seleccionada)
            
            objeto_seleccionado = self.mochila.pop(int(seleccion_objeto)-1)
            objeto_seleccionado.entregar_beneficio(self, arena_seleccionada)
        
        elif len(self.mochila) == 1:
            print(f"[1] [{self.mochila[0].nombre}] \
| Tipo: [{self.mochila[0].tipo}]")
            seleccion_objeto = input("Seleccione el objeto que desea utilizar: ")
            opciones_seleccion = [str(i) for i in range (1, len(self.mochila) + 1)]
            
            while seleccion_objeto not in opciones_seleccion:
                print("La opcion ingresada es invalida\n")
                self.utilizar_objeto(arena_seleccionada)
            
            objeto_seleccionado = self.mochila.pop(int(seleccion_objeto)-1)
            objeto_seleccionado.entregar_beneficio(self, arena_seleccionada)

        else:
            print("No tiene objetos en su mochila, amigo/a, vuelva pronto")

    def pedir_objeto(self):
        if self.popularidad > COSTO_OBJETO:
            self.popularidad -= COSTO_OBJETO
            objeto_elegido = (choice(self.objetos))
            self.mochila.append(objeto_elegido)
            self.peso += int(objeto_elegido.peso)
            print(f"Se añadio {objeto_elegido.nombre} a tu mochila")
        else:
            print("Su popularidad no es suficiente, lo sentimos")
        
    def accion_heroica(self):
        if self.energia > ENERGIA_ACCION_HEROICA:
            self.popularidad += POPULARIDAD_ACCION_HEROICA
            print("Tremenda accion heroica, go simp")
        
        else:
            print("Esto no es posible debido a su baja energia, \
por favor intente con otra opcion")

class Arena:
    def __init__(self, nombre, dificultad, riesgo, jugador, tributos, ambientes):
        self.nombre = nombre
        self.dificultad = dificultad
        self.riesgo = riesgo
        self.jugador = jugador
        self.tributos = tributos
        self.ambientes = ambientes

    def ejecutar_evento(self, ambiente_actual):
        tributos_dañados = ambiente_actual.calcular_daño(self.tributos)
        tributo_seleccionado = ambiente_actual.calcular_daño(self.jugador)

        lista_tributos = []
        print(" ")
        for tributo in tributos_dañados:
            if tributo[2] <= 0:
                print(f"{tributo[0]} ha recibido {tributo[1]} de daño, lo que lo \
ha dejado con {tributo[2]} de vida, provocando su muerte")

            elif tributo[2] > 0:
                print(f"{tributo[0]} ha recibido {tributo[1]} de daño, lo que lo \
ha dejado con {tributo[2]} de vida")

        if tributo_seleccionado[2] <= 0:
            print(f"\nTu tributo {tributo_seleccionado[0]} ha sufrido {tributo_seleccionado[1]} \
de daño, dejandolo con {tributo_seleccionado[2]} de vida, provocando su muerte\n")
            print(f"El juego se ha acabado debido a que tu tributo {tributo_seleccionado[0]}, \
se ha quedado sin vida ")
            self.jugador.esta_vivo = False
            exit()
            
        elif tributo_seleccionado[2] > 0:
            print(f"\nTu tributo {tributo_seleccionado[0]} ha sufrido {tributo_seleccionado[1]} \
de daño, dejandolo con {tributo_seleccionado[2]} de vida\n")

        for tributo in self.tributos:
            if tributo.vida > 0:
                lista_tributos.append(tributo)
            else:
                tributo.esta_vivo = False
        
        self.tributos = lista_tributos

    def encuentros(self):
        lista_tributos = [] 
        n_encuentros = (round(float(self.riesgo)) * len(self.tributos)) // 2
        for encuentro in range(0, n_encuentros):
            tributos_encuentro = sample(self.tributos, 2)
            tributo_atacante = tributos_encuentro[0]
            tributo_atacado = tributos_encuentro[1]
            tributo_atacante.atacar(tributo_atacado)
            
        for tributo in self.tributos:
            if tributo.vida > 0:
                lista_tributos.append(tributo)
            else:
                tributo.esta_vivo = False
        self.tributos = lista_tributos

class Personaje(Tributo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    ## property
    def obtener_energia(self):
        return self.energia

    ## Vida setter
    def modificar_energia(self):
        if self.energia > 100:
            self.energia = 100

    def mostrar_estado(self):
        texto = (f"Objetos: ")
        if len(self.mochila) > 0:
            for objeto in self.mochila:
                texto += (f"{objeto.nombre}, ")
        print(("Estado tributo").center(30))
        print("----------------------------------------------------------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Distrito: {self.distrito}")
        print(f"Edad: {self.edad}")
        print(f"Vida: {self.vida}")
        print(f"Energía: {self.energia}")
        print(f"Agilidad: {self.agilidad}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Ingenio: {self.ingenio}")
        print(f"Popularidad: {self.popularidad}")
        print(texto)
        print(f"Peso: {self.peso}")
        print("")

def resumen_dccapitolio( tributo_elegido: Personaje, arena: Arena, \
    tributos: list, ambiente_actual, ambientes: list):
    print("Estado DCCapitolio".center(30))
    print("----------------------------------------------------------------------------")
    print(f"Dificultad: {arena.dificultad}")
    print("Tributos vivos:")
    for tributo in tributos:
        if tributo.vida > 0 and tributo.esta_vivo == True:
            print(f"{tributo.nombre}: {tributo.vida}".center(10))
    print(f"{tributo_elegido.nombre}: {tributo_elegido.vida}")
    indice = ambientes.index(ambiente_actual)
    if indice == (len(ambientes) - 1):
        proximo_ambiente = ambientes[0]
    else:
        proximo_ambiente= ambientes[indice + 1]
    print(f"Próximo ambiente: {proximo_ambiente.nombre}")

class Objeto:
    def __init__(self, nombre, tipo, peso):
         self.nombre = nombre
         self.tipo = tipo
         self.peso = peso
    
    def entregar_beneficio(self, tributo: Personaje, arena_seleccionada):

        if self.tipo == 'consumible':
            tributo.energia += AUMENTAR_ENERGIA
            print(f"Su energia ha sido aumentada en {AUMENTAR_ENERGIA}")
            tributo.modificar_energia()
        elif self.tipo == 'arma':
            tributo.fuerza += round(tributo.fuerza * (PONDERADOR_AUMENTAR_FUERZA \
* float(arena_seleccionada.riesgo) + 1))
            print(f"Su fuerza ha aumentado en \
{round(tributo.fuerza * (PONDERADOR_AUMENTAR_FUERZA * float(arena_seleccionada.riesgo) + 1))}")
        elif self.tipo == 'especial':
            tributo.fuerza += (tributo.fuerza * (PONDERADOR_AUMENTAR_FUERZA \
                * float(arena_seleccionada.riesgo) + 1))
            print(f"Su fuerza ha aumentado en \
{round(tributo.fuerza * (PONDERADOR_AUMENTAR_FUERZA * float(arena_seleccionada.riesgo) + 1))}")
            tributo.energia += AUMENTAR_ENERGIA
            print(f"Su energia ha sido aumentada en {AUMENTAR_ENERGIA}")
            tributo.agilidad += AUMENTAR_AGILIDAD
            print(f"Su agilidad ha aumentado en {AUMENTAR_AGILIDAD}")
            tributo.ingenio += AUMENTAR_INGENIO
            print(f"Su ingenio ha aumentado en {AUMENTAR_INGENIO}")
            tributo.modificar_energia()
