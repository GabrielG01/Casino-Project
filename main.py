import random

def blackjack():
    card_list = [1,2,3,4,5,6,7,8,9,10,11]
    total_balance = 200
    print(f'\nWelcome to the blackjack table!\nYour current balance is ${total_balance}, would you like to play? (Y / N) ')
    userInput = input('').upper()
    
    def endCard():
        print('Thanks for stopping by! Come Again!')
        return

    def mainGame(deck, cash):
        playerCardOne = random.choice(deck)
        playerCardTwo = random.choice(deck)

        print("Here are your cards sir and/or ma'am!\n")
        print(f'You are handed a(n) {playerCardOne} and a(n) {playerCardTwo}.')
        

    if userInput == 'Y':
        mainGame(card_list,total_balance)
        
    else:
        endCard()
        

blackjack()