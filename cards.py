from collections import OrderedDict as odict
import random
from unicards import unicard

class Deck:

	class print_type:
		minimal 	= 0
		textual 	= 1
		graphical	= 2
	
	values = odict([(u'➁','Two'), (u'➂','Three'), (u'➃','Four'), (u'➄','Five'), (u'➅','Six'), (u'➆','Seven'),
	(u'➇','Eight'), (u'➈','Nine'), (u'➉','Ten'), (u'Ⓙ','Prince'), (u'Ⓠ','Queen'), (u'Ⓚ','King'), (u'Ⓐ','Ace')])
	
	shapes = {'♠':'Spades', '♡':'Hearts', '♢':'Diamonds', '♣':'Clubs'}
	
	def _get_deck():
		deck = []
		for shape in Deck.shapes.keys():
			for val in Deck.values:
				deck.append((val, shape))
		return deck
		
	def get_card_name(card):
		temp = Deck.values[card[0]]
		temp += ' of '
		temp += Deck.shapes[card[1]]
		return temp
	
	def get_unicard(card):
		def get_val(symbol):
			if ord(symbol) == 10121:
				return 'T'
			elif 9398 <= ord(symbol) <= 9414:
				return chr(ord(symbol) - 9333) 
			else:
				return chr(ord(symbol) - 0x274f)
		temp = get_val(card[0])
		temp += Deck.shapes[card[1]][0]
		return unicard(temp)
		
		
		
		

	def __init__(self, cards=None):
		self.cards = Deck._get_deck() if cards == None else cards
		
	def shuffle(self, times=1):
		for x in range(times):
			random.shuffle(self.cards)
			
	def print_deck(self, printType=print_type.minimal):
		ops = [lambda x: print(x), lambda x: print(Deck.get_card_name(x)), lambda x: print(Deck.get_unicard(x))]
		op = ops[printType]
		
		for x in self.cards:
			op(x)
			
	def split_to_half(self):
		return self.cards[0 : len(self.cards) / 2], self.cards[len(self.cards) / 2 : len(self.cards)]
