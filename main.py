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
#from combat_functions import *
from terminalprints import *
from ASCII_Art import *


def main():

    while True:

        start = welcome()
        cont = start
        run_game = cont
        if start:
            while cont:
                if run_game:
                    run_game = start_game()
                else:
                    cont = death()
                    run_game = cont
        else:
            return
    return


main()

