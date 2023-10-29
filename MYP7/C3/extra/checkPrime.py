x = 7

i = 2

flagPrime = True

while i <= x-1:

    if x % i == 0:
        flagPrime = False
        break

    i = i + 1

print("Is", x, "a prime number?", flagPrime)
