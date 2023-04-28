#OTP generator
import random as r

val = r.random()
stri = str(val)
num = int(input("how many digit otp you want: "))
print("your otp is: ",stri[3: num+3])
