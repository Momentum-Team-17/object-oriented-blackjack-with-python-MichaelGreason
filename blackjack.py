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
        print('Player score: ', score)
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
        print('Dealer score: ', score)
        return score


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
        self.player.view_cards()
        print(new_game.dealer)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        print('Dealer hand is ')
        self.dealer.view_cards()

    def player_turn(self, stay):  # player decides how many times to hit before playing
        choice = input('Hit or Check? ')
        player_score = self.player.calculate()
        if player_score < 21:
            if choice == "Hit":
                card = self.deck.cards.pop()
                self.player.hand.append(card)
                print(f'{self.player.name}s hand is ')
                self.player.view_cards()
            else:
                print(f'{self.player.name} chose to stay, Dealers turn ')
                stay = True
        elif player_score > 21:
            print('Bust!')
        return self.player.calculate(), stay

    def dealer_turn(self):
        card = self.deck.cards.pop()
        dealer_score = self.dealer.calculate()
        if dealer_score < 21:
            if self.dealer.calculate() < 17:
                self.dealer.hand.append(card)
                print('Dealer hand is ')
                self.dealer.view_cards()
        elif self.dealer.calculate() > 21:
            print('Dealer bust! You win!')
        return self.dealer.calculate()

    def turn_take(self):
        p_score = 0
        d_score = 0
        stay = False
        while p_score < 21 and not stay:
            p_score, stay = self.player_turn(stay)
        if p_score > 21:
            print('Bust! You lose.')
            return
        while d_score < 17:
            d_score = self.dealer_turn()
        print('Player score: ', p_score)
        print('Dealer score: ', d_score)

    def game_over(self):
        player_score = self.player.calculate()
        dealer_score = self.dealer.calculate()
        if player_score < 21:
            if player_score > dealer_score:
                print('You win!')
            elif dealer_score < 21:
                print('You Lose')
        elif player_score > 21:
            print("Bust! You lose!")
        elif dealer_score < 21:
            if player_score < dealer_score:
                print('You Lose')
            else:
                print('You win!')
        elif dealer_score > 21:
            print('Dealer bust! You Win!')


new_game = Game()
new_game.deal()
new_game.turn_take()
new_game.game_over()
