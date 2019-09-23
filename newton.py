# Aaron Burns - Newton's Method
# A program which gets the approximates the square root of numbers
# Adpated from https://tour.golang.org/flowcontrol/8

def sqrt(x):
    # make and initial guess as to what the square root of x is
    z = 5
    # keep getting a better estimate for the sqrt of x 
    # until you are within 2 decimal places
    # "abs" returns postives integers of negitive numbers
    while abs(z*z - x >= 0.01):
        # get a better approximation for the sqrt
        z -= (z*z - x) / (2*z)
    return z

print(sqrt(8.0))