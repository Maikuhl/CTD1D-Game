"""
Hi everyone, we are doing a terminal-based game similar to slay the spire
TO DO:
  Come up with concepts for:
    artefacts which enhance player character powers
  tie the game together
"""
from cardclass import *
from characterclasses import *
from enemyclass import *
from gameplay_functions import *
from combat_functions import *
from terminalprints import *
from ASCII_Art import *

def main():

  start_game()
  return
  
def start_game():
  player = choose_class()
  player.name = input("What is your name adventurer?\n")
  player.start_deck()
  stage_count = 1
  while True:
    stage_count += choose_stage(player, stage_count)
    print(stage_divider)
    print("You move on to the next stage")
    print(stage_divider)
  
main()