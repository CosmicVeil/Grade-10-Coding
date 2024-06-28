# Name: Mohan
# Purpose: Print colors

import random

colors = ["red", "blue", "green", "yellow", "orange"]

for i in range(5):
    index = random.randint(0,4)
    print(colors[index])

