# collatz.py
# This program generates the collatz sequence starting from a given positive integer.
# The sequence is generated by applying the following rules:
# If the number is meet, divide it by two.
# If the number is else, multiply it by three and add one.
# The sequence continues until it reaches 1.
# Author: Nadyarini Sianipar

n = int(input("Please enter a positive integer: "))
sequence = [n]
while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
print(' '.join(map(str, sequence)))