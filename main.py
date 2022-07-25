from turtle import *
import time
import pandas
from random import shuffle



data = pandas.read_csv('brazilian_states.csv', index_col=False)
game_running = True

screen = Screen()
screen.setup(width=800, height=700)
screen.tracer(0)


bg_turtle = Turtle()

ALL_STATES = data.state.to_list()
shuffle(ALL_STATES)
START_IMAGE = 'frames/bg.gif'
FULL_MAP = 'frames/brazil_map.gif'
BACKGROUND_MAP = 'frames/start.gif'

screen.addshape(START_IMAGE)
screen.addshape(FULL_MAP)
screen.addshape(BACKGROUND_MAP)

bg_turtle.shape(START_IMAGE)


all_states_turtle = {}
for state_name in data.state:
    state_image = Turtle(visible=False)
    state_csv = data[data.state == state_name]
    shape_file = state_csv.file.to_string(index=False)
    screen.addshape(shape_file)
    state_image.shape(shape_file)

    state_object = Turtle(visible=False)
    state_object.penup()
    state_object.shape('circle')
    state_object.goto(x=float(state_csv.x.to_string(index=False)), y=float(state_csv.y.to_string(index=False)))
    state_object.write(state_name, align='center')

    all_states_turtle[state_name] = {'image': state_image,
                                     'object': state_object}

screen.update()


# testar se clicar perto do estado printar o nome dele, no caso pra saber se é perto usando as coordenadas do csv
# trocar o valor do x e y pra tudo sem . pra sair o valor de double pra int e poupar linha


def get_mouse_click_coor(x, y):

    if -236 < x < 236:
        if -34 > y > -150:
            bg_turtle.shape(BACKGROUND_MAP)
        elif -184 > y > -300:
            type_mode()

    for state_name in all_states_turtle:
        state_csv = data[data.state == state_name]
        hitbox = int(state_csv.hitbox.to_string(index=False))
        if all_states_turtle[state_name]['object'].distance(x=x, y=y) < hitbox:
            all_states_turtle[state_name]['image'].showturtle()
            screen.update()

    screen.update()



def type_mode():
    pass


onscreenclick(get_mouse_click_coor)
mainloop()

