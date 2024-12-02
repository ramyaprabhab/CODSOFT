# r=-1
# p=0
# s=1

import random
a=int(input("enter the number for times you want to play: "))
for i in range (a):
    computer=random.choice([1,-1,0])
    user=input("enter your choice from r/p/s : ")
    userDict={"r":-1,"p":0,"s":1}
    revDict={-1:"rock",0:"paper",1:"scissor"}
    you=userDict[user]
    print(f"you chose {revDict[you]}\nand compputer chose {revDict[computer]}")

    if(computer==you):  
     print("its a draw")

    else:
        if(computer ==-1 and you == 0): 
            print("you lose")
    
        elif(computer ==-1 and you ==1):    
            print("you win")
    
        elif(computer ==0 and you ==1):
            print("you lose")
    
        elif(computer==0 and you ==-1):
            print("you win")
    
        elif(computer==1 and you ==-1):
            print("you lose")
    
        elif(computer==1 and you ==0):
            print("you win")
    
        else:
            print("oops!")