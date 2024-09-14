import random

#Global Values start---

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 9
}

symbol_values = {
    "A": 5,
    "B": 3,
    "C": 4,
    "D": 2
}

#Global Values end---


#Checking winnings in that spin start---
def wins(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
#Checking winnings in that spin stop---



#Slot machine start---
def get_spin_slot(rows, cols, symbols):
    
    all_symbols = [] #Making a list to append symbols into it
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)#Appending all symbols into the list
            
            
    columns = []
    for col in range (cols):
        column = [] #Making a List for values
        current_symbols = all_symbols[:] #Copying all values to dont use them more it needs
        for row in range(rows):
            value = random.choice(all_symbols)#Taking random Value in the list of all_symbols
            current_symbols.remove(value) #Deleting it from copy list
            column.append(value)#Adding random values to new column list
        columns.append(column)
    return columns
#Slot machine end---


#Slot Machine's simple layout screen start---
def print_slot_machine(columns):
    for row  in range (len(columns[0])):
        for q, column in enumerate(columns):
            if q != len(columns) -1: 
                print(column[row], end=" | ") #after every output prints pipe
            else: 
                print(column[row], end="")
        print()
#Slot Machine's simple layout screen end---


#Getting amount of balance for deposit start---
def deposit():
    while True: 
        #Getting amount input
        amount = input("How much would like to deposit $")
        
        #checking amount is digit or string
        if amount.isdigit():
            
            #if amount is digit converting into the integer
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0. ")
        
        else: #if amount isn't integer prints this line
            print("Please enter a number")
            
    return amount 
#Getting amount of balance for deposit end---


#Getting amount of number of lines start---
def get_number_of_lines():
    while True: 
        #Getting lines input
        lines = input("Enter lines of you desire (1 - " + str(MAX_LINES) + " ) ? ")
        
        #checking lines is digit or string
        if lines.isdigit():
            
            #if lines is digit converting into the integer
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines ")
        else: #if value of lines isn't integer prints this line
            print("Please enter a number")
            
    return lines 
#Getting amount of number of lines end---


#Getting amount of bet start---
def get_bet():
    while True: 
        #Getting amount of input
        amount = input("What is your bet on each line $")
        
        #checking amount is digit or string
        if amount.isdigit():
            
            #if amount is digit converting into the integer
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                #Making sure amount is between given between min and max bet on the global values
                print(f"Amount must be between #{MIN_BET} - ${MAX_BET}")
        
        else: #if amount isn't integer prints this line
            print("Please enter a number")
            
    return amount
#Getting amount of bet end---

def spin(balance):
    lines = get_number_of_lines()
    
    
    #Checking if balance is more than the bet
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your balance is not enough for the bet .Your current balance is ${balance}. Try Again...")
        else:
            break
        
        
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet} ")
    
    slots = get_spin_slot(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = wins(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on lines", *winnings_lines)
    
    return winnings - total_bet


#Looping the slot machine if we want to play or we have balance to play
def main():
    balance = deposit()
    while True: 
        print(f"Current balance is: ${balance}")
        answer = input("Press ENTER to play - Press 'q' to  Quit ")
        if answer == "q":
            break

        balance += spin(balance)#Updating Balance that we have
        
main()


        
