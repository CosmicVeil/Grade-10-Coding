#Name: Mohan
# Purpose: Practice

for i in range(8):
    for j in range(i+1):
        print("*", end='')
    print()

for i in range(6):
    for j in range(i):
         print("", end='')
    print("#")

for i in range(5):
    for j in range(i+1):
        print(chr(j+65),end='')
    print()