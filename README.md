# Python-Programming
#All the codes of python which i had practiced.
import random as r

print('''Welcome!
You are playing a game in which you have to predict the number by throwing fluke.
And you can also enter how much guesses you want to guess the number.
you have given 10 chances to predict the number between 1 to 100.
Note:  you have to guess the number between 1 to 100 and the number of chances are 10.
All The Best!!''')


ls = []
for i in range(101):
    ls.append(i)

num = r.randint(0,100)
level = int(input("Enter how much guesses you want to enter guess the number: "))
us_in = 0
count = 1
print(num)
while num != us_in:
    us_in = int(input("Enter the number: "))
    if count<(level+1):
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
if count<(level+1):
    print(f"Conratulations! you guess the number in {count} trials")
