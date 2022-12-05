from characterclasses import *
from cardclass import *
from enemyclass import *
from terminalprints import *
from time import sleep
from copy import *
from ASCII_Art import *
from story import *
import random

def choose_class():
  while True:
    print("Choose a class:")
    print("[Tank/Mage/Rogue]")
    print("Type 'info' for more information")
    cmd = input().lower()
    if cmd not in ['tank', 'mage', 'rogue', 'info']:
      print("Please choose a valid option")
    else:
      if cmd == 'info':
        print("[Tank/Mage/Rogue]")
        print("Which character class would you like to see?")
        let_me_see = input().lower()
        if let_me_see == 'tank':
          print("The Tank is one of three playable characters in Molluscophobia. He wields an arsenal of powerful strikes, boasts formidable defensive options, and draws fiendish strength from his demonic benefactors to empower himself in various ways. He starts with 80 hp, highest of the playable characters")
        elif let_me_see == 'mage':
          print("The Mage is one of three playable characters in Molluscophobia. She is a monk that utilizes the effects of her different stances to her advantage, boasts an arsenal oriented around deck control via scrying, retain, and Energy generation, as well as a unique focus on mid-combat card generation. She starts with 72 HP.")
        elif let_me_see == 'rogue':
          print("The Silent is one of three playable characters in Molluscophobia. She is a huntress themed on a rogue fantasy build. This cunning character weakens her foes with numerous cuts and poison, while using cheap tricks and agility to avoid their attacks. With many powerful cards that draw and discard, the Silent ensures that she will always be one step ahead of her enemy. She starts with a relatively low 70 hp.")
      if cmd in ['tank', 'mage', 'rogue']:
          return classes[cmd.lower()]

def choose_stage(player, stage_count):
  print("Stage {}:".format(stage_count))
  stage_type = ['combat', 'rest', 'treasure', 'shop']
  stage_choices = []
  if stage_count % 9 == 0 or stage_count % 9 == 1:
    stage_choices.append('combat')
    choice = choose_stage_prompt(stage_choices)
    take_me_there(player, choice, stage_count)
    return 1
  elif stage_count % 9 == 8:
    stage_choices.append('rest')
    choice = choose_stage_prompt(stage_choices)
    take_me_there(player, choice, stage_count)
    return 1
  else:
    how_many_stages = random.randint(1, 3)
    for i in range(how_many_stages):
      stage_choices.append(random.choices(stage_type, weights=(70, 10, 10, 10), k=1)[0])
    choice = choose_stage_prompt(stage_choices)
    take_me_there(player, choice, stage_count)
    return 1
        
def choose_stage_prompt(stage_choice_list):
  while True:
    print(stage_choice_list)
    print("choose a stage")
    cmd = input().lower()
    if cmd not in stage_choice_list:
      print("please choose a valid option")
    else:
      return cmd

def take_me_there(player, stage, stage_count):
  stage_power = 0 + stage_count
  if stage == 'combat':
    return combat(player, stage_power)
  elif stage == 'rest':
    return rest(player)
  elif stage == 'shop':
    return shop(player)
  elif stage == 'treasure':
    return treasure(player)
                      

def rest(player):
  options = ['rest', 'skip']
  print(display_options(options))
  while True:
    choice = input()
    if choice not in options:
      print("I don't think you should do that here")
    elif choice == 'rest':
      player.hp = min([player.hp + player.maxhp * 0.5, player.maxhp])
      print("You have recovered 50% of your health!")
      break
    elif choice == 'skip':
      break
  return

def treasure(player):
  choose_card_reward(player)

def choose_card_reward(player):
  card_dictionary = class_cards[player.cls]
  card_list = list(card_dictionary)
  card_options = [card_list[randint(0, len(card_list)-1)],card_list[randint(0, len(card_list)-1)],card_list[randint(0, len(card_list)-1)]]
  while True:
    print("Loot: Choose one card or skip")
    print(card_options)
    cmd = input().lower()
    if cmd == 'skip':
      break
    elif cmd not in card_options:
      print("Please choose a valid option")
    else:
      player.deck.append(cmd)
      break

