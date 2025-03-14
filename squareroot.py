# squareroot.py
#
# Author: Nadyarini Sianipar

def sqrt(a):
    """
    Approximates the square root of a positive number using the Newton-Raphson method.
    """
    if a <= 0:
        raise ValueError("Input must be a positive number.")
    # Initial guess
    x = a / 2.0
    # 
    while True:
        next_x = (x + a / x) / 2
        if abs(next_x -x) < 1e-10:
            break
        x = next_x
    return x
# Get user input and compute the square root
try:
    number = float(input("Please enter a positive number: "))
    if number <= 0:
        print("Please enter a positive number.")
    else:
        approximation = sqrt(number)
        print(f"The square root of {number} is approx. {approximation:.1f}.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
