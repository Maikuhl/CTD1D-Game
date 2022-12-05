"""
TODO:
make sure the cards with no attack don't need to have an attack prompt
"""

import re
from random import randint
from characterclasses import *
from terminalprints import divider, debugger
import time

class Card():
  
  def __init__(self, damage, block, mana, name, effect_ls):
    """
    initializes the card
    """
    self.damage = damage
    self.block = block
    self.mana = mana
    self.name = name
    self.effect_ls = effect_ls
    self.effect_description = self.get_effect_description(effect_ls)
    self.effect = self.define_effect(effect_ls)
    self.effectandtags = self.get_effect_tags()
    self.price = 2*self.mana
    self.types = self.get_card_type()

  def get_effect_description(self, effect_ls):
    effect_description = ""
    for effect in effect_ls:
      effect_description += effectdict[effect][0]
    return effect_description
    
    
  def description(self):
    """
    Describes the card, displays mana requirement, damage, block, and its effects
    """
    print("{}:".format(self.name))
    print("Uses {} mana".format(self.mana))
    if self.damage != 0:
      print("Deals {} damage".format(self.damage))
    if self.block != 0:
      print("Blocks {} damage".format(self.block))
    if self.effect_ls != []:
      print("{}".format(self.effect_description))
    print(divider)
    return

  def define_effect(self, effect_ls):
    """
    returns a list of effects that should be applied when the card is played.
    each item is a dictionary
    [{'target': target, 'action': action, 'value': value}, ...]
    """
    tag_list = []
    for effect in effect_ls:
      effectsplit = effectdict[effect][0].split(",")
      for one_effect in effectsplit:
        effectwords = effectdict[effect][0].split(" ")
        tags = {'target': None}
        for word in effectwords:
          if word in ['enemy', 'player', 'all']:
            tags['target'] = word
        tag_list.append(tags)
    return tag_list

  def get_effect_tags(self):
    effect_tag_dict = {}
    for effect in self.effect_ls:
      effect_tag_dict[effect] = effectdict[effect][1]
    return effect_tag_dict

  def get_card_type(self):
    type_list = []
    if self.effect_ls != []:
      for effect in self.effect_ls:
        type_list.append(effect)
    if self.block != 0:
      type_list.append('blk')
    if self.damage != 0:
      type_list.append('atk')
    return type_list


effectdict = {'all': ['all enemies receive damage', {'condition': False, 'turns': 0}],
             'flex': ['player deals 1 extra damage', {'condition': True, 'turns': 3}],
             'twice': ['player deals 200% damage', {'condition': False, 'turns': 0}],
             'calm': ['player receives 50% damage', {'condition': True, 'turns': 3}],
             'wrath': ['player deals 200% damage, player receives 200% damage', {'condition': True, 'turns': 3}],
             'exit stance': ['player deals 100% damage, player receives 100% damage', {'condition': True, 'turns': 0}],
             'vulnerable': ['enemy receives 150% damage', {'condition': True, 'turns': 2}],
             'weak': ['enemy deals 50% damage', {'condition': True, 'turns': 2}],
             'drain': ['player receives 3 damage, player gains 2 mana', {'condition': False, 'turns': 0}],
             'poison': ['enemy receives 3 damage for 5 turns', {'condition': True, 'turns': 5}],
             'gain mana': ['player gains 1 mana', {'condition': False, 'turns': 0}],
             'copy': ['player copy 1 card', {'condition': False, 'turns': 0}],
             'snailritual': ['player gains 1 strength', {'condition': True, 'turns': 1}],
             'snailgrow': ['player gains 1 strength', {'condition': True, 'turns': 1}],
             'snailweak': ['enemy deals 75% damage', {'condition': True, 'turns': 2}],
             'snailspit': ['player shuffles lick into discard pile', {'condition': False, 'turns': 0}]}

