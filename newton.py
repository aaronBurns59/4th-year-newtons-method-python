# Aaron Burns - Newton's Method
# A program which gets the approximates the square root of numbers
# Adpated from https://tour.golang.org/flowcontrol/8

# testing how a cpu does square root function
def sqrt(x):
    # make and initial guess as to what the square root of x is
    z = 5
    z -= (z*z - x) / (2*z)
    return z

print(sqrt(25))