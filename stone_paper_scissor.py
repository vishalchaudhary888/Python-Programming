import random as r

print('''In this game you are going to play stone paper scissor.
    All the best for your luck.
    Guidence: Stone(S), Paper(P) and Scissor(Sc)''')


cha = input("Enter your choice: ")
ls = ["s","p","sc"]
com = r.choice(ls)

if com == "s" and cha.lower() == "sc" or com == "p" and cha.lower() == "s" or com == "sc" and cha.lower() == "p":
    print(f'''You choose {cha} and PC choose {com}
    Sorry! You loose the game.
    Try again!''')
elif com == cha.lower():
    print('''You both choose same.
    Match draw!
    ''')   
else:
    print(f'''You choose {com} and PC choose {cha}
    ''')
    print("Congratulations! You won the game")

use = input("Do you want playe the game again: Yes(y) or No(n)")
aga = ""
while use.lower() == "y" or aga.lower()=="y":
    cha = input("Enter you choice: ")
    if com == "s" and cha.lower() == "sc" or com == "p" and cha.lower() == "s" or com == "sc" and cha.lower() == "p":
        print(f'''You choose {cha} and PC choose {com}
        Sorry! You loose the game.
    Try again!
    ''')
    
    elif com == cha.lower():
        print('''You both choose same.
    Match draw!
    ''')
    
    else:
        print(f'''You choose {cha} and PC choose {com}
        ''')
        print("Congratulations! You won the game")
    
    aga = input("Do you want playe the game again: Yes(y) or No(n):  ")
    use ='n'