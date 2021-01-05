# Get the number from the user
number = int(input("Type your number:"))
# Put your number here
prime = True

for i in range(2, number): #Prime number recognition
    if number % i == 0:
        prime = False
if prime:
    print("It's prime number")
else:
    print("It's not a prime number")