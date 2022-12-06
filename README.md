```
███╗   ███╗ ██████╗ ██╗     ██╗     ██╗   ██╗███████╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗
████╗ ████║██╔═══██╗██║     ██║     ██║   ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██║  ██║██╔═══██╗██╔══██╗██║██╔══██╗
██╔████╔██║██║   ██║██║     ██║     ██║   ██║███████╗██║     ██║   ██║██████╔╝███████║██║   ██║██████╔╝██║███████║
██║╚██╔╝██║██║   ██║██║     ██║     ██║   ██║╚════██║██║     ██║   ██║██╔═══╝ ██╔══██║██║   ██║██╔══██╗██║██╔══██║
██║ ╚═╝ ██║╚██████╔╝███████╗███████╗╚██████╔╝███████║╚██████╗╚██████╔╝██║     ██║  ██║╚██████╔╝██████╔╝██║██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
```

```
     /^\    /^\
    (  O)  (  O)
     \ /    \ /
     //     //       _------_
    //     //     ./~        ~-_
   / ~----~/     /              \
 /         :   ./       _---_    ~-
|  \________) :       /~     ~\   |
|        /    |      |  :~~\  |   |
|       |     |      |  \___-~    |
|        \ __/`^\______\.        ./
 \                     ~-______-~\.
 .|                                ~-_
