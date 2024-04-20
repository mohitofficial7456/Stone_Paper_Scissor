import random

def play(user,comp):
    user = int(user)
    if(user == comp):
        return 0
    
    elif(user == 0 and comp == 1):
        return -1

    elif(user == 1 and comp == 2):
        return -1

    elif(user == 2 and comp == 0):
        return -1
    
    else:
        return 1

user = input("Enter 0 for Stone, 1 for Paper and 2 for Scissor - ")
comp = random.randint(0,2)

print("You : ", user)
print("Computer : ",comp)

score = play(user,comp)
if(score == -1):
    print("You Lose")

elif(score == 0):
    print("Its a Draw")

else:
    print("You Won")