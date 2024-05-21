import turtle
import time

# DASHBOARD DESIGN
board=turtle.Screen()
title=board.title("Pong")
board.bgcolor("black")
board.setup(width=800,height=600)
board.tracer(0)

# SCORE
score_a=0
score_b=0

# PADDLE A
paddle_a=turtle.Turtle()
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color('white')
paddle_a.goto(-350,0)
paddle_a.speed(0)
paddle_a.penup()

# PADDLE B
paddle_b=turtle.Turtle()
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color('white')
paddle_b.goto(350,0)
paddle_b.speed(0)
paddle_b.penup()

# SPLIT LINE
line=turtle.Turtle()
line.shape('square')
line.color('gray')
line.shapesize(stretch_wid=30, stretch_len=0.07)
line.penup()
line.goto(0,0)

#BALL
ball=turtle.Turtle()
ball.shape('square')
ball.color('white')
ball.goto(0,0)
ball_dx=0.3 #speed
ball_dy=0.3
ball.penup()
static=True

#SCORE DASHBOARD
score_board=turtle.Turtle()
score_board.color('white')
score_board.speed(0)
score_board.penup()
score_board.hideturtle()
score_board.goto(-3,220)
score_board.write('0         0',align='center',font=('Fixedsys',60,'bold'))

#ENTER MESSAGE
message=turtle.Turtle()
message.color('white')
message.speed(0)
message.penup()
message.hideturtle()
message.goto(0,120)
message.write('PRESS ENTER TO START', align='center',font=('Fixedsys', 24, 'bold'))

#PADDLES MOVEMENTS
def paddle_a_up():
    y= paddle_a.ycor()
    # movement is limited to avoid the paddle is out the dashboard
    if y <= 240:
        y +=20
        paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    if y >= -220:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    if y <= 240:
        y +=20
        paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    if y >= -220:
        y -= 20
        paddle_b.sety(y)

#GAME START
def init_game():
    # Use global to indicate that the variable static is affected not only in this function, it is affected all the script.
    global static
    # static=False, so the ball can start moving
    static = False
    message.clear()

#RESTART SCOREDASHBOARD
def reset_screen():
    ball.goto(0,0)
    #ball_dx *=-1
    message.write('PRESS ENTER TO START', align='center',font=('Fixedsys', 24, 'bold'))
    paddle_a.goto(-350,0)
    paddle_b.goto(350,0)

#SCORE UPDATE
def update_score():
    score_board.clear()
    score_board.write(f'{score_a}         {score_b}', align='center', font=('Fixedsys', 60,'bold'))

#KEYBOARD SETTINGS
board.listen()
board.onkeypress(paddle_a_up,'w')
board.onkeypress(paddle_a_down,'s')
board.onkeypress(paddle_b_up,'Up')
board.onkeypress(paddle_b_down,'Down')
board.onkeypress(init_game,'Return')

#GAME
while True:
    try:
        board.update()
        #BALL MOVEMENT
        if static==False:
            ball.setx(ball.xcor()+ball_dx)
            ball.sety(ball.ycor()+ball_dy)
        
        #REBOUND SUPERIOR & INFIRIOR LIMIT
        if ball.ycor() > 290 or ball.ycor() < -290: 
            ball_dy *= -1

        #CROSS PADDLE B
        if ball.xcor() > 390:
            score_a += 1
            update_score()
            static = True
            time.sleep(1)
            reset_screen()
        
        #CROSS PADDLE A
        if ball.xcor() < -390:
            score_b +=1
            update_score()
            static=True
            time.sleep(1)
            reset_screen()
        
        #REBOUND ON PADDLE B
        if 350 > ball.xcor() > 340 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            ball_dx *= -1
        
        #REBOUND ON PADDLE A
        if -350 < ball.xcor() < -340 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() -50):
            ball_dx *= -1

    except:
        break