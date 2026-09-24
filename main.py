import turtle

# setting up the window
window = turtle.Screen()
window.title("Ping Pong Game")
window.setup(width=1000, height=600)
window.tracer(0) # setting delay for update drawings
window.bgcolor(0,0,.11)

### setting game objects
# The ball
ball = turtle.Turtle()
ball.speed(0)    # Drawing speed (fastest)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)  # scale factor (default: 20px*20px) 
ball.goto(x=0, y=0)  #start position
ball.penup()   # ball stop drawing lines while drawing
ball_dx , ball_dy = -1 , 1
ball_speed = .6

# Center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square") 
center_line.color("white")
center_line.shapesize(stretch_len=.1,stretch_wid=27)
center_line.goto(x=0, y=0)
center_line.penup()

# Player 1
player1= turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1,stretch_wid=7)
player1.color("blue")
player1.penup()
player1.goto(x=-450,y=0)

# player 2 
player2= turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1,stretch_wid=7)
player2.color("red")
player2.penup()
player2.goto(x=450,y=0)


# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.goto(x=0,y=270)
score.penup()
score.write(f"player1: 0 player2: 0", align="center", font=("courier",14,"normal"))
score.hideturtle() # To hide the object  [default shape (Arow ->) ]
p1_score, p2_score = 0,0
player_speed = 40

###  players movments
def p1_move_up():
    player1.sety(player1.ycor() + player_speed)

def p1_move_down():
    player1.sety(player1.ycor() - player_speed)

def p2_move_up():
    player2.sety(player2.ycor() + player_speed)

def p2_move_down():
    player2.sety(player2.ycor() - player_speed)

# Get users inputs (Key bindings)
window.listen()  #make the window feels the inputs
window.onkeypress(p1_move_up, "w")  
window.onkeypress(p1_move_up, "W")  
window.onkeypress(p1_move_down, "s") 
window.onkeypress(p1_move_down, "S")
window.onkeypress(p2_move_up, "Up") 
window.onkeypress(p2_move_down, "Down") 

# Game loop
window_display = True

while window_display:
    window.update()

    # Ball movment
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    # Ball and Borders collitions
    if (ball.ycor()> 290):  # 290(TOP border 300 - ball radius 10) 
        ball.sety(290)
        ball_dy*=-1  # invert Y direction

    if (ball.ycor()< -290):  # 290(TOP border 300 - ball radius 10) 
        ball.sety(-290)
        ball_dy*=-1  #invert Y direction

    # collision with player 1
    if ball.xcor() < -430 and ball.xcor() > -440 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-430)
        ball_dx *= -1

    # collision with player 2
    if ball.xcor() > 430 and ball.xcor() < 440 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60):
        ball.setx(430)
        ball_dx *= -1

    # Score Handling
    if (ball.xcor() > 490):
        ball.goto(x=0, y=0)
        ball_dx*=-1     # invert x direction
        score.clear()   
        p1_score +=1
        score.write(f"player1: {p1_score} player2: {p2_score}", align="center", font=("courier",14,"normal"))
    if (ball.xcor() < -490):
        ball.goto(x=0, y=0)
        ball_dx*=-1   # invert x direction
        score.clear()   
        p2_score +=1
        score.write(f"player1: {p1_score} player2: {p2_score}", align="center", font=("courier",14,"normal"))
    
    if player1.ycor() > 250 :
        player1.sety(250)
    if player2.ycor() > 250 :
        player2.sety(250)    
    if player1.ycor() < -250 :
        player1.sety(-250)
    if player2.ycor() < -250 :
        player2.sety(-250)        
    # End game condition
    score_to_end =  5
    if (p1_score)== score_to_end:
        window_display = False
    if (p2_score)== score_to_end:
        window_display = False    