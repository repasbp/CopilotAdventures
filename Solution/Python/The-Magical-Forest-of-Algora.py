import random


class Character:
    def __init__(self, name):
        self.name = name

    def twirl(self):
        return 'T'

    def leap(self):
        return 'L'

    def spin(self):
        return 'S'

class Forest:
    def __init__(self):
        self.state = ''

    def update_state(self, lox_move, drako_move):
        if lox_move == 'T' and drako_move == 'T':
            self.state = 'Fireflies light up the forest.'
        elif lox_move == 'L' and drako_move == 'S':
            self.state = 'Gentle rain starts falling.'
        elif lox_move == 'S' and drako_move == 'L':
            self.state = 'A rainbow appears in the sky.'
        else:
            self.state = 'The forest is filled with magical sparkles.'

def perform_dance(character1, character2, forest):
    lox_actions = ['twirl', 'leap', 'spin', 'twirl', 'leap']
    drako_actions = ['spin', 'twirl', 'leap', 'leap', 'spin']
    for action1, action2 in zip(lox_actions, drako_actions):
        lox_move = getattr(character1, action1)()
        drako_move = getattr(character2, action2)()
        forest.update_state(lox_move, drako_move)
        print(f'{character1.name} did {action1} and {character2.name} did {action2}.')
        print(f'Forest state: {forest.state}')


print('Welcome to the Magical Forest of Algora!')

lox = Character('Lox')
drako = Character('Drako')
forest = Forest()

perform_dance(lox, drako, forest)