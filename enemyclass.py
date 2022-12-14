from random import *
from cardclass import *


class Snail():

    def __init__(self, stats):
        self.cls = stats[3]
        self.name = stats[0]
        self.type = 'enemy'
        self.hp = stats[1]
        self.takedamagemult = 1
        self.damagemult = 1
        self.block = 0
        self.damage = 0
        self.moveset = []
        self.conditions = {}
        self.powerlevel = stats[2]
        self.coins = stats[2]*4
        self.set_moveset()

    def set_moveset(self):
        if self.name == 'Snail Cultist':
            self.moveset.append('snail strike')
            self.moveset.append('incantation')

        elif self.name == 'Spike Snail':
            self.moveset.append('lick')
            self.moveset.append('spiketackle')

        elif self.name == 'Acid Snail':
            self.moveset.append('tacklemacid')
            self.moveset.append('lick')
            self.moveset.append('corrosivespit')

        elif self.name == 'Hard Shell Snail':
            self.moveset.append('chomp')
            self.moveset.append('thrash')
            self.moveset.append('bellow')

        elif self.name == 'Snail Archon':
            self.moveset.append('snailspace')
            self.moveset.append('iwillhaveshell')
            self.moveset.append('torntosnails')

    def add_conditions(self, card_obj):
        for condition, tags in card_obj.effectandtags.items():
            if tags['condition'] == True:
                if condition not in self.conditions.keys():
                    self.conditions[condition] = tags['turns']
                else:
                    self.conditions[condition] += tags['turns']
                return


snails = {'snailcultist': Snail(['Snail Cultist', 28, 1, 'snailcultist']), 'spikesnail': Snail(['Spike Snail', 30, 2, 'spikesnail']), 'acidsnail': Snail(
    ['Acid Snail', 30, 2, 'acidsnail']), 'hardshellsnail': Snail(['Hard Shell Snail', 40, 3, 'hardshellsnail']), 'snailarchon': Snail(['Snail Archon', 150, 9, 'snailarchon'])}


snail_list = list(snails.keys())
