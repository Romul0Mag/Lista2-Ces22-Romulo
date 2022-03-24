import turtle # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    ''' Draw a nice housing to hold the traffic lights '''
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


def change_color_red():
    '''change turtle´s color to red'''
    tess.color("red")


def change_color_green():
    '''change turtle´s color to green'''
    tess.color("green")


def change_color_blue():
    '''change turtle´s color to blue'''
    tess.color("blue")


def increase_width():
    '''increase pen´s width'''
    if tess.pensize() < 20:
        tess.pensize(tess.pensize() + 1)


def decrease_width():
    '''decrease pen´s width'''
    if tess.pensize() > 1:
        tess.pensize(tess.pensize() - 1)


def change_window_color():
    '''alternate window background color'''
    if wn.bgcolor() == "lightgreen":
        wn.bgcolor("darkgreen")
    else:
        wn.bgcolor("lightgreen")


def increase_circle_size():
    '''increase the circle radius'''
    if tess.shapesize()[1] < 3:
        tess.shapesize(tess.shapesize()[1] + 0.5)


def decrease_circle_size():
    '''decrease the circle radius'''
    if tess.shapesize()[1] > 1:
        tess.shapesize(tess.shapesize()[1] - 0.5)


wn.onkey(increase_circle_size, "i")
wn.onkey(decrease_circle_size, "d")
# Bind the event handler to the space key.
wn.onkey(change_color_red, "r")
wn.onkey(change_color_green, "g")
wn.onkey(change_color_blue, "b")

wn.onkey(increase_width, "+")
wn.onkey(decrease_width, "-")

wn.onkey(change_window_color, "w")

wn.onkey(advance_state_machine, "space")

wn.listen() # Listen for events
wn.mainloop()