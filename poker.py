import random

def gen_deck():
	houses = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
	cards = [str(i) for i in range(2, 11)]
	cards.extend(['K', 'Q', 'J', 'A'])
	deck = []
	for house in houses:
		deck.extend([house + ' ' + card for card in cards])
	deck = range(1,55)  # temp fix
	return deck


class Player(object):

	def __init__(self):
		self.main_key = random.randint(0, 100000000)
		self.ind_keys = [random.randint(1,100000000) for i in range(1,55)]

	def enc_deck_main(self, deck):
		new_deck = []
		for card in deck:
			new_deck.append(card * self.main_key)
		return new_deck

	def enc_deck_ind(self, deck):
		new_deck = []
		for i in range(len(deck)):
			new_deck.append(deck[i] * self.ind_keys[i])
		return new_deck

	def dec_deck_main(self, deck):
		new_deck = []
		for card in deck:
			new_deck.append(card / self.main_key)
		return new_deck

	def card_request(self, p, choices):
		chosen_cards = []
		other_keys=[]
		self_keys = []
		for choice in choices:
			other_keys.append(p.ind_keys[choice])
			self_keys.append(self.ind_keys[choice])
			chosen_cards.append(deck[choice] / (self.ind_keys[choice] * p.ind_keys[choice]))
		print chosen_cards

	def shuffle_deck(self, deck):
		random.shuffle(deck)
		return deck


deck = gen_deck()
print deck

alice = Player()
bob = Player()

deck = alice.enc_deck_main(deck)
deck = alice.shuffle_deck(deck)
print deck

deck = bob.enc_deck_main(deck)
deck = bob.shuffle_deck(deck)
print deck

deck = alice.dec_deck_main(deck)
deck = alice.enc_deck_ind(deck)
print deck

deck = bob.dec_deck_main(deck)
deck = bob.enc_deck_ind(deck)
print deck

alice_choices = input("Which cards does alice pick? ")
alice.card_request(bob, alice_choices)