def shop(player):
  cards = list(class_cards[player.cls])
  card_list = {}
  for i in range(8):
    random_card = cards[randint(0, len(cards)-1)]
    card_list[random_card] = get_card_object(player, random_card).price
  while True:
    print("Welcome to the shop, what would you like to buy?")
    print("[Cards/Health/Mana]")
    print("You have ", player.coins, " coins.")
    cmd = input().lower()
    if cmd not in ['cards', 'health', 'mana']:
      print("Please choose a valid option")
    elif cmd == 'cards':
      while True:
        print(card_list)
        print("choose a card or go back")
        choice = input()
        if choice == 'go back':
          break
        elif choice not in card_list:
          print("we don't sell that, asshole")
        elif class_cards[player.cls][choice].price > player.coins: 
          print("come back with more money")
        else:
          player.coins -= class_cards[player.cls][choice].price
          player.deck.append(choice)
          break
      print("Continue shopping? [Yes, No]")
      cmd1 = input().lower()
      if cmd1 not in ['yes', 'no']:
        print("say what")
      elif cmd1 == "yes":
        pass
      else:
        return
    elif cmd == 'health':
      while True:
        try:
          choice = int(input("How much hp? [1hp:1coin]: "))
        except ValueError:
          print("Enter valid number")
          continue
        else:
          if player.coins < choice:
            print("come back with more money")
          else:
            player.coins -= choice
            player.maxhp += choice
            print("your max hp increased by {}".format(choice))
            break
      print("Continue shopping? [Yes, No]")
      cmd1 = input().lower()
      if cmd1 not in ['yes', 'no']:
        print("say what")
      elif cmd1 == "yes":
        pass
      else:
        return
    else:
      while True:
        try:
          choice = int(input("How much mana? [1mana:5coins]: "))
        except ValueError:
          print("Enter valid number")
          continue
        else:
          if player.coins < choice*5:
            print("come back with more money")
          else:
            player.coins -= choice*5
            player.maxmana += choice
            print("your max mana increased by {}".format(choice))
            break
      print("Continue shopping? [Yes, No]")
      cmd1 = input().lower()
      if cmd1 not in ['yes', 'no']:
        print("say what")
      elif cmd1 == "yes":
        pass
      else:
        return        



def player_turn(player, enemy_list):

  """
  This is the player turn. ends when mana <= 0 or enemies <= 0
  """
  print(start_divider)
  print("{}'s turn".format(player.name))
  print(start_divider)
  options = [  ]
  display = display_options(options)
  player.mana = player.maxmana

  #initializes enemies as objects
  enemy_names = []
  for enemy in enemy_list:
    enemy_names.append(enemy.name)
  ended = False
  
  while not ended:
    
    checks(player, enemy_list)
    print(divider)
    get_player_status(player)
    print(divider)
    print("Enemies:")
    print(small_divider)
    print_enemies(enemy_list)
    print(divider)
    player.print_hand()
    print(divider)
    print(display)
    cmd = input().lower()
    if cmd in player.hand:
      if not valid_mana(player, cmd):
        not_enough_mana(player, cmd)
      else:
        card_play(player, enemy_list, cmd)
    elif cmd == 'end_turn':
      ended = True
      print(reject_divider)
      print("Turn ended")
      print(reject_divider)
      
    elif cmd == 'inspect':
      print("Choose an enemy to inspect:")
      print_enemies(enemy_list)
      print("input 'all' for all enemies")
      while True:
        i_cmd = input().lower()
        if i_cmd not in enemy_names and i_cmd != 'all':
          print("You really don't like to listen, do you?")
          sleep(0.5)
        elif i_cmd in enemy_names:
          index = enemy_names.index(i_cmd)
          get_description(enemy_list[index])
          break
        elif i_cmd == 'all':
          for enemy in enemy_list:
            get_description(enemy)
          break
    elif cmd == 'card_descriptions':
      print(divider)
      for card in player.hand:
        o_card = class_cards[player.cls]
        o_card[card].description()
    elif cmd == 'play_card':
      while True:
        print("Choose a card to play")
        chosen_card = input().lower()
        if chosen_card not in player.hand:
          print("Stop trying to make shit up")
          sleep(0.5)
        elif not valid_mana(player, chosen_card):
          not_enough_mana(player, chosen_card)
          break
        else:
          card_play(player, enemy_list, chosen_card)
          break
    else:
      print("Choose one of the options oh my ****")
      sleep(0.5)
  player.conditions = update_conditions(player.conditions)
            

        
def enemy_turn(player, enemy_list):
  print(start_divider)
  print("The enemies have started their turn")
  print(start_divider)
  for enemy in enemy_list:
    move = enemy.moveset[randint(0, len(enemy.moveset)-1)]
    card_played(enemy, player, move)
    enemy.conditions = update_conditions(enemy.conditions)

def swap_turn(actor):
  """
  returns a boolean value, True for player, False for enemies
  """
  return not actor

        
def combat(player, stage_power):
  enemy_list = spawn_enemies(stage_power)
  turn = True
  fighting = True
  player.start_combat()
  player.start_draw()
  player_turn(player, enemy_list)
  turn = swap_turn(turn)
  while fighting:
    if enemy_list == []:
      break
    if defeated(player):
      return death()
    elif turn:
      player.draw_card(1)
      player_turn(player, enemy_list)
      turn = swap_turn(turn)
    else:
      enemy_turn(player, enemy_list)
      turn = swap_turn(turn)
  choose_card_reward(player)
  return

def spawn_enemies(stage_power):
  """
  The thought process behind this is that, the total power of the enemies are levelled according to the stage level (4 + stage). Then, we choose enemies of random power level until the total power has been reached.
  returns a list of enemies
  """
  enemy_list = []
  if stage_power == 9:
      enemy_list.append(deepcopy(snails['snailarchon']))
      return enemy_list
  else:
    while stage_power > 0:
      rand_snail = snail_list[randint(0, len(snail_list)-1)]
      if stage_power < snails[rand_snail].powerlevel:
        pass
      else:
        enemy = snails[rand_snail]
        enemy_list.append(deepcopy(enemy))
        stage_power -= snails[rand_snail].powerlevel
    return enemy_list
                      

