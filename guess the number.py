
import random as r

name = input("Enter your name:  ")
print(f'''Welcome! {name}
You are playing a game in which you have to predict the number by throwing fluke.
You have to predict the numbers as soon as you can for a better score
Note:  you have to guess the number between 1 to 100 and the number of chances given to you as per your choice.
All The Best!!''')


ls = []
for i in range(101):
    ls.append(i)

num = r.randint(0,100)
level = int(input("Enter in how much guesses you want to  guess the number: "))
us_in = 0
count = 1

while num != us_in:
    us_in = int(input("Enter the number: "))
    if count<(level):
        if num<us_in:
            print('''number is lesser than your's!
            Your guess was wrong''')
            count+=1
        elif num>us_in:
            print('''number is greater than your's!
            Your guess was wrong''')
            count+=1
    else:
        print("your chances are over")
        break
if count<(level):
    print(f"Conratulations! you guess the number in {count} trials")
