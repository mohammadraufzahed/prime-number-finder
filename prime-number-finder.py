n = 3 # put your number here
prime = True

for i in range(2, n):
    if n % i == 0:
        prime = False
if prime:
    print("It's prime number")
else:
    print("It's not a prime number")