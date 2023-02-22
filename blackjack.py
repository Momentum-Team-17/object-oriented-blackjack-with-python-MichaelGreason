import random

SUITS = ['♥', '♣️', '♠️', '♦']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'


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

    def view_cards(self):
        for card in self.hand:
            print(card)

    def calculate(self):
        card_value = 0
        score = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                card_value = 10
            # elif card.rank == 'A':
            #     value_choice = input("Do you want 1 or 11? ")
            #     if value_choice == '1':
            #         card_value = 1
            #     elif value_choice == '11':
            #         card_value = 11
            #     else:
            #         "This is not applicable"
            elif card.rank == 'A':
                if score >= 11:
                    card_value = 1
                else:
                    card_value = 11
            else:
                card_value = card.rank
            score += card_value
        print('Score: ', score)
        return score


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

    def player_turn(self):  # player decides how many times to hit before playig
        choice = input('Hit or Check? ')
        if choice == "Hit":
            card = self.deck.cards.pop()
            self.player.hand.append(card)
            print(f'{self.player.name}s hand is ')
            self.player.view_cards()
        else:
            print(f'{self.player.name} chose to stay, Dealers turn ')

    def dealer_turn(self):
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        print('Dealer hand is ')
        self.dealer.view_cards()

    def deal(self):
        self.setup()
        self.deck.shuffle()
        print(new_game.player)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        print(f'{self.player.name}s hand is ')
        self.player.view_cards()
        print(new_game.dealer)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        print('Dealer hand is ')
        self.dealer.view_cards()
        
    def win_lose(self):
        while self.player.calculate():
            


new_game = Game()
new_game.deal()
new_game.player_turn()
new_game.player.calculate()
new_game.dealer_turn()
new_game.dealer.calculate()
