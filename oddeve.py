import random
import time
print("Let's play Odd-Eve :)")
chToss = input("We are going to do the toss. Odd or eve?")
chTossset = {"odd","eve"}
bat = {"batting", 'bat', '1', 'to bat'}
bowl = { 'bowling', 'balling', 'ball', '2'}
choice = {"batting", 'bat', 'to bat', 'bowling', 'balling', 'ball' }
choice = tuple(choice)
if chToss.lower() not in chTossset:
    print("Choose the toss properly man.")
    time.sleep(3)
    exit()
if chToss.lower() == "odd":
    xc = 0
    print('you chose odd')
elif chToss.lower() == "eve":
    xc = 1
    print('you chose eve')
uToss = int(input("Lets do the toss. Remember, only 1 to 6. "))
score = {1,2,3,4,5,6}
score = tuple(score)
cToss = random.choice(score)
print('I did ', cToss)
if uToss not in score:
    print("you didnt give number properly. ill close the game now")
    time.sleep(3)
    exit()
rToss = cToss + uToss
if rToss % 2 == 0:
    print("It's Eve! ")
    if xc == 1:
        print("Alright you won the toss")
        gamew = input("Batting or bowling?")
        if gamew.lower() in bat:
            print("okay batting it is.")
            plyrchoice = 1
        elif gamew.lower() in bowl:
            print("okay bowling it is.")
            plyrchoice = 2
    if xc == 0:
        print("uh oh you lost the toss")
        c = random.choice(choice)
        print("I get to choose then, i choose ", c)
        if c in bat:
            plyrchoice = 2
        elif c in bowl:
            plyrchoice = 1
elif rToss % 2 != 0:
    print("It's Odd! ")
    if xc == 1:
        print("uh oh you lost the toss")
        c = random.choice(tuple(choice))
        print("I get to choose then, i choose ", c)
        if c in bat:
            plyrchoice = 2
        elif c in bowl:
            plyrchoice = 1

    if xc == 0:
        print("Alright you won the toss")
        gamew = input("Batting or bowling?")
        if gamew.lower() in bat:
            print("okay batting it is.")
            plyrchoice = 1
        elif gamew.lower() in bowl:
            print("okay bowling it is.")
            plyrchoice = 2

print("Alright, lets continue.")

plyrbat = 0
compbat = 0
plyrwicket = 0
cwicket = 0
stat = {0, 1}
game = 0

while game in stat:
    if plyrchoice == 1:
        while plyrwicket == 0:
            print("You are batting!")
            pbat = int(input("Choose from 1 to 6! "))
            if pbat not in score:
                print("you didnt give number properly. ill close the game now")
                time.sleep(3)
                exit()
            cball = random.choice(score)
            print('You chose- ', pbat, 'I chose- ', cball)
            if pbat != cball:
                plyrbat += pbat
                print('you made ', pbat, ' runs. Total runs- ', plyrbat)
                pbat ==0
                cball = 0
            elif pbat == cball:
                print("You're out! you made ", plyrbat, ' runs.')
                print(' ')
                game += 1
                plyrwicket += 1
                plyrchoice = 2


    elif plyrchoice == 2:
        while cwicket == 0:
            print("You are bowling!")
            pball = int(input("Choose from 1 to 6! "))
            if pball not in score:
                print("you didnt give number properly. ill close the game now")
                time.sleep(3)
                exit()
            cbat = random.choice(score)
            print('You chose- ', pball, 'I chose- ', cbat)
            if pball != cbat:
                compbat += cbat
                print('I made ', cbat, ' runs. Total runs of mine- ', compbat)
                pball = 0
                cbat = 0
            elif pball == cbat:
                print("I am out!, I made ", compbat, ' runs.' )
                print(' ')
                game += 1
                cwicket += 1
                plyrchoice = 1
#    elif game == 2:
#      break


if game == 2:
    print('Game over!!')
    print( ' ')
    print('You made ', plyrbat, 'runs.')
    print('I made ', compbat, 'runs.')
    if plyrbat == compbat:
        print( ' ')
        print(' Uh oh! its a tie!!')
        print('Good game. I will quit now. ')
        time.sleep(10)
        exit()
    elif plyrbat > compbat:
        print( ' ')
        print(' YAY! You win!!')
        print('Good game. I will quit now. ')
        time.sleep(10)
        exit()
    elif plyrbat < compbat:
        print( ' ')
        print(' uh OH! I win!! you lose haha.')
        print('Good game. I will quit now. ')
        time.sleep(10)
        exit()
