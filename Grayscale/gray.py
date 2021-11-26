import random

width = 128
height = 128
genstr = f"P2\n{width} {height}\n63\n"
for i in range(0, height):
    for j in range(0, width):
        genstr += str(random.randint(0, 63)) + " "
    genstr += "\n"

with open("gen1.pgm", "w") as f:
    f.write(genstr)