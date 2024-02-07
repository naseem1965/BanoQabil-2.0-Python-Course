#Abdur Rahman Naseem
#
#maninaseem1965@gmail.com

#Python Mini Project Code:

#importing random function:
import random

# making list's of words that has to be Gussesed related to python programming saving them in variables:

python_functions=['print','input']
python_data_types=['float','integer','dictionary','string','list']
python_errors=['syntax','zero division','runtime','name']

# Making variable in which storing these list's:

while 1:
    words_list=python_functions+python_data_types+python_errors

        # Using a random choice function:
        
    random_words=random.choice(words_list)

        #Printing Game Title:

    print("                                                  ******** Welcome to Word Guessing Games ********                                          ")

        # Using if condition:

    if random_words in python_functions:
            print("Hint: It is a Python Function")
    elif random_words in python_data_types:
                print("Hint: It is a Python Data Types") 
    elif random_words in python_errors:
                print("Hint: It is a Python Python Errors")

        #Taking User Guesses:

    user_guesses=''

        #Defining No of Attempts:
    Attempts=5

        # Using While Loop And if Conditions :

    while Attempts>0:
       wrong_guess=0
       for ch in random_words:
            if ch in user_guesses:
                print(ch,end=' ')
            else:
                wrong_guess+=1
                print('-' ,end=' ')
       if wrong_guess==0:
           print(f'\ncongrats you won the Game.The Word is : "{random_words}"')
                
        # making Again Variable For Playing Game Again or Not:
           again=input('If You  Want to Quit Game Press "q" !\nif you Want to play again press any key!!')
           if again=="q":
             print("COME BACK SOON!I'LL BE WAITING FOR YOU!")
             quit()
           else: 
            print("Yeah !! You Wnat To Challenge Me Agian :- Come On Play With Me!")
            break

       guess=input('\nGuess a Word ')
       user_guesses+=guess
        # defining wrong Attempts:
       if guess not in random_words:
            Attempts-=1
            print(f'\nWrong.You have {Attempts} More Chances!!')
            if Attempts==0:
                print(f'\nGame Over. You Lost the Game . The Word is"{random_words}"')
        # making if Player Don't Want to Restart Game:
        
                restart_game=input('If You Want to Play Agian Press"r"!!!\nIf You Dont Want Quit than Press Any of The Key!!')
                if restart_game=="r":
                  print("No Problem Bro Try It Again :-) You Will Win this Game . ")
                  break
                else:
                    print("COME BACK SOON!I'LL BE WAITING FOR YOU!")
                    quit()
                 
                        


