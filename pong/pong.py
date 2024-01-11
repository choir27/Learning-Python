#! python3
# Pong - pong game for beginners

import turtle, winsound, pygame
from pygame.locals import *
from pygame import mixer

# create screen
wn = turtle.Screen()

# set title shown on screen
wn.title('Pong By @choir27')

# set background color on screen
wn.bgcolor('black')

# set height and width of window
wn.setup(width = 800, height = 600)

# stops the window from updating and requires manual updates, increasing the speed by quite a lot
wn.tracer(0)

mixer.init()
mixer.music.load('background.wav')
mixer.music.play(-1)

def gameObject(gameObject, shape, color, positionX, positionY, sizeH, sizeW):
    #sets the animation speed of the game object, setting to 0 is the maximum speed
    gameObject.speed(0)
    #sets the shape of the game object to a specific shape, default size is 20px by 20px
    gameObject.shape(shape)
    #stretch the shape, here it is 5 * 20 = 100 by 1
    gameObject.shapesize(stretch_wid = sizeH, stretch_len = sizeW)
    #sets the color of the game object
    gameObject.color(color)
    #by default, turtle module draws lines, but we don't need that here
    gameObject.penup()
    #sets where the game object will start at, coordinates of x,y
    gameObject.goto(positionX, positionY)


#paddle A
paddle_a = turtle.Turtle()
gameObject(paddle_a, 'square', 'white', -350, 0, 5, 1)

#paddle B
paddle_b = turtle.Turtle()
gameObject(paddle_b, 'square', 'white', 350, 0, 5, 1)

#ball
ball = turtle.Turtle()
gameObject(ball, 'circle', 'white', 0, 0, 1, 1)

# main game loop
#center is at -400wleft, -400wright, -300hup, -300hdown

def paddle_a_up():
    # return the y coordinate of paddle a
    y = paddle_a.ycor()
    y+=20
    # sets the y coordinate to the updated value
    paddle_a.sety(y)    

def paddle_a_down():
    # return the y coordinate of paddle a
    y = paddle_a.ycor()
    y-=20
    # sets the y coordinate to the updated value
    paddle_a.sety(y)    

def paddle_b_up():
    # return the y coordinate of paddle a
    y = paddle_b.ycor()
    y+=20
    # sets the y coordinate to the updated value
    paddle_b.sety(y)    

def paddle_b_down():
    # return the y coordinate of paddle a
    y = paddle_b.ycor()
    y-=20
    # sets the y coordinate to the updated value
    paddle_b.sety(y)    

#dx means delta/change, x representing the x coord. Every time the object moves, the ball in this case, it moves by n pixels
ball.dx = .1
#dx means delta/change, y representing the y coord. Every time the object moves, the ball in this case, it moves by n pixels
ball.dy = .1


# keyboard binding
    
# tells keyboard to wait for keyboard button press, only need to define once
wn.listen()
# on the user pressing the w button on the keyboard, call the function passed through it
wn.onkeypress(paddle_a_up, 'w')

# on the user pressing the s button on the keyboard, call the function passed through it
wn.onkeypress(paddle_a_down, 's')

# on the user pressing the s button on the keyboard, call the function passed through it
wn.onkeypress(paddle_b_up, 'Up')

# on the user pressing the s button on the keyboard, call the function passed through it
wn.onkeypress(paddle_b_down, 'Down')

# Create Pen (Display Score)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
#hides the pen object
pen.hideturtle()
pen.goto(0,260)
playerA = 0
playerB = 0

#displays the string on the first argument, also accepts align and font customizations
pen.write('Player A: ' + str(playerA) + ' Player B: ' + str(playerB), align = 'center', font=('Courier', 24, 'normal'))

while True:
    # updates the screen upon each iteration of the loop
    wn.update()

 
    # move the ball

    # set the x coordinate by the current x coordinate added with the delta cahnge of the ball
    ball.setx(ball.xcor() + ball.dx)
    # set the y coordinate by the current y coordinate added with the delta cahnge of the ball
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # if(ball.xcor())
    # 300(max height)-10 (ball height)
    if ball.ycor() > 290:
        ball.sety(290)
        # reverses the direction
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    # 300(lowest height)-10 (ball height)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # 300(max width)-10 (ball width)
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        playerA += 1
        #clears whats on the screen writing wise
        pen.clear()
        #displays the string on the first argument, also accepts align and font customizations
        pen.write('Player A: ' + str(playerA) + ' Player B: ' + str(playerB), align = 'center', font=('Courier', 24, 'normal'))
    # 300(lowest width)-10 (ball width)
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        playerB += 1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        #clears whats on the screen writing wise
        pen.clear()
        #displays the string on the first argument, also accepts align and font customizations
        pen.write('Player A: ' + str(playerA) + ' Player B: ' + str(playerB), align = 'center', font=('Courier', 24, 'normal'))
    # paddle and ball collision
        
    # if the x coo
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
