import turtle
import random 

gaming_board = turtle.Screen()
gaming_board.bgcolor("light blue")
gaming_board.title("Catch the Turtle")


player_t = turtle.Turtle()
player_t.speed(0)
player_t.hideturtle()  

aim_t =turtle.Turtle()
aim_t.shape("turtle")
aim_t.pencolor("green")
aim_t.speed(0)
aim_t.penup()
aim_t.shapesize(1.5, 1.5, 1.5)  # outline parametresini belirtmezseniz, varsayılan değer kullanılır.


score = 0
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(-55, -gaming_board.window_height() / 2 + 40)
score_display.color("#9966CC")  
score_display.write("Score: 0", align="left", font=("Verdana", 30, "bold"))

time_remaining = 10
time_display = turtle.Turtle()
time_display.penup()
time_display.hideturtle()
time_display.goto(-60, gaming_board.window_height() / 2 - 40)
time_display.color("#5958db") 
time_display.write(f"Time: {time_remaining}", align="left", font=("Verdana", 30, "normal"))


is_target_moving = False


def move_player_t(x, y):
    global score
    player_t.penup()
    player_t.goto(x, y)
    
    if player_t.distance(aim_t) < 20:  
        score += 1  
        score_display.clear()
        score_display.write(f"Score: {score}", align="left", font=("Verdana", 30, "normal"))


def move_target():
    width = gaming_board.window_width()
    height = gaming_board.window_height()

    rand_x = random.randint(-width//2, width//2)
    rand_y = random.randint(-height//2, height//2)

    aim_t.goto(rand_x, rand_y)

    gaming_board.ontimer(move_target, 1000)


def click_handler(x, y):
    print("Tıklama algılandı:", x, y)
    global is_target_moving
    move_player_t(x, y)
    if not is_target_moving:
        is_target_moving = True
        move_target()
        update_timer()



def update_timer():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        time_display.clear()
        time_display.write(f"Time: {time_remaining}",align="left", font=("Verdana", 30, "normal"))
        gaming_board.ontimer(update_timer, 1000)
    else:
        end_game()

def end_game():
    global is_target_moving
    is_target_moving =False
    aim_t.hideturtle()
    player_t.hideturtle()
    time_display.clear()
    score_display.clear()
    score_display.goto(0,0)
    score_display.color("#955251")  

    score_display.write(f"  Game Over! \n\n Your Score: {score}", align="center", font=("Verdana", 30, "bold"))






gaming_board.onclick(click_handler)



turtle.mainloop()


