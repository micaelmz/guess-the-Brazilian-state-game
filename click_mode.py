from turtle import Turtle, Screen
from random import shuffle
import sound_effect as fx
import pandas

DATA = pandas.read_csv('brazilian_states.csv', index_col=False)


class GameClickMode:
    """
    pass
    """
    def __init__(self):
        # setting scoreboard object settings
        self.scoreboard_turtle = Turtle(visible=False)
        self.scoreboard_turtle.penup()
        self.scoreboard_turtle.goto(300, 290)
        # loading pandas csv
        self.list_of_states = DATA.state.to_list()

        self.list_of_states_revealed = []
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
        self.scoreboard()

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

    def check_click(self, x, y):
        for state in self.list_of_states:
            state_csv = DATA[DATA.state == state]
            hitbox = int(state_csv.hitbox.to_string(index=False))

            if self.states_turtles[state]['object'].distance(x=x, y=y) < hitbox:
                if self.list_of_states_remaining[0] == state:
                    fx.RIGHT.play()
                    self.list_of_states_revealed.append(self.list_of_states_remaining.pop(0))
                    self.states_turtles[state]['image'].showturtle()
                else:
                    fx.WRONG.play()
                    self.list_of_states_remaining.pop(0)

        self.scoreboard()

    def scoreboard(self):
        self.scoreboard_turtle.clear()
        if len(self.list_of_states_remaining) > 0:
            self.scoreboard_turtle.write(
                f'{self.list_of_states_remaining[0]}\n'
                f'Acertos: {len(self.list_of_states_revealed)}\n'
                f'Restantes: {len(self.list_of_states_remaining)}',
                font=('Times New Roman', 24, 'bold'), align='center'
            )
        else:
            self.finish()

    def finish(self):
        self.scoreboard_turtle.clear()
        self.scoreboard_turtle.write(
            f'Acertos: {len(self.list_of_states_revealed)} / {len(self.list_of_states)}',
            font=('Times New Roman', 24, 'bold'), align='center'
        )

        for state in self.list_of_states:
            self.states_turtles[state]['object'].write(
                f'{state}',
                font=('Times New Roman', 12, 'bold'), align='center'
            )