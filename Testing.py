
rows = 5

for r in range(rows):

    for c in range(rows, r, -1):
        print(" ", end="")
    for c in range(1,r+1):
        print("b", end=" ")

    print()


rows = 5

for r in range(rows, 0, -1):

    for c in range(rows-r):
        print(" ", end="")
    for c in range(rows-r, rows):
        print(c+1, end="")
    print()


for r in range(rows+1):
    for c in range(1, r+1):
        print(c, end="")
    print()

for r in range(rows, 0 ,-1):
    for c in range(rows-r):
        print(" ", end="")
    for c in range(r, 0, -1):
        print(c, end=" ")
    print()