cube = 8
# cube = -27
# cube = -0.125
# cube = -0.015625

epsilon = 0.001
num_guess = 0
negative = cube < 0
cube = abs(cube)

if cube >= 1:
    low = 1.0
    high = cube
else:
    low = cube
    high = 1.0

guess = (high + low) / 2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guess += 1 

if negative:
    cube = -cube
    guess = -guess
print(f"Cube root of {cube} is {guess} and it took us {num_guess} guesses.")