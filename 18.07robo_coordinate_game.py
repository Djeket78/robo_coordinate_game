from os import system
from re import A
from this import d

lenght = 20
roboX = 15
bombX = 8
hp=100

while True:
    system("cls")

###########################   hp  ############
    if roboX == bombX:
        hp=hp-50 
        if hp ==0:
            print("❌❌❌Game over :( ❌❌❌ ")
            break



###########################  limits  ##########

    if roboX <=1:
        roboX=1
    if roboX >=lenght:
        roboX=lenght


    ########################### MAP ###########
    x=1
    print("hp: ",hp)
    print("\n")

    while x <=lenght:
        if x==roboX:
            print("😶",end="")
        elif x==bombX:
            print("💣",end="")
        else:
            print("-", end="")
        x +=1
    print("\n")
    ####################### CONTROL ############
    direction=input("dir (a/d/x) > ")
    if direction == "a":
        roboX -=1
    if direction == "d":
        roboX +=1
    if direction == "x":
        system ("cls")
        print("Thank you for playing!!!")
        break
    ############################################
