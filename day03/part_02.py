#!/usr/bin/env python

from circuit import Circuit


with open('input', 'r') as f:
    path_1 = f.readline().strip()
    path_2 = f.readline().strip()

c = Circuit()
c.run(path_1, 1)
c.run(path_2, 2)

results = []
for (distance, x, y, layer) in c.cross:
    length = c.len_of_path_to(path_1, x, y)  \
           + c.len_of_path_to(path_2, x, y)
    results.append(length)

print(f"Solution of first part is: {min(results)}")
