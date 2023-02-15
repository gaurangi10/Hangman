import random


def hangman():

    list_of_words = ['edureka', 'world', 'animals', 'bakery', 'beaches', 'cricket', 'celebrity', 'wolverine', 'weekends', 'google', 'diner', 'eiffel tower']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')


    while len(word)>0:
        main_word = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "

        if main_word == word:
            print(main_word)
            print("YOU WON!!")
            break

        print("Guess the word", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade+guess
        else:
            print("enter valid character")
            guess=input()

        if guess not in word:
            turns = turns-1

            if turns==9:
                print("9 turns left!!")
                print("_ _ _ _ _ _ _ _")
            if turns==8:
                print("8 turns left!!")
                print("_ _ _ _ _ _ _ _")
                print("       O       ")
            if turns==7:
                print("7 turns left!!")
                print("_ _ _ _ _ _ _ _")
                print("       O       ")
                print("       |       ")
            if turns==6:
                print("6 turns left!!")
                print("_ _ _ _ _ _ _ _")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            if turns==5:
                print("5 turns left!!")
                print("_ _ _ _ _ _ _ _")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns==4:
                print("4 turns left!!")
                print("_ _ _ _ _ _ _ _")
                print("      \O       ")
                print("       |       ")
                print("      / \      ")
            if turns==3:
                print("3 turns left!!")
                print("_ _ _ _ _ _ _ _")
                print("      \O/       ")
                print("       |       ")
                print("      / \      ")
            if turns==2:
                print("2 turns left!!")
                print("_ _ _ _ _ _ _ _")
                print("      \O/ |     ")
                print("       |       ")
                print("      / \      ")
            if turns==1:
                print("1 turns left!! Hangman on his last breath")
                print("_ _ _ _ _ _ _ _")
                print("      \O/_|     ")
                print("       |       ")
                print("      / \      ")
            if turns ==0:
                print("YOU LOST")
                print("You let a good man die")
                print("_ _ _ _ _ _ _ _")
                print("       O_|     ")
                print("      /|\       ")
                print("      / \      ")
                print("The word is",word)
                break
            
name = input (" ENTER YOUR NAME ->")
print ("Welcome", name, "!")
print("_ _ _ _ _ _ _ _ _ _ _ _ _")
print ("Try to guess the word in less than 10 attempts")
         
              
hangman()

