import random
import string

defined = []
classname = ''

alpha = 'abcdefghijklmnopqrstuwxyz'
def randomstring(size = 6):
    r = ''.join(random.choice(alpha) for _ in range(size))
    if r in defined or r is classname:
        randomstring(size)
    return r

f = open('junk.cpp', 'w')

classname = randomstring()

# first: writing the class
f.write(f'class {classname} {{\n')
for i in range(random.randint(1, 100)):
    r = randomstring()
    while r in defined:
        r = randomstring()

    t = random.choice(['int', 'float'])
    f.write(f'    {t} {r}();\n')
    defined.append([r, t])

f.write('};\n\n')

# second: defining methods
for element in defined:
    f.write(f'{element[1]} {classname}::{element[0]}() {{\n')
    for i in range(random.randint(4, 10)):
        r = randomstring()
        f.write(f'    int {r} = {random.randint(0, 100)};\n')

        if random.randint(0, 1) is 0:
            f.write(f'    int {randomstring()} = {random.randint(0, 100)};\n')
        else:
            f.write(f'    if({r} == {random.randint(0, 100)}) {{\n')
            f.write(f'        {r} = {random.randint(0, 100)};\n')
            f.write(f'    }}\n')
    f.write(f'    return {random.randint(0,100)};\n}}\n\n')

f.close()