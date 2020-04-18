#Rain Kinsey
#Lame Game – This program will display a game menu and allow the user to select their desired option
#Then, let the user play Make Change, High Card, Deal Hand, Save Dream Cards, Display Dream Cards, Word Guess, or quit.

import cardClass
import random


#Displays menu and runs the program
def main():
    try:
        #Let user select choice
        choice = menu()

        while choice >= 1 and choice < 8:
            #If the user chose option 1: Make Change
            if choice == 1:
                make_change()

            #The user will play a game of High Card
            elif choice == 2:
                high_card()

            #The user will play a game of Deal Hand
            elif choice == 3:
                deal_hand()
            #The user will play a game of Save Dream Hand
            elif choice == 4:
                save_dream_hand()

            #The user will be prompted to open a file then read it
            elif choice == 5:
                display_dream_hand()

#The user will play a game of Word Guess
            elif choice == 6:
                word_guess()
#This will print a message for the exiting user
            elif choice == 7:
                print("Thanks for stopping by. Have a nice day!")
                break
            choice = menu()

    except Exception as error:
        print(error)


#Gives the user a description of the games and allows them to choose a game, validates the choice and returns it
def menu():
    #Initialize choice by adding a value to it in order to avoid an exception
    choice = 0

    try:
        #This is the welcome statement
        print("Welcome to Lame Games!" "\n")

        #Display of the menu
        print("MAIN MENU")
        print("1. Make Change - Calculate How Much Change Is Due"
              "\n"
              "2. High Card - See If You Have The Highest Card"
              "\n"
              "3. Deal Hand - Deals Five Cards"
              "\n"
              "4. Save Dream Hand - Pick 5 Playing Cards and Save to a File"
              "\n"
              "5. Display Dream Hand - Read Your Dream Cards' File"
              "\n"
              "6. Word Guess - Guess The Word"
              "\n"
              "7. Quit")

        #Allows user to choose numbers 1, 2, or 3 only and re-enter if the user puts an invalid number
        choice = int(input("Choose an Option Number: "))

        while choice > 7 or choice < 1:
            print("Invalid Option" "\n")
            main()

    except ValueError:
        print("Error: Invalid Data Entered")
    except:
        print("An Unknown Error Has Occurred")

    #Pass choice back to user if valid
    return choice


#Allows user to Calculate How Much Change Is Due in dollars, quarters, dimes, nickels, and pennies
def make_change():
    #Asks for the amount owed and amount paid
    owed = float(input("\n" "Amount Owed: $"))
    paid = float(input("Amount Paid: $"))
    change_due = paid - owed

    #Display no amount due if applicable
    if change_due == 0:
        print("No Change Due")

    #Display not enough payment if applicable
    elif owed > paid:
        print("Insufficient Payment")

    #Displays amount of change due if applicable
    else:
        print("\nChange Due: $", format(change_due, ",.2f"), sep='')

        #Breaks down the change due dollars
        dollar = int(change_due)

        #Breaks down the change due quarters
        quarter = int((change_due - dollar) / 0.25)

        #Breaks down the change due dime
        dime = int(((change_due - dollar) - (quarter * 0.25)) / 0.10)

        #Breaks down the change due nickels
        nickel = int(
            ((change_due - dollar) - (quarter * 0.25) - (dime * 0.10)) / 0.05)

        #Breaks down the change due pennies
        penny = round(((change_due - dollar) - (quarter * 0.25) -
                       (dime * 0.10) - (nickel * 0.05)) / 0.01)

        #Display dollar amount of change due
        if dollar > 1:
            print(format(dollar, ','), "dollars")
        elif dollar == 1:
            print(format(dollar, ','), "dollar")

        #Display quarter amount of change due
        if quarter > 1:
            print(format(quarter, ','), "quarters")
        elif quarter == 1:
            print(format(quarter, ','), "quarter")

        #Display dime amount of change due
        if dime > 1:
            print(format(dime, ','), "dimes")
        elif dime == 1:
            print(format(dime, ','), "dime")

        #Display nickel amount of change due
        if nickel > 1:
            print(format(nickel, ','), "nickels")
        elif nickel == 1:
            print(format(nickel, ','), "nickel")

        #Display penny amount of change due
        if penny > 1:
            print(format(penny, ','), "pennies")
        elif penny == 1:
            print(format(penny, ','), "penny\n")


