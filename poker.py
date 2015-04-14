import random


def gen_deck():
    houses = ['S', 'C', 'H', 'D']
    cards = ['0' + str(i) if len(str(i)) == 1 else str(i)
             for i in range(2, 11)]
    cards.extend(ord(face_card) for face_card in ['K', 'Q', 'J', 'A'])
    deck = []
    for house in houses:
        deck.extend([int(str(ord(house)) + str(card)) for card in cards])

    return deck


def read_card(card):
    card = str(card)
    house = chr(int((card[0:2])))
    num = card[2:]
    num = int(num) if int(num) <= 10 else chr((int(num)))
    houses = {'S': 'Spades', 'C': 'Clubs', 'H': 'Hearts', 'D': 'Diamonds'}
    return str(num) + ' of ' + houses[house]


class Player(object):

    def __init__(self):
        self.main_key = random.randint(0, 1000)
        self.ind_keys = [random.randint(1, 1000) for i in range(1, 55)]

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
        other_keys = []
        self_keys = []
        for choice in choices:
            other_keys.append(p.ind_keys[choice])
            self_keys.append(self.ind_keys[choice])
            chosen_cards.append(
                deck[choice] / (self.ind_keys[choice] * p.ind_keys[choice]))
        return chosen_cards

    def shuffle_deck(self, deck):
        random.shuffle(deck)
        return deck


deck = gen_deck()
cards = [read_card(card) for card in deck]

print "\n###  The cards are in the deck are:\n"
print cards

print "\n\n###  We represent them as such so that integer operations can be performed on them.\n"
print deck


alice = Player()
bob = Player()

deck = alice.enc_deck_main(deck)
deck = alice.shuffle_deck(deck)
print "\n\n###  This is how the deck looks like after Alice has encrypted and shuffled it. Bob can't make sense of the deck in this state\n"
print deck


deck = bob.enc_deck_main(deck)
deck = bob.shuffle_deck(deck)
print "\n\n###  This is how the deck looks like after Bob has encrypted and shuffled it. Neither Bob nor Alice can make sense of the deck in this state.\n"
print deck


deck = alice.dec_deck_main(deck)
deck = alice.enc_deck_ind(deck)
print "\n\n###  Alice decrypts the cards and encrypts them individually. Neither Bob nor Alice can make sense of the deck in this state.\n"
print deck

deck = bob.dec_deck_main(deck)
deck = bob.enc_deck_ind(deck)
print "\n\n###  Bob decrypts the cards and encrypts them individually. Neither Bob nor Alice can make sense of the deck in this state.\n"
print deck

alice_choices = input("###  Which cards does alice pick? \n")
print "\n###  The cards selected after a secure shuffle are:\n"
print [read_card(card) for card in alice.card_request(bob, alice_choices)]
