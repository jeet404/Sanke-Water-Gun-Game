import random

print("The game will be total of 10 rounds\nPress: 's' for Snake or 'w' for Water or 'g' for Gun")
i=0
win=0
lost=0
draw=0
while i<10:
    lst=["Snake", "Water", "Gun"]
    choice=random.choice(lst)
    n=input("\nEnter your choice: ")
    if choice=="Snake":
        if n=="s":
            print("Computer's choice: ",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="w":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="g":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    elif choice=="Water":
        if n=="w":
            print("Computer's choice:",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="g":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="s":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    else:
        if n=="g":
            print("Computer's choice:",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="s":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="w":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    print("Left-over round number: ",10-i)
    a=f"\nTill now the score is:\nYou: {win}\nComputer: {lost}\nDraw: {draw}"
    print(a)
    i+=1
if i==10:
    if win>lost:
        print("\nWinner!!! You have won the game")
    elif lost>win:
        print("\nGame Over!!! You have lost the game")
    else:
        print("\nGame Draw!!!")