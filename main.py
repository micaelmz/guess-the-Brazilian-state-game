from turtle import *
from sound_effect import CLICK
import pandas
from click_mode import GameClickMode
from type_mode import GameTypeMode

data = pandas.read_csv('brazilian_states.csv', index_col=False)
game_running = True
gamemode = None
game = None

screen = Screen()
screen.title('Advinhe o Estado Brasileiro')
screen.setup(width=900, height=800)
screen.tracer(0)

bg_turtle = Turtle()

START_IMAGE = 'frames/bg.gif'
FULL_MAP = 'frames/brazil_map.gif'
BACKGROUND_MAP = 'frames/start.gif'

screen.addshape(START_IMAGE)
screen.addshape(FULL_MAP)
screen.addshape(BACKGROUND_MAP)

bg_turtle.shape(START_IMAGE)

screen.update()


# testar se clicar perto do estado printar o nome dele, no caso pra saber se é perto usando as coordenadas do csv
# trocar o valor do x e y pra tudo sem . pra sair o valor de double pra int e poupar linha


def get_mouse_click_coor(x, y):
    global gamemode
    global game

    # main screen, gamemode not setted yet
    if gamemode is None:
        # check if player is clicking in button 1
        if -236 < x < 236 and -34 > y > -150:
            CLICK.play()
            bg_turtle.shape(BACKGROUND_MAP)
            game = GameClickMode()
            gamemode = 'click'
            screen.update()
        # check if player is clicking in button 2
        elif -236 < x < 236 and -184 > y > -300:
            CLICK.play()
            bg_turtle.shape(BACKGROUND_MAP)
            game = GameTypeMode()
            gamemode = 'type'
            screen.update()

            move = screen.textinput(title=f"ATENÇÃO",
                                    prompt="CLIQUE EM QUALQUER\n"
                                           "LUGAR DA TELA PARA\n"
                                           "INICIAR O JOGO")

    # gamemode is already setted
    elif gamemode == 'click':
        game.check_click(x, y)
        screen.update()

    elif gamemode == 'type':
        while len(game.list_of_states_remaining) > 0:
            game.player_move()
            screen.update()


onscreenclick(get_mouse_click_coor)
mainloop()
