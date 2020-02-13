txt = input("Type your number:") #This will take the number from user
number = int(txt)
#Put your number here
prime = True

for i in range(2, number): #Prime number recognition
    if number % i == 0:
        prime = False
if prime:
    print("It's prime number")
else:
    print("It's not a prime number")