def card_play(actor, enemy_list, card):
  target = 'single'
  card_obj = get_card_object(actor, card)
  if 'atk' in card_obj.types:
    for effect in card_obj.effect:
      if effect['target'] == 'all':
        target = 'all'
      break
    if target == 'all':
      for enemy in enemy_list:
        card_played(actor, enemy, card)
      mana_deduction(actor, card)
      actor.discard_card(card)
    else:
      tgt = get_target(choose_target(enemy_list), enemy_list)
      if tgt == None:
        return
      card_played(actor, tgt, card)
      mana_deduction(actor, card)
      actor.discard_card(card)
  else:
    add_block(actor, card_obj)
    actor.add_conditions(card_obj)
    actor.discard_card(card)
    
def card_played(actor, enemy, card):
  card_obj = get_card_object(actor, card)
  for effect in card_obj.effect:
    if effect['target'] == 'player':
      actor.add_conditions(card_obj)
    elif effect['target'] == 'enemy':
      enemy.add_conditions(card_obj)
  blocked = add_block(actor, card_obj)
  apply_conditions(actor)
  apply_conditions(enemy)
  damage = deal_damage(actor, enemy, card_obj)
  reset_conditions(actor)
  reset_conditions(enemy)
  print_attack(actor, enemy, card, damage)
  return
      

"""DEPRECATED FUNCTION
def add_effect(actor, effect):
  if effect['action'] == 'deals':
    actor.damagemult = actor.damagemult*effect['value']
  elif effect['action'] == 'receives':
    actor.takedamagemult = actor.takedamagemult*effect['value']
  elif effect['action'] == 'draw':
    actor.draw_card(effect['value'])
  elif effect['action'] == 'discard':
    actor.discard_card(effect['value'])
  elif effect['action'] == 'gains':
    actor.damage += effect['value']
  return
  """

def choose_target(enemy_list):
  while True:
    print(divider)
    enemy_names = print_enemies(enemy_list)
    print("choose an enemy or 'back' to go back")
    enemy_chosen = input()
    if enemy_chosen == 'back':
      return None
    elif enemy_chosen not in enemy_names:
      print("You have chosen an invalid target")
    else:
      return enemy_chosen
      
def deal_damage(actor, enemy, card):
  damage_done = max(((actor.damage + card.damage)*actor.damagemult)*enemy.takedamagemult - enemy.block, 0)
  enemy.block = max(enemy.block - ((actor.damage + card.damage)*actor.damagemult)*enemy.takedamagemult, 0)
  enemy.hp = enemy.hp - damage_done
  return damage_done

def get_target(str, enemy_dict):
  target = None
  if str == None:
    return None
  for enemy in enemy_dict:
    if enemy.name.lower() == str.lower():
      target = enemy
      return target

def valid_mana(actor, card):
  card_obj = get_card_object(actor, card)
  return actor.mana >= card_obj.mana

def mana_deduction(actor, card):
  card_obj = get_card_object(actor, card)
  actor.mana = actor.mana - card_obj.mana
  return

def ended(enemy_list):
  return enemy_list == []

def defeated(actor):
  dead = actor.hp <= 0
  if dead:
    print("{} has died on the battlefield".format(actor.name))
  return dead

def remove_from_combat(actor, enemy_list):
  enemy_list.remove(actor)
  return

def checks(player, enemy_list):
  for enemy in enemy_list:
    if defeated(enemy):
      remove_from_combat(enemy, enemy_list)
      player.coins += enemy.coins
  return ended(enemy_list)

def update_conditions(conditions_dict):
  new_conditions = {}
  for condition in conditions_dict.keys():
    if conditions_dict[condition] == 0:
      pass
    else:
      new_conditions[condition] = conditions_dict[condition] - 1
  return new_conditions

def add_block(actor, card_obj):
  actor.block += card_obj.block
  print("added {} to {}'s' block".format(card_obj.block, actor.name))
  sleep(0.5)
  print("{} now has {} block".format(actor.name, actor.block))
  sleep(0.5)
  return

def apply_conditions(actor):
  for cond in actor.conditions.keys():
    conditions_dict[cond](actor)
  return

def reset_conditions(actor):
  actor.damage = 0
  actor.takedamagemult = 1
  actor.damagemult = 1
  return
    
def death():
  options = ['yes', 'no']
  display = display_options(options)
  print(game_end)
  print("Would you like to start again?")
  print(options)
  choice = input()
  if choice not in options:
    print("u are dead stop trying things")
  elif choice == 'yes':
    return start_game()
  elif choice == 'no':
    return main()

def start_game():
  player = choose_class()
  player.name = input("What is your name adventurer?\n")
  player.start_deck()
  stage_count = 1
  while True:
    if stage_count < 10 and stage_count % 2 == 1:
      story_list[stage_count // 2]()
    stage_count += choose_stage(player, stage_count)
    print(stage_divider)
    print("You move on to the next stage")
    print(stage_divider)
