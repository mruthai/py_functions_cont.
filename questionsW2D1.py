
#Exercise #1

"""Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop."""


number_cubed = 0

while True:
    
    cube = number_cubed ** 3
    number_cubed += 1
    if cube <= 1000:
        print(cube)
    else:
        cube >= 1000
        break


# Exercise #2

"""Get first prime numbers up to 100"""

# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

# for prime in range(1, 100):
#     if prime / 2 != 2:
#         print(prime)
#     elif prime % 3 != 2:
#         print(prime)
#     elif prime % 5 != 2:
#         print(prime)
#     elif prime % 7 != 2:
#         print(prime)

# for number in range(2,101):
#     prime = True
#     for not_prime in range(2,number):
#         if (number % not_prime == 0):
#             prime = False
#     if prime:
#         print(number)

for prime in range(2,101):
    prime_time = prime * 6 + 1
    if prime == 2 or prime == 3 or prime == 5 or prime == 7 or prime == 11:
        print(prime)
    elif prime_time <= 100:
        print(prime_time)

#Exercise 3

"""Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors"""

user_age = "How old are you? "

while True:
    age = int(input(user_age))
    if age < 18:
        print(f"You're a kid!")
    elif age < 65 :
        print(f"You're an adult!")
    else:
        print(f"You're a Senior citizen!")