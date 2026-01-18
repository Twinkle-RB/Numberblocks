import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(0)

last_spawn_time = 0
COOLDOWN = 0.9
blocks = []

ui = turtle.Turtle()
ui.hideturtle()
ui.penup()
ui.color("black")

bar = turtle.Turtle()
bar.hideturtle()
bar.penup()

def draw_instructions():
    ui.goto(-325, 350)
    ui.pendown()
    ui.color("black", "lightgray")
    ui.begin_fill()
    ui.forward(550)
    ui.right(90)
    ui.forward(300)
    ui.right(90)
    ui.forward(550)
    ui.right(90)
    ui.forward(300)
    ui.right(90)
    ui.end_fill()
    ui.penup()
    ui.goto(-300, 150)
    ui.write(
        "CONTROLS\n"
        "[SPACE]   SPAWN NUMBERBLOCK 1\n"
        "[Q]       QUIT\n"
        "[CLICK CLEAR] : REMOVE ALL\n",
        align="left",
        font=("Arial", 20, "bold")
    )

def draw_count():
    count_ui = turtle.Turtle()
    count_ui.hideturtle()
    count_ui.penup()
    count_ui.goto(-300, 70)
    count_ui.color("black")
    count_ui.write(
        f"COUNT : {len(blocks)}",
        align="left",
        font=("Arial", 18, "bold")
    )

def draw_clear_button():
    ui.goto(250, 250)
    ui.pendown()
    ui.color("black", "lightgray")
    ui.begin_fill()
    for _ in range(4):
        ui.forward(120)
        ui.right(90)
    ui.end_fill()
    ui.penup()
    ui.goto(275, 225)
    ui.write("CLEAR", font=("Arial", 16, "bold"))

def clear_all(x = None, y = None):
    for t in blocks:
        t.clear()
        t.hideturtle()
    blocks.clear()

def draw_cooldown_bar():
    bar.clear()
    bar.pensize(16)
    bar.goto(-300, 100)
    bar.pendown()
    bar.color("lightgray")
    bar.forward(200)
    bar.penup()
    elapsed = time.time() - last_spawn_time
    ratio = min(elapsed / COOLDOWN, 1)
    bar.goto(-300, 100)
    bar.pendown()
    bar.color("green")
    bar.forward(200 * ratio)
    bar.penup()    

def draw_ui():
    ui.clear()
    draw_clear_button()
    draw_instructions()
    draw_count()

def draw_arm(t, base_x, base_y, side):
    t.color("brown")
    t.penup()
    t.goto(base_x, base_y+10)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.goto(base_x+side*30, base_y-30)
    t.goto(base_x+side*15, base_y-45)
    t.goto(base_x, base_y - 30)
    t.goto(base_x, base_y + 10)
    t.end_fill()
    t.penup()
    t.goto(base_x+side*15, base_y-45)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

def draw_leg(t, base_x, base_y, side):
    t.color("brown")
    t.penup()
    t.goto(base_x+side*15, base_y-50)
    t.pendown()
    t.pensize(27.5)
    t.goto(base_x+side*20, base_y-75)
    t.pensize(1)

def draw_mouth(t, x, y):
    t.color("brown")
    t.pensize(10)
    t.penup()
    t.goto(x, y-37.5)
    t.setheading(-30)
    t.pendown()
    t.circle(25, 120)
    t.pensize(1)

def spawn_numberblocks():
    global last_spawn_time
    now = time.time()
    if now - last_spawn_time < COOLDOWN:
        return
    last_spawn_time = now
    t = turtle.Turtle()
    blocks.append(t)
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    while True:
        if (-325 < x < 225 and 50 < y < 50) or (250 < x < 370 and 130 < y < 250):
            x = random.randint(-500, 500)
            y = random.randint(-500, 500)
        else:
            break       
    t.hideturtle()
    t.speed(0)
    draw_arm(t, x-50, y, -1)
    draw_arm(t, x+50, y,  1)
    draw_leg(t, x, y, -1)
    draw_leg(t, x, y,  1)
    t.penup()
    t.goto(x-50, y-50)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x, y-30)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.penup()
    t.goto(x, y-20)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()
    t.goto(x, y-5)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.goto(x+5, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.goto(x-7.5, y+60)
    t.pendown()
    t.color("black")
    t.write("I", font=("Arial", 50, "bold"))
    draw_mouth(t, x, y)
    t.penup()
    draw_ui()

def click_handler(x, y):
    if 250 < x < 370 and 130 < y < 250:
        clear_all()

def quit_program():
    screen.bye()

draw_instructions()
draw_clear_button()

screen.listen()
screen.onkey(spawn_numberblocks, "space")
screen.onkey(quit_program, "q")
screen.onclick(click_handler)

while True:
    draw_cooldown_bar()
    draw_ui()
    screen.update()
    time.sleep(0.016)