/_____________________________________~~____
```

# Team 4A - Molluscophobia: Attack on Snail

# Scenario: 
This game is created for Michael. He has an absurd hatred for snails and becomes agitated every time he sees a snail. Currently, he is stressed because he is overwhelmed by all the projects in school. He needs something that could relieve his stress and stabilize his emotions. A game that fights against snails could help Michael to feel happy and secrete dopamine.

## Description of the game: 
A RPG card game run on terminal, inspired by Slay the Spire. You can play as either a Tank, Mage or Rogue which all have different starting stats and attributes. The storyline is that the player has suddenly woken up in a forest full of scary mutant snails. The player has to fight against the snails and travel back home. The game is stage based, and the player can choose between combat, treasure, rest stage or buying new cards and/or power ups in the shop after each fight. During the combat stage, the player gets a starting deck of cards and can choose cards to play against the chosen enemy until their mana runs out. After each turn, the player gets to choose one card from a randomised list from the dictionary containing all the skills of the class the player has chosen. Each card has a different amount of damage, block and mana, some cards also have effects which include buffs and debuffs either to the player or the enemy. The combat stage ends when the player or all enemies die.


> This game requires the following libraries installed:

> 1. Regular Expressions
> 2. Random
> 3. Time
> 4. Copy

Enjoy our game!

# Documentation

Documented below are the following types of functions. We will be segregating the functions and classes based on their standard functionalities.
 
Cardclass.py: 

## Classes 

> Card():
     Attributes: 
     -	Damage (int): 
     -	Block (int):
     -	Mana (int):
     -	Name (str): 
     -	Effect_ls (list):
     -	Effect_description (str):
     -	Effect (list):
     -	Effectandtags (dict):
     -	Price (int):
     -	Types (list): returns the type of effect of the card in the list
> Methods:
     -	Get_effect_description(): Describes the card, displays mana requirement, damage, block, and its effects. 
     -	Define_effect(effect_ls): returns a list of effects that should be applied when the card is played. 
          o	each effect is defined as a dictionary: [{'target': target, 'action': action, 'value': value}, ...]

     -	description(): Describes the card, displays mana requirement, damage, block, and its effects.
          o	Returns a string of the descriptions
     -	Get_effect_tags():
          o	Returns a dictionary of effects
     -	Get_card_type():
          o	Returns a list of card types 
          
## Functions (Under Card Class)

Get_card_object(actor, card):
-	Takes in an object type (player,snail) and a card object
-	Returns a dictionary of enemy or class 
Not_enough_mana(player, card): 
-	A function that returns a string, telling the user that they do not have enough mana. Prints current available mana as well.

### Functions that return a dictionary of cards based on the class:
-	Get_class_cards():
-	Get_tankcardsdict():
-	Get_mage_cardsdict():
-	Get_roguecardsdict():
-	Get_enemycardsdict():

Functions that modify the attributes of an object:
-	Get_description(snail):
     o	Takes in a snail object, and returns a formatted string with snail stats.
     
-	Flex(actor): 
     o	Increases the damage attribute of an object by 1 (int)
     
-	Twice(actor):
     o	Doubles the damage received by an object
     
-	Calm(actor):
     o	 Halves the damage received by the player object
     
-	Wrath(actor):
     o	Doubles the damage dealt and damage received by the player object
     
-	Exit_stance():
     o	Cleanse all buffs and debuffs of the player
     
-	Vulnerable():
     o	Enemy receives 150% damage 
     
-	Weak(actor):
     o	Halves the damage dealt by the enemy object
     
-	Poison():
     o	Enemy receives 3 damage for 5 turns
     
-	Snail_ritual():
     o	Player deals 1 (int) additional damage
     
-	Snail_grow():
     o	Player deals 1 (int) additional damage
     
-	Snail_weak():
     o	Enemy deals 75% damage
     
-	Drain(actor):
     o	Takes in an object and returns modified attribute
     
-	Gain_mana(actor):
     o	Takes in an object and returns modified attribute
     
-	Copy(actor): 
     o	Takes in an object and appends the chosen card to be copied into the hand list.
     
-	Snail_spit(actor): 
     o	Appends string “lick” to the graveyard list



Snail()
Attributes:
     - cls [str]
     - name [str]
     - type [str]
     - hp [int/float]
     - takedamagemult [int/float]
     - damagemult [int/float]
     - takedamagemult [int/float]
     - block [int/float]
     - damage [int/float]
     - moveset [list of str]
     - conditions [dict]
     - powerlevel [int]
     - coins [int]
Methods:
     -	__init__(): initializes the object with all the attributes
     -	Set_moveset(): sets moveset based on snail name
     -	Add_conditions(card_obj): adds condition of card to self

Character()
## Attributes:
     -	Cls_display [displays the name nicely with capitalization]
     -	Cls [str for character class]
     -	Maxhp [max hp for character]
     -	Hp [hp variable throughout the game]
     -	Maxmana [maxmana for character]
     -	Mana [mana variable throughout the game]
     -	Block [int]
     -	Damage [int]
     -	Damagemult [damage multiplier]
     -	Takedamagemult [damage recieve multiplier]
     -	Relics [list for relics (not implemented yet)]
     -	Conditions [dictionary of conditions as keys and turns as values]
     -	Deck [list of cards that the player has during the run]
     -	Deckinplay [deck variable in list type]
     -	Graveyard [list of cards used during combat]
     -	Hand [list for player hand]
     -	Coins [player coins as int]
     -	Type [player type]
     -	Name [human player input name]
## Methods:
     -	__init__(): initalizes the object with all the attributes
     -	Start_deck(): gives starting deck based on class
     -	Start_draw(): initializes player draw at the start of combat to draw 5 cards
     -	Draw_card(value): draws a random card from deckinplay
     -	Discard_card_rand(value): discards <value> random cards from hand
     -	Discard_card(card): discards card from hand
     -	Print_hand(): prints player hand
     -	Start_combat(): initializes all variable statuses to default when initializing combat
     -	Add_conditions(card_obj): adds conditions with its turns to the player.conditions dict

## Gameplay Functions 

Choose_class(): 
     -	gets an input from the player to choose a class from Tank, Mage or Rogue, returns invalid if player inputs something else. 
     -	The player can also input info, which returns the description of each class and their starting stats.
     
Choose_stage(player, stage_count): 
-	It contains combat, rest, treasure and shop stages with different weights/probabilities. 
-	It randomly provides 1 to 3 stages that the player could choose from. 

choose_stage_prompt(stage_choice_list): 
-	prompts the user to enter their desired stage. 
-	If the player enters an invalid stage, it notifies the player and promtpts again.

take_me_there(): 
-	increases the stage power and loads the stage according to what the player chooses

rest(player): 
     -	provides the player with the options to rest or skip the stage. 
     -	If the input is neither, notifies the user and prompts again. 
     -	If the choice is to rest, recovers the player’s hp by 50%. 
     -	If the choice is to skip, moves on to the next stage.
Treasure(player): 
-	stage name, calls the choose_card_rewards function

choose_card_rewards(player): 
-	generates a random list of cards from the character class’ skills and prompt the player to choose one or skip. 
-	Adds(append) the card chosen to the list: player’s deck.

Shop(player):
-	allows the player to purchase different items such as cards, hp and mana that could enhance player’s strength using the coins gained from the combats. 
-	It deducts the number of coins and increases attributes of the player.

player_turn(player, enemy_list): 
     -	prints the players options during the turn: 'play_card', 'card_descriptions', 'inspect', or 'end_turn'
     -	Resets the players mana to maximum
     -	While the turn is not ended: prints all enemy's and player’s statuses, the cards in the player’s hand
     -	If player chooses to play card: prompts the player for their choice of card. If the choice of card is not in the player’s hand, notify them and reprompt.               Else if the choice of card has a higher mana cost than the player has remaining mana, notify them and reprompt. Else, play the chosen card.
     -	If the player chooses to end turn: end the turn
     -	If the player chooses to inspect: prompts them for the enemy they wish to inspect. If the input is not within the current enemies names or not all, notify             them and reprompt. If the player enters an current enemies name, print the description of the selected enemy. If the player enters all, print the description           of all enemies.
     -	If the player chooses card descriptions, prints the descriptions of all cards present in the players hands
     -	If the player types something other than any of the options, notify them and reprompt
     
Enemy_turn(player, enemy_list): 
     -	for each enemy, choose a skill from the list of skills of their type
     -	play the card, damaging the player and activating any effects
     
Swap_turn(actor):
     -	Swaps the boolean value, True for player, False for enemies 
     
Combat(player, stage_power)
     -	It calls the spawn_enemies function to generate enemies
     -	It calls player_turn function to allow player to initiate attack on enemies
     -	If player is defeated, it returns death and shows game over screen
     -	If player finishes the turn, it swaps turn
     -	If player defeats all enemies in the stage, it calls choose_card_reward function for the player to choose additional card.
Spawn_enemies(stage_power): 
     -	returns a list of enemies. The total power of the enemies is levelled according to the stage level (4 + stage). We choose enemies of random power level until           the total power has been reached.
     
Card_play(actor, enemy_list, card):
     -	Initializes the card attack type, single or all
     -	Gets the card object from card name
     -	If card object is attack type, plays card according to target type
     -	If card is not attack type, adds block and conditions
     
Card_played(actor, enemy, card):
     -	Gets the card object from card name
     -	Adds effects of card object according to target tag
     -	Applies conditions of actor and enemy
     -	Runs the damage calculation and amends respective health and block values
     -	Resets conditions of actor and enemy
     -	Prints the attack to console
     
Choose_target(enemy_list):
     -	A prompt for the human player to choose an enemy from enemy_list

Deal_damage(actor, enemy, card):
     -	Calculates damage done and returns it
     -	Also reevalutes the enemy block
     
Get_target(str, enemy_dict):
     -	Returns an object if string matches object.name
     
Valid_mana(actor, card):
     -	Returns a boolean if actor has enough mana to play card
     
Mana_deduction(actor, card):
     -	Gets the card object from card name
     -	Deducts required mana to play card from actor mana
     
Ended(enemy_list):
     -	Returns True if all enemies are dead
     
Defeated(actor):
     -	Returns a boolean if actor is dead
     -	Prints a nice terminal print to let everyone know actor is dead
     
Remove_from_combat(actor, enemy_list):
     -	Removes an enemy from the list

Checks(player, enemy_list):
     -	Checks if enemy in enemy_list is dead
     -	Removes dead enemies
     -	If enemy dead, add coins dropped by enemy to player
     
Update_conditions(conditions_dict):
     -	Updates the conditions of the actor
     -	If zero removes the condition
     -	If not zero takes out the turn by one
     
Add_block(actor, card_obj):
     -	Takes the actors block and adds it with the block added by the card object

Reset_conditions(actor):
     -	Resets actor conditions to default values

Death():
     -	Prints the death screen
     -	Asks the player if he would like to play again
     -	If yes start_game()
     -	If no return to main()
     
Start_game(): 
     -	Asks the player to choose a class
     -	Gets the player to input his name
     -	Initalizes player deck according to his class
     -	Initialzies stage count
     -	Plays story from story list every 2 stages
     -	Loops through the stages

Story Functions
     -	Def Chapter_n():
          o	It presents storyline every chapter