#Allows 2 users to see if one has the highest card by assigning a random number to the user and giving the number a card face value
def high_card():
    first_player = input("\nPlayer 1's Name:")
    second_player = input("Player 2's Name:")

    player1_card = cardClass.Card()
    player2_card = cardClass.Card()

    #Generate random cards and assign them to the players
    player1_card.deal()
    player2_card.deal()

    print("\nDealing Cards...\n")
    print(first_player, "has {}.".format(player1_card.get_face_value()))

    print(second_player, "has {}.".format(player2_card.get_face_value()))

    #Declare a winner or a tie
    if player1_card.get_value() > player2_card.get_value():
        print(first_player, "Wins!\n")
    elif player1_card.get_value() < player2_card.get_value():
        print(second_player, "Wins!\n")
    else:
        print("It's a Tie!\n")


#Displays the card face value of each card
def display_hand(card_list):
    #Read line of file, convert to interger, finally display face value
    for item in card_list:
        print(item.get_face_value())


#Displays the total and average of the card values
def hand_stats(card_list):
    #Set total = 0, so it is assigned before it is called
    total = 0

    #Caluculate the total of the list
    for i in range(len(card_list)):
        total = total + card_list[i].get_value()

    #Calculate the average of the card values
    average = total / len(card_list)

    #Print the sum and the average
    print("The Total of the Card Values:", total)
    print("The Average of the Card Values:", average)


#Displays 5 face value cards using random number function and assigning the numbers a face value
def deal_hand():
    #Create list
    card_list = []

    #Display a opening message
    print("\nDealing Cards...")

    for item in range(5):
        #Assign cards to random value
        card = cardClass.Card()
        card.deal()

        #Store the cards in a list and save in file
        card_list.append(card)
    print("Your Hand is ")
    #Display hand
    display_hand(card_list)

    #Display hand statistics
    hand_stats(card_list)

    print("")


#Allows the user to choose and save their card hand, the cards are given numeric value
def save_dream_hand():
    #Create list
    card_list = []
    try:
        print(
            "\nUsing Numbers 1-13, 1 = Ace and 13 = King, Enter Your 5 Dream Cards:\n"
        )

        #Ask for dream cards
        for item in range(5):
            card = int(input("Card: "))

            while card > 13 or card < 1:
                print("Invalid Choice. Try Again.\n")
                card = int(input("Card: "))

            card_obj = cardClass.Card()
            card_obj.set_value(card)
            #Store the cards in a list
            card_list.append(card_obj)

        #Save user input to filename
        file = open(str(input("\nPlease Type File Path To Save Cards: ")), 'w')

        print("\nSaving Cards...")
        #Save file
        for item in card_list:
            file.write(str(item.get_value()) + '\n')

        #Close the file
        print("\nCards Are Saved!\n")
        file.close()

        print("")

    # Error trap for invalid value for card
    except ValueError:
        print("Error: Invalid Input")
    except:
        print("An Unknown Error Has Occurred")


#Allows the user to retrieve and display their dream card hand in face card value
def display_dream_hand():
    #Create list
    card_list = []
    try:
        #Prompt user to open file
        card_file = open(str(input("\nYour Dream Card File Name: ")), 'r')

        for line in card_file:
            card = int(line)
            card_obj = cardClass.Card()
            card_obj.set_value(card)
            card_list.append(card_obj)

        #Call lines of file
        display_hand(card_list)

        #Close file
        card_file.close()

        print("")

    # Check for invalid file name
    except FileNotFoundError:
        print("Error: File Does Not Exist")


#Allows user to guess a word chosen by another user, exposiong the correct guess until the entire word is uncovered
def word_guess():

    print("")

    #Ask for word to guess
    word = str(input("Type a Word to Guess: "))
    #make the case the same, so all input will be valid
    word = word.lower()

    #Display enough space to hide the word
    print("\n" * 100)

    #Display astericks the length of the word
    blank = "*" * len(word)

    print(blank)

    #Make sure that the variable is set to string
    string = ""

    guessed = ""

    #Ask for a letter until word is complete
    while string != word:
        #Ask user for letter to guess
        guess = str(input("Guess a Letter: "))
        print("")
        string, guessed = hide_word(string, word, guess, guessed)
        print(string)

    if string == word:
        print("You Win!\n")


def hide_word(string, word, guess, guessed):

    #Add results
    result = ""

    #Make sure this will translate into string character
    ch = ""

    #Adds new character to guessed

    if guess not in guessed:
        guessed += str(guess)
    else:
        print("You Have Already Guessed This Letter\n")

    #Tell the user if they already guessed
    for letter in word:
        if letter in guessed:
            result += letter
        else:
            result += "*"

    return result, guessed


main()
