# squareroot.py
#
# Author: Nadyarini Sianipar

def sqrt(x):
    """
    Approximates the square root of a positive number using the Newton-Raphson method.
    """
    estimate = x / 2.0 # initial guess for the square root
        
    # lambda function
    update_estimate = lambda e: (e + x / e) / 2.0
    # 
    while True:
        new_estimate = update_estimate(estimate)
        if abs(new_estimate - estimate) < 1e-10:
            break
        estimate = new_estimate

    return new_estimate
# Get user input and compute the square root
def main():
    while True:
        try:
            num = float(input("Please enter a positive number: "))
            if num > 0:
                break
            else :
                print("Error: Please enter a positive number.")
        except ValueError :
            print("Error : Invalid input. Please enter a number.")
    # calculate the square root
    result = sqrt(num)

    # Output the result rounded to one decimal place
    print(f"The square root of {num} is approx. {round(result, 1)}.")

if __name__ == "__main__" :
    main()
