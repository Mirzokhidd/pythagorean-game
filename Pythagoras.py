#Porject: Pythagoras
#By: Mirzokhid Ganiev
#Age: 16
#Grade: 10 G
#Date upon finishing: Friday, 12th February 2021 (12/02/2021)
#Location: Osh,  kyrgyzstan

#Basic idea: 
# The first option calculate the answer for any pythagoras question
# The second optino works in this manner and steps: 
# randomly chooses a side 
# than randomly assigns values from 0-10 to the other sides
# than asks you to answer the question
#s tracks the score and has 10 questions
#imports

import math
import random
from random import randrange
import sys

chooseProgram = int(input("Choose between: (type only the number) \n 1. Calculate \n 2. Question \n 3. Quit \n "))

#extra functios:


#calculate any side of a right angle trainle with pythagoras
def programOne():
    if chooseProgram == "calculate" or chooseProgram == 1: # start the program
        print(" \n |\ \na| \ c\n |  \ \n ---- \n  b") 
        ask = input("Which side do you want to calculate (a, b, c) (You can press Q to quit): ") # ask the question
        if ask == "a" or ask == "A":
            b = int(input("Value for b: ")) #ask values
            c = int(input("Value for c: ")) #ask values
            total = round(math.sqrt((c**2) - (b**2)))
            print("The value of the A would be: " + str(total) + "\n") #calculate
        elif ask == "b" or ask == "B":
            a = int(input("Value for a: ")) #ask values
            c = int(input("Value for c: ")) #ask values
            total = round(math.sqrt((c**2) - (a**2)))
            print("The value of the B would be: " + str(total) + "\n") #calculate
        elif ask == "c"or ask == "C":
            a = int(input("Value for a: ")) #ask values
            b = int(input("Value for b: ")) #ask values
            total = round(math.sqrt((a**2) + (b**2)))
            print("The value of the C would be: " + str(total) + "\n") #calculate
        elif ask == "q" or ask == "Q":
            sys.exit()
        else: 
            print("That wasnt there")
            ask = input("Which side do you want to calculate (a, b, c): ")


#play a game. 10 random question on the topic
def programTwo():
    global score
    global point

    while point < 10:
        letters = ["c", "a", "b"]
        randomLetter = random.choice(letters) #choose a random side for the question
        if randomLetter == "a": #if the side is a
            b = randrange(10) #random value for the b side
            c = randrange(10) #random value for the c side
            if b > c: #if b is lager than c, than restart the function.
                print("Sorry the random values are a bit wrong. Here is an another questoin \n")
                programTwo()
            elif b < c: #else continue
                print(" \n |\ \na| \ c\n |  \ \n ---- \n  b") #draw the triangle
                print("Find " + randomLetter + ": ") 
                print("B is: " + str(b) + " \nC is: " + str(c))
                solution = round(math.sqrt((c**2) - (b**2))) #calculate the answer
                answer = float(int(input("Your answer for A is ( Round to the whole number ): ")))
                if solution == answer: #compare the user's answer and the real solution
                    print("Yes, you are right!! Your answer " + str(answer) + " is correct. \n") #they are are correct
                    score += 1
                    point += 1 
                    print("Your score is " + str(score) +"\n") #print scores
                elif solution != answer: #if the user's answer is wrong
                    point += 1
                    print("Sorry you are wrong.The correct answer is: " + str(solution))
        elif randomLetter == "b": #if the side is b
            a = randrange(10) # assign a random number to a
            c = randrange(10) # assign a random number to c
            if a > c: # if a is bigger than c restart the function
                print("Sorry the random values are a bit wrong. Here is an another questoin \n")
                programTwo()
            elif a < c: # if everything is right than continue
                print(" \n |\ \na| \ c\n |  \ \n ---- \n  b") # draw a triangle
                print("Find " + randomLetter + ": ")
                print("A is: " + str(a) + " \nC is: " + str(c))
                solution = round(math.sqrt((c**2) - (a**2))) # calculate the answer
                answer = float(int(input("Your answer for B is ( Round to the whole number ): ")))
                if solution == answer: #compare the user's answer and the real solution
                    print("Yes, you are right!! Your answer " + str(answer) + " is correct. \n")
                    score += 1
                    point += 1
                    print("Your score is " + str(score) +"\n") #print scores
                elif solution != answer:#if the user's answer is wrong
                    point += 1
                    print("Sorry you are wrong.The correct answer is: " + str(solution))
        elif randomLetter == "c": # if the side is c
            b = randrange(10) #random value for b
            a = randrange(10) #random value for a
            if a <= b or a >= b:
                print(" \n |\ \na| \ c\n |  \ \n ---- \n  b") #draw a triangle
                print("Find " + randomLetter + ": ")
                print("A is: " + str(a) + " \nB is: " + str(b))
                solution = round(math.sqrt((a**2) + (b**2)))
                answer = float(int(input("Your answer for C is ( Round to the whole number ): ")))
                if solution == answer: #compare the user's answer and the real solution
                    print("Yes, you are right!! Your answer " + str(answer) + " is correct. \n")
                    score += 1
                    point += 1
                    print("Your score is " + str(score) +"\n") #print scores
                elif solution != answer:#if the user's answer is wrong
                    point += 1
                    print("Sorry you are wrong.The correct answer is: " + str(solution))

#global variables:
score = 0 #scores
point = 0 #to make sure there are exactly 10 questions because in my code there are parts where the function is restarted. If not taken care of the function can go on for every and the score would be set to 0 everytime

#Menu page
while True:
    if chooseProgram == 1:
        programOne()
    elif chooseProgram == 2:
        print("There will be 10 questions to answer. Hope you get a 100%, good luck.")
        programTwo()
        if point == 10: #end the question
            print("You are done. You got " + str(score) + " / 10 \n")
            score = 0
            chooseProgram = int(input("Choose between: (type only the number) \n 1. Calculate \n 2. Question \n 3. Quit \n "))
    elif chooseProgram == 3:
        sys.exit()
