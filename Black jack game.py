import random
import time

suits = ('Hearts', 'Diamond', 'Spade', 'Club')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


def chips(name):
    total_chips = 100
    a = True
    while a:
        bet = int(input(f'{name} how many chips you want to bet:'))
        if bet < total_chips:
            total_chips -= bet
            print(f"chips left:{total_chips}")
            a = False
        else:
            print("Sorry! you don't have enough chips to bet")
            print(f"you have {total_chips} chips")


def game_play():
    name = input("\nEnter the name of the player:")
    chips(name)
    deck = Deck()
    deck.shuffle()
    player_card = Hand()
    player_card.add_card(deck.deal())
    player_card.add_card(deck.deal())
    player_card.adjust_for_ace()
    print("\n\t\tPLAYER'S CARDS:")
    for card in player_card.cards:
        print(card)
    print("\n\t\tPLAYER'S SCORE:", end=" ")
    print(player_card.value)

    dealer_card = Hand()
    dealer_card.add_card(deck.deal())
    dealer_card.add_card(deck.deal())
    dealer_card.adjust_for_ace()
    print("\n\t\tDEALER'S CARDS:")
    print("(CARD HIDDEN)")
    print(dealer_card.cards[1])
    print("\n\t\tDEALER'S SCORE:", end=" ")
    print(dealer_card.value - dealer_card.cards[0].value)

    while player_card.value < 21:
        choice = input("\npress H to hit and S to stand:")
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("you entered the wrong choice..")
        if choice.upper() == 'H':
            player_card.add_card(deck.deal())
            player_card.adjust_for_ace()
            print("\n\t\tPLAYER'S CARDS:")
            for card in player_card.cards:
                print(card)
            print("\n\t\tPLAYER'S SCORE:", end=" ")
            print(player_card.value)
            print("\n\t\tDEALER'S CARDS:")
            print("(CARD HIDDEN)")
            print(dealer_card.cards[1])
            print("\n\t\tDEALER'S SCORE:", end=" ")
            print(dealer_card.value - dealer_card.cards[0].value)

        if choice.upper() == 'S':
            break

    print("\n\t\tPLAYER'S CARDS:")
    for card in player_card.cards:
        print(card)
    print("\n\t\tPLAYER'S SCORE:", end=" ")
    print(player_card.value)
    print("\nDealer is revealing it's card ", end='')
    time.sleep(2)
    print(". .", end=" ")
    time.sleep(2)
    print(". .", end=" ")
    time.sleep(2)
    print(". .")
    print("\n\t\tDEALER'S CARDS:")
    for card in dealer_card.cards:
        print(card)
    print("\n\t\tDEALER'S SCORE:", end=" ")
    print(dealer_card.value)

    if player_card.value == 21:
        print("\n Player has a BLACKJACK")
        print(f"{name} you won !!!")
        quit()

    if player_card.value > 21:
        print("\nPlayer Busted !!!")
        print("Dealer won the game.....")
        quit()

    while dealer_card.value < 17:
        print("\nDealer hit a card !!!")
        dealer_card.add_card(deck.deal())
        dealer_card.adjust_for_ace()
        print("\n\t\tPLAYER'S CARDS:")
        for card in player_card.cards:
            print(card)
        print("\n\t\tPLAYER'S SCORE:", end=" ")
        print(player_card.value)
        print("\n\t\tDEALER'S CARDS:")
        for card in dealer_card.cards:
            print(card)
        print("\n\t\tDEALER'S SCORE:", end=" ")
        print(dealer_card.value)

    if dealer_card.value > 21:
        print("\n Dealer Busted!!!")
        print("Player won the game...")
        quit()

    if dealer_card.value == 21:
        print("\n Dealer has a BLACKJACK")
        print(f"{name} you loose !!!")
        quit()

    if dealer_card.value == player_card.value:
        print("\nTIE !!!")
        print("Game over ....")
        quit()

    elif dealer_card.value < player_card.value:
        print(f"\n{name} you win !!!")
        quit()

    else:
        print("\nDealer win !!!")
        quit()


game_play()
