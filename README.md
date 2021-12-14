# Tarea 1: DCCapitolio :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

<La tarea funciona en general de manera fluida, no se cae, o si se cae,
cuesta mucho que esta se caiga, sin embargo, hay un error al actualizar
los tributos disponibles al momento de atacar, como jugador o tributo seleccionado, pues, 
salen todos los tributos, aunque hayan muerto. Cabe destacar, que al momento de ver el DccResumen por ejemplo,
si el jugador que queda es el nuestro (DCCollao) y Maxy15 (utilizado solamente para dar el ejemplo), y
Maxy15 esta a un ataque de nosotros de morir, si lo elegimos al momento de realizar el ataque 
en la simulacion de hora, el juego se acabara, debido a que no queda ningun otro tributo presente
ademas de nosotros.>

<Los modulos necesarios para hacer correr el programa son 5, los cuales son:
parametros.py , CargaDatos.py, clases.py, menus.py y main.py, estos deben
ser abiertos en ese orden para no tener ningun problema con elementos que
no fueron definidos>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos: 38 pts (27%)
##### ✅  Diagrama <DCCapitolio esta compuesto por listas de Tributo, Arena, Ambiente y Objeto. Ambiente tiene una relacion de agregacion con DCCAmbientes, pues, la lista que retorna DccAmbientes esta compuesta por un conjunto de objetos de clase Ambiente. Por otro lado, Ambiente es superclase de Playa, Montana y Bosque. Luego, tenemos que Arena tiene una relacion de agregacion con DccArenas, debido a que la lista que retorna DccArenas, esta compuesta por objetos de clase Arena. De la misma manera,t enemos que hay una relacion de agregacion entre Objeto y DccObjetos, pues, al igual que las anteriores con sus respectivas clases, DccObjetos retorna una lista que esta compuesta de objetos de clase Objeto. Por ultimo, tenemos que Tributo es superclase de Personaje, que es la clase utilizada para el personaje principal. >
##### ✅ Definición de clases, atributos y métodos <En general las clases se definen de manera correcta, junto con sus metodos>
##### ✅ Relaciones entre clases <Hay relacion de composicion con la clase Dccapitolio que contiene a todas las demas, por otro lado, hay una relacion de agregacion con la clase Dcctributos y Tributo, pues, DccTributos genera una lista compuesta de Tributos>
#### Simulaciones: 12 pts (8%)
##### ✅ Crear partida <Se crea de manera correcta una partida, tanto en la primera como en proximas veces>
#### Acciones: 43 pts (30%)
##### 🟠 Tributo <La clase en general funciona bien a excepcion de la falta de actualizacion de los tributos a atacar>
##### 🟠 Objeto <La clase en general funciona bastante bien, sin embargo, con el metodo entregar_beneficio, se genera una problematica, donde, por razones que no se, dice que se suma una cantidad de fuerza al tributo, pero en realidad se le suma otra. Me gustaria recibir feedback de esto por favor.>
##### ✅ Ambiente <La clase no presenta problemas>
##### ✅ Arena <La clase no presenta problemas>
#### Consola: 34 pts (24%)
##### ✅ Menú inicio <explicacion\>
##### ✅ Menú principal <explicacion\>
##### ✅ Simular Hora <explicacion\>
##### ✅ Robustez <Los menus en general funcionan bastante bien, y el programa no se cae, o si se cae, lo hace con mucha dificultad, pues, yo no logre encontrar forma de echarlo abajo>
#### Manejo de archivos: 15 pts (11%)
##### ✅ Archivos CSV  <Se logra extraer de manera correcta los datos de cada uno de los archivos>
##### ✅ parametros.py <Se utilizan e importan de manera correcta los parametros>
#### Bonus: 3 décimas máximo
##### ❌ Guardar Partida <No se realizo>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```clases.py``` en ```T1```
2. ``` CargaDatos.py``` en ```T1```
3. ```menus.py``` en ```T1```
4. ```parametros.py``` en ```T1```
5. ```Diagrama_clases.pdf``` en ```T1```
6. ```.gitignore``` en ```T1```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```choice-choices-sample / se utilizo en el modulo clases.py```
2. ```librería_2```: ```función() / módulo``` (debe instalarse)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus```: Contiene a ```mostrar_inicio()``` en linea 53, ```mostrar_arenas()``` en linea 35, ```mostrar_tributos()``` en linea 12, ```mostrar_principal```en linea 79(mostrar inicio muestra el menu principal, mostrar arenas y mostrar tributos muestran la seleccion de arena y tributo y mostrar principal, muestra el menu principal).
2. ```CargaDatos```: Contiene a ```DccAmbientes``` en linea 84, ```DccArenas``` en linea 64, ```DccObjetos``` en linea 10, ```DccTributos``` en linea 31 (en general estas clases cargan los datos de las clases a las que se refieren, creando, para cada una, una lista con los objetos de clase a partir de datos extraidos de los archivos.csv).
3. ```Parametros```: Contiene una gran cantidad de parametros que se utilizaron para hacer funcionar el juego, los parametros creados se pondran a continuacion: 

POPULARIDAD_ACCION_HEROICA, PROBABILIDAD_EVENTO, \
    PONDERADOR_AUMENTAR_FUERZA, PRECIPITACIONES_MONTAÑA, PRECIPITACIONES_BOSQUE, \
        HUMEDAD_PLAYA, ENERGIA_BOLITA, ENERGIA_ACCION_HEROICA, AUMENTAR_ENERGIA, \
            VELOCIDAD_VIENTOS_PLAYA, VELOCIDAD_VIENTOS_BOSQUE, AUMENTAR_INGENIO, \
                AUMENTAR_AGILIDAD

4. ```clases```: Contiene a ```Ambiente``` en linea 9, ```Playa``` en linea 19, ```Bosque``` en linea 61, ```Montana``` en linea 104, ``` Tributo``` en linea 147, ``` Arena``` en linea 258, ``` Personaje``` en linea 318 (en general estas clases cargan los datos de las clases a las que se refieren, creando, para cada una, una lista con los objetos de clase a partir de datos ex traidos de los archivos.csv).

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <Los modulos necesarios para hacer correr el programa son 5, los cuales son:
parametros.py , CargaDatos.py, clases.py, menus.py y main.py, estos deben
ser abiertos en ese orden para no tener ningun problema con elementos que
no fueron definidos>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
