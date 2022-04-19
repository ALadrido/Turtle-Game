from guizero import App, Drawing, Text
#from gpiozero import Button
from turtle import RawTurtle
from random import randint

#button1 = Button(5)
#button2 = Button(21)
#buttonLeft = Button(19)
#buttonRight = Button(18)
#buttonMissile = Button(25)
missile_shot = False                            #Declaration of Variables
score = 0
time = 60


def place_red_square():                         #Creating Red Square, Placing it randomly
    global red_square
    global red_square_y
    global red_square_x
    red_square_x = randint(100, 400)
    red_square_y = randint(100, 400)
    red_square = drawing.rectangle(red_square_x, red_square_y, red_square_x + 20, red_square_y + 20, color = "red")

#Utilization of Bread Board, Raspberry Pi, Buttons, Widgets
#def move_up():
    #global missile_shot
    #global red_square_area
    #global red_square
    #global score
    #while button1.is_active and not missile_shot:
        #turtle.seth(90)
        #turtle.forward(5)
#def move_down():
    #global missile_shot
    #global red_square_area
    #global red_square
    #global score
    #while button2.is_active and not missile_shot:
        #turtle.seth(270)
        #turtle.forward(5)
#def move_left():
    #global missile_shot
    #global red_square_area
    #global red_square
    #global score
    #while buttonLeft.is_active and not missile_shot:
        #turtle.seth(180)
        #turtle.forward(5)
#def move_right():
    #global missile_shot
    #global red_square_area
    #global red_square
    #global score
    #while buttonRight.is_active and not missile_shot:
        #turtle.seth(0)
        #turtle.forward(5)
#def shoot_missile():
    #global missile_shot
    #global red_square_area
    #global red_square
    #global score
    #while buttonMissile.is_active and not missile_shot:
        #CREATE MISSILE
        #missile = RawTurtle(drawing.tk)
        #missile.hideturtle()
        #missile.seth(turtle.heading())
        #missile.penup()
        #tp = turtle.position()
        #missile.setpos(tp)
        #missile.showturtle()
        #for i in range(100):
            #missile.forward(5)
            #if (missile.xcor() >= red_square_x and missile.xcor() <= red_square_x + 20) \
                #and \
                #(missile.ycor()*-1 >= red_square_y and missile.ycor()*-1 <= red_square_y + 20):
                #drawing.delete(red_square)
                #score += 1
                #score_text.value = "Score: " + str(score)
                #place_red_square()
        #missile.hideturtle()
        #missile_shot = False
    #else:
        #print("Error, Invalid Key")


def key_pressed(event_data):
    global missile_shot                         #Declaring Variables for Missile, Red Square, and Score, For function to see.
    global red_square_area                      #Pulling Global Variables.
    global red_square
    global score
    #print(event_data.key)                                                   #Turtle movement using WASD
    if (event_data.key == "w" and not missile_shot):
        turtle.seth(90)
        turtle.forward(5)
    elif (event_data.key == "a" and not missile_shot):
        turtle.seth(180)
        turtle.forward(5)
    elif (event_data.key == "s" and not missile_shot):
        turtle.seth(270)
        turtle.forward(5)
    elif (event_data.key == "d" and not missile_shot):
        turtle.seth(0)
        turtle.forward(5)
    elif (event_data.key == "m" and not missile_shot):  #not missile_shot does not allow key presses during missile movement
        #CREATE MISSILE
        missile = RawTurtle(drawing.tk)
        missile.hideturtle()
        missile.seth(turtle.heading())  #Determining which way the turtle is facing
        missile.penup()
        tp = turtle.position()           #Setting Turtle Position
        missile.setpos(tp)              #Setting Missile Start Position To Turtle Current Position
        missile.showturtle()            #Showing the missile
        missile_shot = True             #Setting MissileShot to True when Missile Is Fired
        for i in range(100):
            missile.forward(5)          #For Loop for missile movement
            if (missile.xcor() >= red_square_x and missile.xcor() <= red_square_x + 20) \
                and \
                (missile.ycor()*-1 >= red_square_y and missile.ycor()*-1 <= red_square_y + 20):
                drawing.delete(red_square)  #If Missile Hits Red Box, Delete Box
                score += 1                  #Increasing Score
                score_text.value = "Score: " + str(score)   #replacing score value in HUD
                place_red_square()  #Placing a new red square
        missile.hideturtle()        #Hiding Missile
        missile_shot = False        #Setting MissileShot To False
    else:
        print("Error, Wait for the missile to finish shooting.") #If keypress != WASD || M, Output Error

def update_time():          #Updating Time in HUD
    global time
    global score
    time -= 1
    time_text.value = "Time: " + str(time)
    if (time == 0):                 #End of Game when time runs out
        print("End of Game!")
        print("Your Score Was: " + str(score))  #outputting final score
        exit()      #Exiting Application
   


app = App()

app.when_key_pressed = key_pressed
drawing = Drawing(app, width = "fill", height = "fill")
score_text = Text(app, text = "Score : 0")
time_text = Text(app, text = "Time: 60")

turtle = RawTurtle(drawing.tk)
turtle.shape("turtle")
turtle.color("Magenta")
turtle.penup()

#button1.when_pressed = move_up
#button2.when_pressed = move_down
#buttonLeft.when_pressed = move_left
#buttonRight.when_pressed = move_right
#buttonMissile.when_pressed = shoot_missile

place_red_square()

app.repeat(1000, update_time)

app.display()