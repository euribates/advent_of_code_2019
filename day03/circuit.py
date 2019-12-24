#!/usr/bin/env python

from collections import defaultdict

DIRECTIONS = ['U', 'R', 'L', 'D']

UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'U':
            return Vector(self.x, self.y + 1)
        elif direction == 'R':
            return Vector(self.x + 1, self.y)
        elif direction == 'D':
            return Vector(self.x, self.y - 1)
        elif direction == 'L':
            return Vector(self.x - 1, self.y)
        else:
            raise ValueError('Direction must be U, R, L or D')

    def __len__(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return '<{}, {}>'.format(self.x, self.y)


class Circuit:

    def __init__(self):
        self.board = defaultdict(int)
        self.origin = Vector(0, 0)
        self.cursor = Vector(0, 0)
        self.cross = []
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0

    def dump_png(self, width=501, height=501):
        from PIL import Image
        img = Image.new('RGB', (width, height))

        def scalemap(x, y):
            x = x + (width // 2)
            y = (height // 2) - y
            return x, y

        for y in range(height//2, (-height//2)-1, -1):
            for x in range(-width//2, (width//2)+1):
                v = self.board[(x, y)]
                pos = scalemap(x, y)
                if v == 1:
                    img.putpixel(pos, (255, 64, 64))
                elif v == 2:
                    img.putpixel(pos, (64, 255, 64))
                elif v == 3:
                    img.putpixel(pos, (255, 255, 64))
        img.save('circuit.png')

    def dump(self, width=11, height=11):
        print('circuit:')
        for y in range(height//2, (-height//2)-1, -1):
            for x in range(-width//2, (width//2)+1):
                v = self.board[(x, y)]
                if x == 0 and y == 0:
                    print('o', end='')
                elif v == 0:
                    print(' ', end='')
                elif v == 1:
                    print('░', end='')
                elif v == 2:
                    print('▒', end='')
                elif v == 3:
                    print('▓', end='')
                else:
                    print('E', end='')
            print()

    def go(self, direction: str, number=1, layer=0):
        for i in range(number):
            self.cursor = self.cursor.move(direction)
            prev_value = self.board[(self.cursor.x, self.cursor.y)]
            if prev_value and prev_value != layer:
                dist = len(self.cursor)
                self.cross.append(
                    (dist, self.cursor.x, self.cursor.y, layer)
                )
            self.board[(self.cursor.x, self.cursor.y)] = prev_value | layer
        self.min_x = min(self.min_x, self.cursor.x)
        self.min_y = min(self.min_y, self.cursor.y)
        self.max_x = max(self.max_x, self.cursor.x)
        self.max_y = max(self.max_x, self.cursor.x)


    def len_of_path_to(self, path, x, y):
        self.cursor = Vector(0, 0)
        steps = path.split(',')
        counter = 0
        for step in steps:
            direction = step[0:1]
            size = int(step[1:])
            for _ in range(size):
                self.cursor = self.cursor.move(direction)
                counter += 1
                # print(f'{counter:+10} {self.cursor.x} {self.cursor.y} == {x} {y}')
                if self.cursor.x == x and self.cursor.y == y:
                    return counter
                

    def run(self, path, layer):
        self.cursor = Vector(0, 0)
        steps = path.split(',')
        for step in steps:
            direction = step[0:1]
            size = int(step[1:])
            self.go(direction, size, layer)
