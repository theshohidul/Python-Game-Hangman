import random
import math

class Hangman:

     # Hangman game

    # hang stage and rope figure
    hang_figure = []
    hang_figure.append(' +----+')
    hang_figure.append('      |')
    hang_figure.append('      |')
    hang_figure.append('      |')
    hang_figure.append('      |')
    hang_figure.append('      |')
    hang_figure.append('=======')

    #man figure
    
    man_figure = {}
    man_figure[0] = [' |    |']

    man_figure[1] = [' |    |',' 0    |']
    man_figure[2] = [' |    |',' 0    |', ' |    |']

    man_figure[3] = [' |    |','\\0    |', ' |    |']
    man_figure[4] = [' |    |','\\0/   |', ' |    |']

    man_figure[5] = [' |    |','\\0/   |', ' |    |', '/     |']
    man_figure[6] = [' |    |','\\0/   |', ' |    |', '/ \\   |']

    man_figure[7] = [' |    |',' 0/   |', '/|    |', '/ \\   |']
    man_figure[8] = [' |    |',' 0    |', '/|\\   |', '/ \\   |']
    man_figure[9] = [' |    |',' 0    |', '/|\\   |', '/ \\   |','DEAD  |']
    
    hangman = []
    
    def __init__(self):
        i, j = 1, 0
        self.hangman.append(self.hang_figure[:])
        for ls in self.man_figure.values():
            pic, j = self.hang_figure[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.hangman.append(pic)


    def print_hangman( self, index ):
        for line in self.hangman[index]:
            print(line)

    def start (self):
        print ("\nWelcome to hangman. Please save a life guessing correct word.\n")
        # a list of words, selected a random word
        word = random.choice(['great', 'courage', 'student'])
        #remaining turns
        turns = len(word)*2
        #store user input characters
        guess = []
        k = 0

        while ( turns >= 0 ) : 
            if ( turns == 0 ): 
                print ("Hey! you have killed a man!")
                break

            hint = [l if l in guess else "_" for l in word]
            print ("\nGuess the word : ", end="")
            print (" ".join(hint) )
            print ("Turns left : ", turns )
            
            if word == ("".join(hint) ) :
                print ("\nThanks for saving a life.")
                break

            else :
                char = input ('\nEnter a character : ')
                if ( char in word ) :
                    guess.append(char)
                else :
                    turns -= 1
                    k = 10 - math.floor( 10*(turns/(len(word)*2)))
                    if  k == (len(self.hangman)-1) and turns == 1 :
                        k -= 1
            self.print_hangman(k)


Hangman().start()