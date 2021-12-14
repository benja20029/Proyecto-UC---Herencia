from menus import mostrar_inicio, mostrar_arenas, mostrar_tributos, mostrar_principal
from CargaDatos import DccAmbientes, DccArenas, DccObjetos, DccTributos
from parametros import POPULARIDAD_ACCION_HEROICA, PROBABILIDAD_EVENTO, \
    PONDERADOR_AUMENTAR_FUERZA, PRECIPITACIONES_MONTAÑA, PRECIPITACIONES_BOSQUE, \
        HUMEDAD_PLAYA, ENERGIA_BOLITA, ENERGIA_ACCION_HEROICA, AUMENTAR_ENERGIA, \
            VELOCIDAD_VIENTOS_PLAYA, VELOCIDAD_VIENTOS_BOSQUE, AUMENTAR_INGENIO, \
                AUMENTAR_AGILIDAD
from clases import Tributo, Personaje, Bosque, Montana, Playa, Ambiente, Arena, resumen_dccapitolio

class DccCapitolio:

    def __init__(self):
        self.ambientes = DccAmbientes("ambientes.csv").cargar_ambientes()
        self.arenas = DccArenas("arenas.csv").cargar_arenas()
        self.tributos = DccTributos("tributos.csv").cargar_tributos()
        self.objetos = DccObjetos("objetos.csv").cargar_objetos()

    def dcc_capitolio(self):
        mostrar_inicio(self.ambientes, self.tributos, self.arenas, self.objetos)

def correr_juego():
    juego = DccCapitolio()
    juego.dcc_capitolio()

correr_juego()

