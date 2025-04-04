import random as rd
import string
lt = list(string.ascii_letters) + list(string.digits) +list(string.punctuation)
n = int(input("Enter how many digit passwoed you need: "))
password = ""
for i in range(1 , n+1):
    password += rd.choice(lt)
print(password)