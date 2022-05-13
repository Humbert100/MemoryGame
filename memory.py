"""Memory, puzzle game of number pairs.
Author: Humberto Alejandro Rosas Téllez
"""
from random import *
from turtle import *
from wsgiref.validate import WriteWrapper #Mostrar texto en pantalla
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None, 'pairs':0, 'taps':0} #Contador de pairs y taps
hide = [True] * 64

writer = Turtle(visible=True)

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    writer.undo()
    writer.color('red')
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        print(state['mark'])
    else:
        hide[spot], hide[mark] = False, False
        state['pairs'] += 1 #Contador de pares
        state['mark'] = None
   
    '''
                                    Juego Completo
    Si usted desea encontrar todos los pares del memorama, debe de descomentar el 
    siguiente bloque de código y comentar el código que comienza con el if state['pairs'] ==1: 
    '''
    # if not any(hide): #Comprueba si ningún cuadro está oculto, muestra el total de taps realizados
    #     write_total() #Llama función write_total(); imprime "You win!" y "Total:"  

    ##                       Juego terminado al encontrar 1 pares de números                 
    ## Se comprueba si el número de pares es igual a 1; puede modificarlo para un mayor entretenimiento
    
    if state['pairs'] == 1: 
        win() #Llamar a función win();imprime imagen
        write_total() #Llamar a función write_total(); muestra "You win!" y "Total:"                
    else: #Si no se cumple condición anterior, se continúa con el conteo de taps
        state['taps'] += 1 
        write_taps() #Llamar a función write_taps(); enseña "Taps" 

"                                   Función write_total                                             "
def write_total():
    writer.color('red') #Asigna color rojo al texto
    writer.goto(-210,250) #Posición del texto YOU WIN!       
    writer.write("YOU WIN!", font=('Arial',60,'normal')) #Formato del texto YOU WIN!  
    writer.goto(210,-50) #Posición del texto Total
    writer.write("Taps: ",font=('Arial',60,'normal')) #Formato del texto Total:  
    writer.goto(450,-50) #Posición del valor de Total
     #Formato del valor Total; se suma 1 al contador taps para considerar el conteo del último tap
    writer.write(state['taps']+1, font=('Arial',50,'normal')) 

"                                   Función write_taps                                             "
def write_taps():
    writer.color('red') #Asigna color rojo al texto
    writer.goto(210,-50) #Posición del texto Taps
    writer.write("Taps: ",font=('Arial',60,'normal')) #Formato del texto Taps
    writer.goto(450,-50) #Posición del valor de Taps
    writer.write(state['taps'], font=('Arial',50,'normal')) #Formato del valor Taps 

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

"                                   Función win                                             "
def win():
    "Se dibuja la imagen que se muestra con el juego haya finalizado"
    clear() #Limpiar tablero
    goto(10, 10) #Situar 
    shape(car) #Se toma como figura a la imagen
    stamp() #Estampa la copia de la figura
    update() #Actualización de turtle screen
    ontimer(win, 50) #Se asigna valor 50 para fijar imagen
    
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
