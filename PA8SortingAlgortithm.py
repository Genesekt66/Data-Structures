#
# Evan Schleter - Assignment 8 
# (2025 - All right reserved)
#
#
# The problem that I chose for this assignment was sorting playing cards in your hand while playing a card game. While this does not necessarily  
# have applications within business beyond further development into a simple game of some sort, it is a real world situation that many have probably used an algorithm to sort there hand without even realizing it.
# The problem is based on drawing cards from a deck at random and sorting them by value and suit in your hand. This is done in most card games for organization and optimization reason so that you can more easily
# find the card you need to play and even be aple to plan a turn in advance more effectively.
# I chose playing cards as they lended themselves well to object oriented programming and the different aspects could be represented in a class easily.
# I chose the insertion sort algorithm for this assignment because it applies itself well to sorting cards. For the insertion sort I did partially modify it in order to also sort the cards by suit as well as value.
#
# As for ChatGPT interactions, I started by asking to provide me examples of real world applications of sorting algorithms. ChatGPT supplied a list of algorithms with descriptions of their real world applications.
# I then asked to provide information about the insertion sort algorithm specifically along with a walkthough of the algorthm itsellf, as in-class it was one that I had trouble wrapping my head around initially from the examples.
# An application of insertion sort that ChatGPT gave as an example was for sorting playing cards, which inspired this entire program.
# In order to better understand how to structure the insertion sort algorithm to include sorting by suit, I did ask the best way to handle the fact that the suit was represented by a string in the class method.
# ChatGPT recomended I use a dictionary and assign each suit an integer within the dictionary and call it in order to then compare their values.
# In retrospect, I could have represented the suit as an integer in the class from the get-go and handle them in a similar fashion to the non-standard card types. This is something that I would change in the future if I ever came back to this program.
#

import random

class PlayingCard: #class to control indevidual card information
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def print(self):
        card_alias = {1: "Ace",11: "Jack", 12:"Queen", 13:"King"}

        if (self.number > 10 or self.number == 1):
            alias = card_alias[self.number]
        else:
            alias = self.number 

        print(f"{alias} of {self.suit}s") 
        #each card contains both a single numeric value of 1-13 and a suite. 1 and 11 - 13 are the non standard cards also represented by a name that is not a number, ace, jack, queen, king respectively.
        #in the class they are represented by the numeric value, but the print method checks if the class instance is any of those card types and prints them with their actual name using the dictionary card_alias.

class Deck: #class to hold deck
    deck = []
    def __init__(self): #contructor populates deck with every combination of suit and number and shuffles them for good measure 
        self.deck=[]
        suits = ["Club","Diamond","Hearts", "Spade"]
        for suit in suits:
            for i in range(1,14):
                self.deck.append(PlayingCard(suit,i))
        
        random.shuffle(self.deck)
    
    def RefreshDeck(self): #clears out remaining cards in the deck and repopulates
        self.deck=[]
        suits = ["Club","Diamond","Heart", "Spade"]

        for suit in suits:
            for i in range(1,14):
                self.deck.append(PlayingCard(suit,i))
        
        random.shuffle(self.deck)
        

class Hand: #class to control your hand and the cards within it.
    def __init__(self):
        self.hand = []    

    #The hand is sorted using a modified version of insertion sort. When checking the card value against the previously sorted items of the array, 
    #upon finding other cards of the same value, it then sorts the sub array by suit. The order sorted is Club, Diamond, Hearts, and Spade.
    #This logic can be tweaked slightly in order to sort by suit and then value if that is needed instead.
    def SortHand(self): 
        suit_order = {"Club": 0, "Diamond": 1, "Heart": 2, "Spade": 3} #uses a similar method to the print function in the Playing card class using a dictionary, but backwards.


        if (len(self.hand) > 1): 
            for i in range(1, len(self.hand)):
                key = self.hand[i]
                s = i - 1
                while s >= 0 and (
                    self.hand[s].number > key.number or (
                    self.hand[s].number == key.number and suit_order[self.hand[s].suit] > suit_order[key.suit])
                ):
                    self.hand[s+1] = self.hand[s]
                    s -= 1

                self.hand[s + 1] = key
    
    def draw(self,cards,deck): #adds specified number of cards from the deck to your hand. Modular if you ever want to have multiple decks if you are insane
        for i in range(cards):
            if (len(deck.deck)-1) >= 0:
                self.hand.append(deck.deck.pop())
            else:
                print("You've drawn as much as you've could!\nOut of cards! Sorry.")
                break
          

    def print(self):
        for card in self.hand:
            card.print()
            

deck = Deck()
hand = Hand()
hand.draw(7,deck)

while True:
    print() #the mythical formating print because visual studio is acting like the \n in the next line doesn't exist
    print("\nWelcome to my card game!\n\nWhat would you like to do?")
    print("1. Look at hand.")
    print("2. Sort your hand.")
    print("3. Shuffle your hand.")
    print("4. Draw more cards.")
    print("5. Reset the game.")

    choice = input("\nEnter your choice:")

    if choice == "1":
        hand.print()
    if choice == "2":
        hand.SortHand()
    if choice == "3":
        random.shuffle(hand.hand)
    if choice == "4":
        num = int(input("How many cards would you like to draw?"))
        hand.draw(num,deck)
    if choice == "5":
        deck.RefreshDeck()
        hand.draw(7,deck)