tankcardsdict = {'bash': Card(8, 0, 2, 'Bash',['vulnerable']),
             'strike': Card(6, 0, 1, 'Strike', []),
             'anger': Card(6, 0, 0, 'Anger', ['copy']),
             'body slam': Card(10, 0, 1, 'Body slam', []),
             'cleave': Card(8, 0, 1, 'Cleave', ['all']),
             'headbutt': Card(9, 0, 1, 'Headbutt', ['copy']),
             'defend': Card(0, 5, 1, 'Block', []),
             'flex': Card(0, 0, 0, 'Flex', ['flex']),
             'shrug it off': Card(0, 8, 1, 'Shrug it off', []),
             'true grit': Card(0, 7, 1, 'True grit', []),
             'bloodletting': Card(0, 0, 2, 'BloodLetting', ['drain']),
             'disarm': Card(0, 0, 1, 'Disarm',['weak']),
             'dual wield': Card(0, 0, 1, 'Dual wield', ['copy']),
             'flame barrier': Card(4, 12, 2, 'Flame barrier', []),
             'entrench': Card(0, 0, 1, 'Entrench', ['calm']),
             'clash': Card(14, 0, 3, 'Clash', ['all'])}

magecardsdict = {'erupt': Card(9, 0, 2, 'Erupt', ['wrath']),
             'strike': Card(6, 0, 1, 'Strike', []),
             'vigilance': Card(0, 8, 0, 'Vigilance', ['calm']),
             'crush joints': Card(10, 0, 1, 'Crush joints',['vulnerable']),
             'consecrate': Card(5, 0, 0, 'Consecrate', ['all']),
             'cut through fate': Card(7, 0, 1, 'Cut through fate', []),
             'empty body': Card(0, 7, 1, 'Empty body', ['exit stance']),\
             'empty fist': Card(7, 0, 1, 'Empty fist', ['exit stance']),
             'empty mind': Card(0, 0, -1, 'Empty mind', ['exit stance']),
             'evaluate': Card(0, 0, 1, 'Evaluate', []),
             'follow up': Card(7, 0, 1, 'Follow up', ['gain mana']),
             'pressure points': Card(8, 0, 1, 'Pressure points', ['all']),
             'fasting': Card(0, 0, 3, 'Fasting', ['wrath']),
             'fear no evil': Card(8, 0, 1, 'Fear no evil', ['calm']),
             'inner peace': Card(0, 0, 1, 'Inner peace', ['calm']),
             'conclude': Card(14, 0, 3, 'Conclude', ['all'])}

roguecardsdict = {'neutralise': Card(5, 0, 1, 'Neutralise', ['weak']),
             'strike': Card(6, 0, 1, 'Strike', []),
             'survivor': Card(0, 8, 0, 'Survivor', []),
             'acrobatics': Card(0, 0, 1, 'Acrobatics',[]),
             'backflip': Card(0, 5, 1, 'Backflip', []),
             'bane': Card(7, 0, 1, 'Bane', ['poison']),
             'dagger spray': Card(4, 0, 1, 'Dagger Spray', ['twice']),
             'dagger throw': Card(7, 0, 1, 'Dagger throw', []),
             'deadly poison': Card(5, 0, 1, 'Deadly poison', ['poison']),
             'deflect': Card(0, 4, 1, 'Deflect', []),
             'dodge and roll': Card(0, 4, 1, 'Dodge and roll', ['twice']),
             'flying knee': Card(8, 0, 1, 'Flying knee', ['gain mana']),
             'outmaneuver': Card(0, 0, 1, 'Outmaneuver', ['gain mana']),
             'piercing wail': Card(10, 0, 2, 'Piercing wail', ['weak']),
             'poisoned stab': Card(6, 0, 1, 'Poisoned stab', ['poison']),
             'all out attack': Card(14, 0, 3, 'All out attack', ['all'])}

enemycardsdict = {'snail strike': Card(6, 0, 0, 'Snail Strike', []),
                 'incantation': Card(0, 0, 0, 'Snail Incantation', ['snailritual']),
                 'chomp': Card(11, 0, 0, 'Snail Chomp', []),
                 'thrash': Card(7, 5, 0, 'Snail Thrash', []),
                 'bellow': Card(3, 6, 0, 'Snail Bellow', []),
                 'grow': Card(0, 0, 0, 'Snail Grow', ['snailgrow']),
                 'tacklemacid': Card(10, 0, 0, 'Snail Tackle', []),
                 'tacklesacid': Card(3, 0, 0, 'Snail Tackle', []),
                 'lick': Card(0, 0, 0, 'Snail Lick', ['snailweak']),
                 'corrosivespit': Card(7, 0, 0, 'Corrosive Spit', ['snailspit']),
                 'tacklesspike': Card(5, 0, 0, 'Tackle', []),
                 'spiketackle': Card(8, 0, 0, 'Spike Tackle', ['snailspit']),
                 'torntosnails': Card(15, 0, 0, 'Torn to Snails!', ['twice']),
                 'iwillhaveshell': Card(3, 8, 0, 'I will have shell', ['snailgrow']),
                 'snailspace': Card(8, 3, 0, "Snail Space!", ['snailweak'])}

