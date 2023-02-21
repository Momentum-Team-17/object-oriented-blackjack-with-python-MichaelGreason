import random

SUITS = ['♥', '♣️', '♠️', '♦']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'

    # def __repr__(self):
    #     return f'{self.rank}{self.suit}'


class Deck:

    def __init__(self):
        self.cards = []

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self):
        self.name = input("What is your name? ")
        self.hand = []

    def __str__(self):
        return f'{self.name} is the player'

    def turn(self):  # player decides how many times to hit before playig
        pass


class Dealer(Player):
    # inherits from Player
    def __init__(self):
        self.name = "Dealer"
        self.hand = []

    def __str__(self):
        # when we write cariables and methods with the same
        # as the parent class, they override the code from
        # the parent class (Player)
        return f'{self.name} is the dealer'

    def turn(self):
        # unlike player, dealer follows the house rules
        pass

    def end_game(self):
        pass


class Game:
    def __init__(self):
        self.player = Player()
        # the value of self.player is an instance of the class Player
        self.dealer = Dealer()
        self.setup()

    def setup(self):
        self.deck = Deck()  # calls line 13, creates a deck
        self.deck.add_cards()  # calls line 16, adds cards to the deck
        # calls the __str__ method to be called for each card

    def deal(self):
        self.setup()
        self.deck.shuffle()
        print(new_game.player)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        print(f'{self.player.name}s hand is ')
        for card in new_game.player.hand:
            print(card)
        print(new_game.dealer)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        print('Dealer hand is ')
        for card in new_game.dealer.hand:
            print(card)


new_game = Game()
new_game.deal()
# for card in new_game.deck.cards:
#     print(card)
# created the game and the deck with cards
