import math
import os
# import numpy



distance = 0
elapsedTime = 0

height = 120.0

box = [(int)(x < 60) for x in range(0, 120)]

def draw():
    data = []
    for y in range(0, 120):
        perspective = y / height
        # value = 1 if box[(int)(1200 * (1 - perspective)**2 + distance) % 120] > 0 else 0
        value = 1 if box[(int)(400 * (1 - perspective)**3 + distance) % 120] > 0 else 0


        data.append(value)

    
    return data
        




grass = []

for i in range(0, 120):

    elapsedTime += 2
    
    mapping = draw()

    grass.append(mapping)

    distance += 1



# Save the mapping
# with open(r'C:\Users\ammar\Documents\Year2\Spring\ece243\project\clipmapping.txt', 'w') as file:
with open(r'C:\Users\ammar\Documents\Year2\Spring\ece243\project\mapping.txt', 'w') as file:

    file.write(str(grass).replace('[', '{').replace(']', '}'))
file. close()