class_cards = {'tank': tankcardsdict, 'mage': magecardsdict, 'rogue': roguecardsdict, 'enemy':enemycardsdict}

def get_card_object(actor, card):
  if actor.type == 'enemy':
    return enemycardsdict[card]
  else:
    class_cards = get_class_cards()
    return class_cards[actor.cls][card]

def not_enough_mana(player, card):
  card_obj = get_card_object(player, card)
  print("")
  print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
  print("It requires {} mana to play that card, you have {} mana".format(card_obj.mana, player.mana))
  print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
  print("")
  time.sleep(2)
  return

def get_class_cards():
  class_cards = {'tank': get_tankcardsdict(), 'mage': get_magecardsdict(), 'rogue': get_roguecardsdict()}
  return class_cards

def get_tankcardsdict():
  return tankcardsdict

def get_magecardsdict():
  return magecardsdict

def get_roguecardsdict():
  return roguecardsdict

def get_enemycardsdict():
  return enemycardsdict

def get_description(snail):
  enemycardsdict = get_enemycardsdict()
  print(divider)
  print("{}:".format(snail.name))
  print(divider)
  print("{} Health / Level {} / drops {} coins on defeat".format(snail.hp, snail.powerlevel, snail.coins))
  for move in snail.moveset:
    enemycardsdict[move].description()
  return

def flex(actor):
  actor.damage += 1
  return

def twice(actor):
  actor.conditions['twice'] = 0
  actor.damagemult *= 2
  return

def calm(actor):
  new_dict = {}
  conditions = list(actor.conditions)[::-1]
  for condition in conditions:
    if condition in ['exit stance', 'wrath']:
      actor.conditions[condition] = 0
    else:
      new_dict[condition] = actor.conditions[condition]
  actor.conditions['calm'] = 3
  actor.takedamagemult *= 0.5
  return

def wrath(actor):
  new_dict = {}
  conditions = list(actor.conditions)[::-1]
  for condition in conditions:
    if condition in ['exit stance', 'calm']:
      actor.conditions[condition] = 0
    else:
      new_dict[condition] = actor.conditions[condition]
  actor.conditions['wrath'] = 7
  actor.conditions = new_dict
  actor.takedamagemult *= 2
  actor.damagemult *= 2
  return

def exit_stance(actor):
  new_dict = {}
  conditions = list(actor.conditions)[::-1]
  for condition in conditions:
    if condition in ['wrath', 'calm']:
      actor.conditions[condition] = 0
    else:
      new_dict[condition] = actor.conditions[condition]
  actor.conditions['exit stance'] = 0
  actor.takedamagemult = 1
  actor.damagemult = 1
  return

def vulnerable(actor):
  actor.takedamagemult *= 1.5
  return

def weak(actor):
  actor.damagemult *= 0.5
  return

def poison(actor):
  actor.hp -= 3*actor.takedamagemult
  return

def snail_ritual(actor):
  actor.damage += 1
  return

def snail_grow(actor):
  actor.damage += 1
  return

def snail_weak(actor):
  actor.damagemult *= 0.75
  return

def drain(actor):
  actor.hp -= 3
  actor.mana += 2
  return

def gain_mana(actor):
  actor.maxmana += 1
  return

def copy(actor):
  while True:
    print("Choose a card to copy")
    chosen_card = input().lower()
    if chosen_card not in actor.hand:
      print("Stop trying to make shit up")
    else:
      actor.hand.append(chosen_card)
      break
  return

def snail_spit(actor):
  actor.graveyard.append('lick')
  return


conditions_dict = {'flex': flex,
                  'twice': twice,
                  'calm': calm,
                  'wrath': wrath,
                  'exit stance': exit_stance,
                  'vulnerable': vulnerable,
                  'weak': weak,
                  'poison': poison,
                  'snailritual': snail_ritual,
                  'snailgrow': snail_grow,
                  'snailweak': snail_weak,
                  'drain': drain,
                  'gain mana': gain_mana,
                  'copy': copy,
                  'snailspit': snail_spit}
  