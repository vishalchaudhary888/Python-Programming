import random as r
print('''Rules are simple :-
        On every wrong guess the hang stages will increase if you guess is right then hange man stage will not increase.
        ''')
st = "abcdefghijklmnopqrstuvwxyz"
n = int(input("Enter the lenght of the word. :- "))

word_ls = r.choices(st,weights=None,k=n)
c_wordst = ""
for i in range(n):
    c_wordst += str(word_ls[i])

ms_wordls = r.sample(c_wordst, k = n//2)
miss_words = ""
for i in range(len(ms_wordls)):
    miss_words += c_wordst.replace(ms_wordls[i],"_")
miss_wordsstr = ""
for i in range(len(ms_wordls)):
    miss_wordsstr += str(ms_wordls[i])
print('''Stages for the hang man are:-
    1.  +----+
        O    |
             |
             |
            ---
    2.  +----+
        O    |
        |    |
             |
            ---
    3.  +----+
        O    |
       /|    |
             |
            ---
    4.  +----+
        O    |
       /|\   |
             |
            ---
    5.  +----+
        O    |
       /|\   |
       /     |
            ---
    6.  +----+
        O    |
       /|\   |
       / \   |
            ---
        It means you have given total 6 chances to save the man from hangging.
        So try your luck and save the man.
        All the best!''')
print("Word is:-- ",miss_words)

max_limit = 6
count = 1
while count <= max_limit:
    user = input('''Enter the word you guess which can fill in the empty space.--> ''')
    print()
    if user in miss_wordsstr:
        print('''Your guess is right.
        ''')
    elif user not in miss_wordsstr:
        print('''Your guess is wrong and remaining chances are :--  ''',6-count)
        count +=1
    else:
        print("Please! Enter a valid word!")
    
if max_limit<count:
    print('''Your chances are over! 
    +----+
    O    |
   /|\   |
   / \   |
        ---
    Sorry! you hanged the man.    ''')
