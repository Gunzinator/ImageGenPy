import random

width = 128
height = 128
genstr = f"P3\n{width} {height}\n255\n"
for i in range(0, height):
    for j in range(0, width):
        genstr += f"{random.randint(0, 255)} {random.randint(0, 255)} {random.randint(0, 255)}\n"

with open("./rgb/gen1.ppm", "w") as f:
    f.write(genstr)