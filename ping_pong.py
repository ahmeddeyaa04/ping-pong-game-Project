import turtle

# set up the window

window = turtle.Screen()
window.title("ping pong")
window.setup(width=1000 , height=600)
window.tracer(0) 
window.bgcolor(0,0,.11)


# set up the game objects

# ball
ball =turtle.Turtle()   
ball.speed(0)           
ball.shape("circle")
ball.color("white")
ball.shapesize(1)
ball.goto(0,0)   
ball.penup()          
ball_dx,ball_dy =1,1
ball_speed = .2



#center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_wid=25,stretch_len=.1)
center_line.penup()
center_line.goto(0,0)

# player 1

player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.shapesize(stretch_len=1,stretch_wid=5)
player_1.color("blue")
player_1.penup()
player_1.goto(x=-450,y=0)

# player 2

player_2=turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.shapesize(stretch_len=1,stretch_wid=5)
player_2.color("red")
player_2.penup()
player_2.goto(x=450,y=0)

# score text

score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0,y=260)
score.write("player1: 0  player2: 0 ",align="center",font=("courier",14,"normal"))
score.hideturtle()         # to hide the object that appears under the text
player_1_score , player_2_score= 0 , 0


# getting the user inputs to control the players

# players movement

def player1_move_up():
    player_1.sety(player_1.ycor()+30)      # set y (to move in y coordinate) / ycor the actual position of player 1 + 30 p


def player1_move_down():
    player_1.sety(player_1.ycor()-30)

def player2_move_up():
    player_2.sety(player_2.ycor()+30)

def player2_move_down():
    player_2.sety(player_2.ycor()-30)

# get the user inputs to interact with the objects 

window.listen()                             # tell the window to interact with the user inputs
window.onkeypress(player1_move_up,"w")       # when the user presses on "w", "turn on player1_move_up" function
window.onkeypress(player1_move_down,"s")
window.onkeypress(player2_move_up,"Up")
window.onkeypress(player2_move_down,"Down")


while True:
    window.update()

    # ball movement
    ball.setx(ball.xcor() + (ball_dx * ball_speed) )
    ball.sety(ball.ycor() + (ball_dy * ball_speed) )

    # ball and borders collisions
    if ball.ycor() > 290:   # لو مكان الكرة ف الاتجاه y اكبر  من 290
        ball.sety(290)      # ثبت القيمة عند 290
        ball_dy *=-1     # invert y direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *=-1

    # ball and players collisions
    # collision with player 1

    if (ball.xcor())  < -440 and ball.xcor() > -450 and  (ball.ycor()) > (player_1.ycor()-60)  and ball.ycor() < (player_1.ycor()+60):
        ball.setx(-440)
        ball_dx *=-1
    # collision with player 2


    if (ball.xcor())  > 440 and ball.xcor() < 450 and  (ball.ycor()) > (player_2.ycor()-60)  and ball.ycor() < (player_2.ycor()+60):
        ball.setx(440)
        ball_dx *=-1

    # score handling
    if ball.xcor() >490 :
        ball.goto(0,0)
        ball_dx *=-1      # inert the direction of start
        score.clear()
        player_1_score +=1
        score.write(f"player1: {player_1_score}  player2: {player_2_score} ", align="center", font=("courier", 14, "normal"))

    if ball.xcor() < -490 :
        ball.goto(0,0)
        ball_dx *=-1
        score.clear()
        player_2_score +=1
        score.write(f"player1: {player_1_score}  player2: {player_2_score} ", align="center", font=("courier", 14, "normal"))

