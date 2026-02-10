cube = float(input("Cube: "))
epsilon = 0.01
num_guesses = 0

# For negative cube roots
negative = cube < 0
cube = abs(cube)
# For cube roots greater than or equal to 1
if cube >= 1:
    low = 1.0
    high = cube
# For cube roots between 0 and 1
else:
    low = cube
    high = 1.0
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
   if guess**3 < cube:
       # look only in upper half search space
       low = guess
   else:
       # look only in lower half search space
       high = guess
   # next guess is halfway in search space
   guess = (high + low)/2.0
   num_guesses += 1
if negative:
    guess = -guess
    cube = -cube
print(f"num_guesses = {num_guesses}")
print(f"{guess} is close to the cube root of {cube}")
