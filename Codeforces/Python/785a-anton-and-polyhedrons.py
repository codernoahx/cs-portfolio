def main():
    n = int(input())
    sides = 0

    for _ in range(n):
        polyhedron = input()
        # Depending on the polyhedron we'll choose how many sides to increment
        if polyhedron == "Tetrahedron":
            sides += 4
        elif polyhedron == "Cube":
            sides += 6
        elif polyhedron == "Octahedron":
            sides += 8
        elif polyhedron == "Dodecahedron":
            sides += 12
        # Else the polyhedron is a Icosahedron
        else:
            sides += 20
    print(sides)


if __name__ == "__main__":
    main()
