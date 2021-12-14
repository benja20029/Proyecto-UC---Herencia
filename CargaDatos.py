from menus import Dcc_capitolio, mostrar_inicio, mostrar_arenas, mostrar_tributos, mostrar_principal
from random import choices, choice, sample
from parametros import POPULARIDAD_ACCION_HEROICA, PROBABILIDAD_EVENTO, \
    PONDERADOR_AUMENTAR_FUERZA, PRECIPITACIONES_MONTAÑA, PRECIPITACIONES_BOSQUE, \
        HUMEDAD_PLAYA, ENERGIA_BOLITA, ENERGIA_ACCION_HEROICA, AUMENTAR_ENERGIA, \
            VELOCIDAD_VIENTOS_PLAYA, VELOCIDAD_VIENTOS_BOSQUE, AUMENTAR_INGENIO, \
                AUMENTAR_AGILIDAD, NUBOSIDAD_MONTAÑA, COSTO_OBJETO
from clases import Bosque, Montana, Playa, Tributo, Objeto, Ambiente, Personaje, resumen_dccapitolio

class DccObjetos:
    
    def __init__(self, path):
        self.path = path


    ## Funcion que carga los datos de objetos.csv
    def cargar_objetos(self):

        lista_objetos = []

        with open(self.path, "rt", encoding = "utf-8") as archivo_objetos:
            for linea in archivo_objetos:
                linea = linea.strip('\n').split(',')
                linea[0] = Objeto(linea[0], linea[1], linea[2])
                lista_objetos.append(linea[0])

        lista_objetos.pop(0)

        return lista_objetos

class DccTributos:

    def __init__(self, path):
        self.path = path

## Funcion que carga los datos de tributos.csv
    def cargar_tributos(self):

        lista_tributos = []
        clases_tributos = []

        with open(self.path, "rt", encoding = "utf-8") as archivo_tributos:
            for linea in archivo_tributos:
                linea = linea.strip('\n').split(',')
                linea[0] = Tributo(linea[0], linea[1], linea[2], \
        linea[3], linea[4], linea[5], \
            linea[6], linea[7], linea[8], 
            DccObjetos('objetos.csv').cargar_objetos())
                lista_tributos.append(linea[0])

        lista_tributos.pop(0)
        for tributo in lista_tributos:
            tributo.edad = int(tributo.edad)
            tributo.vida = int(tributo.vida)
            tributo.energia = int(tributo.energia)
            tributo.agilidad = int(tributo.agilidad)
            tributo.fuerza = int(tributo.fuerza)
            tributo.ingenio = int(tributo.ingenio)
            tributo.popularidad = int(tributo.popularidad)

        return lista_tributos

## Funcion que carga los datos de arenas.csv
class DccArenas:

    def __init__(self, path):
        self.path = path

    def cargar_arenas(self):

        lista_arenas = []

        with open(self.path, "rt", encoding = "utf-8") as archivo_arenas:
            for linea in archivo_arenas:
                linea = linea.strip('\n').split(',')
                lista_arenas.append(linea)
        
        lista_arenas.pop(0)

        return lista_arenas

## Funcion que carga los datos de ambientes.csv

class DccAmbientes:

    def __init__(self, path):
        self.path = path

    def cargar_ambientes(self):

        linea_nueva = []
        lista_ambientes = []

        with open(self.path, "rt", encoding = "utf-8") as archivo_ambientes:
            for linea in archivo_ambientes:
                linea = linea.strip('\n').split(',')
            
                for texto in linea:
                    if ';' in texto:
                        texto = texto.split(';')
                        linea_nueva.append(texto)
                    else:
                        linea_nueva.append(texto)
                if linea_nueva[0] == 'playa':
                    linea_nueva[0] = Playa(linea_nueva[0], [linea_nueva[1], \
                        linea_nueva[2], linea_nueva[3]])
                    lista_ambientes.append(linea_nueva[0])

                elif linea_nueva[0] == 'bosque':
                    linea_nueva[0] = Bosque(linea_nueva[0], [linea_nueva[1], \
                        linea_nueva[2], linea_nueva[3]])
                    lista_ambientes.append(linea_nueva[0])

                elif linea_nueva[0] == 'montaña':
                    linea_nueva[0] = Montana(linea_nueva[0], [linea_nueva[1], \
                        linea_nueva[2], linea_nueva[3]])
                    lista_ambientes.append(linea_nueva[0])
                
                linea_nueva = []
        
        lista_ambientes.pop(0)

        return lista_ambientes
