"""
TODO:
add a working conditions function
"""
from cardclass import *
from random import *
from cardclass import *
from enemyclass import *
from time import sleep

class Character():
  """
  use in the sense of:
  player = Character([class, health, mana, unique_starting_relic])
  """
  
  def __init__(self, stats):
    """
    initializes the player according to the class he has chosen
    """
    self.cls_display = stats[0]
    self.cls = stats[0].lower()
    self.maxhp = stats[1]
    self.hp = stats[1]
    self.maxmana = stats[2]
    self.mana = stats[2]
    self.block = 0
    self.damage = 0
    self.damagemult = 1
    self.takedamagemult = 1
    self.relics = [stats[3]]
    self.conditions = {}
    self.deck = []
    self.deckinplay = []
    self.graveyard = []
    self.hand = []
    self.coins = 0
    self.type = 'player'
    self.name = None
    
  def start_deck(self):
    """
    gives the starting cards to the player
    """
    if self.cls == 'tank':
      for i in range(5):
        self.deck.append('strike')
      for i in range(4):
        self.deck.append('defend')
      self.deck.append('bash')
    elif self.cls == 'mage':
      for i in range(4):
        self.deck.append('strike')
        self.deck.append('empty body')
      self.deck.append('erupt')
      self.deck.append('vigilance')
    elif self.cls == 'rogue':
      for i in range(5):
        self.deck.append('strike')
        self.deck.append('dodge and roll')
      self.deck.append('survivor')
      self.deck.append('neutralise')
      
  def start_draw(self):
    """
    draws the first five cards for a combat stage
    """
    self.deckinplay = self.deck[:]
    for i in range(5):
      card_to_add = self.deckinplay[randint(0, len(self.deckinplay)-1)]
      self.hand.append(card_to_add)
      self.deckinplay.remove(card_to_add)
    return
    
  def draw_card(self, value):
    if self.deckinplay == []:
      self.deckinplay = self.graveyard[:]
      self.graveyard = []
    for i in range(value):
      card_to_add = self.deckinplay[randint(0, len(self.deckinplay)-1)]
      self.hand.append(card_to_add)
      self.deckinplay.remove(card_to_add)
      sleep(0.5)
      print("You draw {}".format(card_to_add))
      sleep(0.5)
    return

  def discard_card_rand(self, value):
    for i in range(value):
      card_to_remove = self.hand[randint(0, len(self.deckinplay)-1)]
      self.hand.remove(card_to_remove)
      self.graveyard.append(card_to_remove)

  def discard_card(self, card):
    self.hand.remove(card)
    self.graveyard.append(card)
    return

  def print_hand(self):
    """
    displays the player's hand
    """
    print("This is your hand:")
    print(self.hand)
    return
    
  def start_combat(self):
    self.conditions = {}
    self.block = 0
    self.hand = []
    self.graveyard = []
    self.deckinplay = self.deck[:]
    return

  def add_conditions(self, card_obj):
    for condition, tags in card_obj.effectandtags.items():
      if condition not in self.conditions.keys():
        self.conditions[condition] = tags['turns']
      else:
        self.conditions[condition] += tags['turns']
      return

    
classes = {'tank': Character(['Tank', 80, 3, 'Burning Blood']), 'mage': Character(['Mage', 72, 4, 'Pure Water']), 'rogue': Character(['Rogue', 70, 3, 'Ring of the Snake'])}