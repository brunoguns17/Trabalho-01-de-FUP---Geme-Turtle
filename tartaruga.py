from turtle import *
import turtle
import math
import random
import winsound


# Utilizando a função Turtle() do módulo turtle

# criando janela do game
janela = Screen()

# define o titulo do game
janela.title("TURTLE SPACE")
# função que fine a cor do fundo da tela

janela.bgcolor("black")
janela.bgpic("space.gif")
#criando area interna
caneta = turtle.Turtle()
caneta.penup()
caneta.setposition(-300,-300)
caneta.pendown()
caneta.pensize(3)
caneta.color("white")

#caneta2
caneta2 = turtle.Turtle()
caneta2.penup()
caneta2.setposition(-300,-300)
caneta2.pendown()
caneta2.pensize(3)
caneta2.color("green")

#criação da área interna do game 
for side in range(4):
    caneta.forward(600)
    caneta.left(90)

caneta.hideturtle()#esconde a tartaruga que desenhou área

#mudando a cor dos pontos para vermelho
winsound.PlaySound("gameInit.wav",winsound.SND_ASYNC)

caneta.color("red")

#criando perssonagem
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.shapesize(2)
tartaruga.color("yellow")
tartaruga.penup()
tartaruga.speed(0)

#pontos
pontos = 0
caneta.penup()
caneta.hideturtle()
caneta.setposition(-295,300)
caneta.penup()
ptotal = (f"Pontos: { pontos} ")
caneta.write(ptotal , font=("arial",12, "bold"))

#vida
vida = 3
caneta2.penup()
caneta2.hideturtle()
caneta2.setposition(200,300)
caneta2.penup()
vtotal = (f"Vidas: { vida} ")
caneta2.write(vtotal , font=("arial",12, "bold"))

#comida
comida = turtle.Turtle()
comida.color("red")
comida.shape("circle")
comida.penup()
comida.speed(0)
comida.setposition(random.randint(-300,300),random.randint(-300,300))


#veneno
veneno = turtle.Turtle()
veneno.color("green")
veneno.shape("circle")
veneno.penup()
veneno.speed(0)
veneno.setposition(random.randint(-300,300),random.randint(-300,300))


#criando velovida de movimento
speed =1

#definindo funçoes

def turnleft():
    tartaruga.left(30)
    
def turnright():
    tartaruga.right(30)

def increaspeed():
    global speed
    speed += 0.3


#controle de movimento
turtle.listen()
turtle.onkey(turnleft,"a")
turtle.onkey(turnright,"d")


#loop principal do game
while True:
    #cria a movimentação automatica da tartaruga
    tartaruga.forward(speed)

   #colisão da área interna do game
    if tartaruga.xcor() >=300 or tartaruga.xcor() <=-300:
        tartaruga.right(180)

    if tartaruga.ycor() >=300 or tartaruga.ycor() <=-300:
        tartaruga.right(180)

    #colisão comida
    colidir_comida = math.sqrt(math.pow(tartaruga.xcor()-comida.xcor(),2)+math.pow(tartaruga.ycor()-comida.ycor(),2))
    if colidir_comida <20:
        winsound.PlaySound("comer.wav",winsound.SND_ASYNC)
        pontos +=1
        increaspeed()
        caneta.undo()
        ptotal = (f"Pontos:{ pontos} ")
        caneta.write(ptotal, font=("arial",11, "bold"))
        
        #cria posição aleatoria da comida da tartaruga
        comida.setposition(random.randint(-300,300),random.randint(-300,300))
        
        

    #colisão veneno
    colidir_veneno = math.sqrt(math.pow(tartaruga.xcor()-veneno.xcor(),2)+math.pow(tartaruga.ycor()-veneno.ycor(),2))
    if colidir_veneno <20:
        vida -=1
        winsound.PlaySound("dan.wav",winsound.SND_ASYNC)
        caneta2.undo()
        vtotal = (f"Vidas:{ vida} ")
        caneta2.write(vtotal, font=("arial",11, "bold"))
        

        veneno.setposition(random.randint(-300,300),random.randint(-300,300))
     
        if vida == 0:
         speed = 0
         janela.bgpic("go.gif")
         winsound.PlaySound("gameOver.wav",winsound.SND_ASYNC)
         
    