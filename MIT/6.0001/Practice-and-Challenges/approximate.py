cube = -15.625

epsilon = 0.01
increment = 0.0001
num_guess = 0
guess = 0.0

negative = cube < 0
cube = abs(cube)

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guess += 1
if abs(guess**3 - cube) >= epsilon:
    print("Failed to find the cube root.")
else:
    if negative:
        guess = -guess
        cube = -cube
    print(f"Cube root of {cube} is {guess} and number of guess it took was {num_guess}.")