#Guess my number 
import random
#instructions
print ("""\t\tGuess  \t   Number      
                       my          Game \n\n""")
print ('now i will guess a number between 0 and 101. you must guess it correctly')
#computer picks a number between 1 and 100
guess = random.randint(1,100)
tries = 1
#player tries to guess it and the computer lets
player =int(input("now guess a number: "))
#the player know if the guess is too high.too low 
while player != guess : 
           if  player > guess: 
           
                 print ("too high")
                 player=int(input("try again:"))
                 tries += 1
           else : 
              
               
                 print ("too low")
                 player=int(input("try again:"))
                 tries += 1
#congragulate the player
print ('\t\t  congragulations!!\nyou have guessed my number correctly which is',guess,'in only' ,tries, 'tries')