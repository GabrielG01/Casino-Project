def blackjack():
    card_list = [1,2,3,4,5,6,7,8,9,10]
    total_balance = 200
    print(f'\nWelcome to the blackjack table!\nYour current balance is ${total_balance}, would you like to play? (Y / N) ')
    userInput = input('').upper()
    
    def endCard():
        print('Thanks for stopping by! Come Again!')
        return

    if userInput == 'Y':
        print('thats cringe')
    else:
        endCard()
        

blackjack()