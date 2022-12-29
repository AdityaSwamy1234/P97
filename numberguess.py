import random
n= random.randint(1,9)
n1=int(input("Guess a number between 1 and 9:"))

while n!=n1:
 if n1>n:
  print("Try a lower number ")
 if n1<n:
  print("Try a higher number")
 n1=int(input("Enter the number"))

 if n1==n:
     print("Well done you guessed it correctly")
