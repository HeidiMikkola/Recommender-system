from random import random

input = open('set.tsv')
output = open('shortened.tsv', 'w')

for i, line in enumerate(input):
    if random() < 0.1:
        output.write(line)

input.close()
output.close()