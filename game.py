import random
def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you == 'g':
             return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you=='w':
            return True

    
randNo = random.randint(1,3)
print("Computer's turn : Snake(s) Water(w) or Gun(g) ")
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 'g':
    comp = 'g'
you = input("Your turn : Snake(s) Water(w) or Gun(g) ")
a = gameWin(comp,you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("This is tie")
elif a==1:
    print("You Won!")
else:
    print("You lost the game")
