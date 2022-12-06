from cardclass import *
from time import sleep

divider = "---------------------------------------"
small_divider = "--------"

reject_divider = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
stage_divider = "======================================="
start_divider = "+++++++++++++++++++++++++++++++++++++++"


def get_player_status(player):
    print("{}: {} Mana / {} Health / {} Block / conditions {}".format(player.name,
          player.mana, player.hp, player.block, player.conditions))
    return


def display_options(options_list):
    return "[" + "/".join(options_list) + "]"


def print_enemies(enemies_list):
    enemy_names = []
    for enemy in enemies_list:
        print("{} / {} Health / {} block / conditions: {}".format(enemy.name,
              enemy.hp, enemy.block, enemy.conditions))
        enemy_names.append(enemy.name.lower())
    print(divider)
    return enemy_names


def print_attack(actor, target, card, damage):
    sleep(0.5)
    print("{} uses {}".format(actor.name, card))
    sleep(0.5)
    print("{} attacks {} for {} damage".format(
        actor.name, target.name, damage))
    sleep(0.5)
    return


def debugger():
    print("your code works...... so far")
    return
