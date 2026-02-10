cube = -8
guess = 0

for i in range(1, int(abs(cube)) + 1):
    if i ** 3 >= abs(cube):
        guess = i
        break

if guess** 3 != abs(cube):
    print(f"{cube} is not a perfect cube, int guess is {guess}.")
else:
    if cube < 0:
        guess = -guess
    print(f"Cube root of {cube} is {guess}.")