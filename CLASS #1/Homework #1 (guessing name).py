# Adamaris Cruz
#September 23, 2017
import random
correct_number = random.randint (1,20)
print ("im tinking of a number betwenn 1 and 20. Can you guess it?? ")
guess_number = int(input())
while guess_number != correct_number:

    if guess_number < correct_number:
        print ('too low ')
        guess_number = int(input())
    elif guess_number > correct_number:
        print ('too hig')
        guess_number = int(input())
print ('yes')
