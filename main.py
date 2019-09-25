# beat the dealer by getting a count as close to 21 as possible, without going over 21.

# before the deal begins, each player places a bet

# player receives two cards, and the dealer receives one card 

# player must decide whether to "stand" (not ask for another card) or "hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly)

# dealer deals another card. If the total is 17 or more, it must stand. If the total is 16 or under, then add cards until its 17 or more

# If player is closer to 21 than dealer, they win. IF player gets exactly 21, it's a blackjack!


import random

def blackjack():
    
    deck = [1,2,3,4,5,6,7,8,9,10,11]
    playerCardOne = random.choice(deck)
    playerCardTwo = random.choice(deck)
    
    total_balance = 200
    print(f'\nWelcome to the blackjack table!\nYour current balance is ${total_balance}, would you like to play? (Y / N) ')
    userInput = input('').upper()
    
    def endCard():
        print('Thanks for stopping by! Come Again!')
        return

    def hit():   
        newplayerCard = random.choice(deck)
        if newplayerCard + (playerCardOne + playerCardTwo) < 21 :
            
            print(f'You pulled a(n) {newPlayerCard}')
            hitOrStand()
        

    def hitOrStand():
        print('\nWould you like to hit or stand? (Hit / Stand)')
        userInputhit = input('').upper()
        if userInputhit == 'HIT':
            hit();
            print('You hit!')
        elif userInputhit == 'STAND':
            # TODO
            print('You stand.')
        else:
            print('Sorry? Come again')
            hitOrStand()
            
    def mainGame():
      
        dealerCardOne = random.choice(deck)
        print("\nHere are your cards sir and/or ma'am!\n")
        print(f'You are handed a(n) {playerCardOne} and a(n) {playerCardTwo}.')
        print(f'The dealer places in front of them a(n){dealerCardOne}')
        hitOrStand()
        

    if userInput == 'Y':
        mainGame()
        
    else:
        endCard()
        

blackjack()