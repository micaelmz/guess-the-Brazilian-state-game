from turtle import Turtle, Screen
from random import shuffle
import sound_effect as fx
import pandas


screen = Screen()
DATA = pandas.read_csv('brazilian_states.csv', index_col=False)


class GameTypeMode:
    """
    pass
    """
    def __init__(self):
        # loading pandas csv
        self.list_of_states = DATA.state.to_list()

        self.states_turtles = {}
        self.score = 0

        # creating objects and loading images from each state
        for state in self.list_of_states:
            state_csv = DATA[DATA.state == state]
            state_image = self.set_states_images(state, state_csv)
            state_object = self.set_states_objects(state, state_csv)
            self.states_turtles[state] = {
                'image': state_image,
                'object': state_object
            }

        self.list_of_states_remaining = self.list_of_states.copy()
        shuffle(self.list_of_states_remaining)

    def set_states_images(self, state, state_csv):
        state_image = Turtle(visible=False)
        shape_file = state_csv.file.to_string(index=False)
        Screen().addshape(shape_file)
        state_image.shape(shape_file)
        return state_image

    def set_states_objects(self, state, state_csv, final=False):
        state_object = Turtle(visible=False)
        state_object.penup()
        state_object.shape('circle')
        state_object.goto(x=float(state_csv.x.to_string(index=False)), y=float(state_csv.y.to_string(index=False)))
        return state_object

    def player_move(self):
        move = screen.textinput(title=f"Chute um estado",
                                prompt=f"Acertos: {self.score} / {len(self.list_of_states)}\n"
                                       "Digite o nome de um estado?").title()
        if move.lower() == 'parar':
            screen.bye()

        elif move in self.list_of_states_remaining:
            fx.RIGHT.play()
            self.states_turtles[move]['image'].showturtle()
            self.states_turtles[move]['object'].write(move, font=('Times New Roman', 12, 'bold'), align='center')
            self.score += 1
            self.list_of_states_remaining.remove(move)
        else:
            fx.WRONG.play()
