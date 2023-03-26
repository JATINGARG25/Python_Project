import random

def game(comp,you):
    if comp == you:
        return None

    elif comp == 's': 
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w': 
        if you == 's':
            return True
        elif you == 'g':
            return False
            
    elif comp == 'g': 
        if you == 'w':
            return True
        elif you == 's':
            return False
    
randnum = random.randint(1,3)
if randnum == 1:
    comp = 's'
elif randnum == 2:
    comp = 'w'
elif randnum == 3:
    comp = 'g'

you = input("Your's Turn : Snake(s) , Water(w) or Gun(g?\n")

a = game(comp,you)

print("Computer Choose "+str(comp),end=" and ")
print("You Choose "+str(you))

if a == None:
    print("Game Draw")
elif a == True:
    print("You Win")
else:
    print("You Lose")