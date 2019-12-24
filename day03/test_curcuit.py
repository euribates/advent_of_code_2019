#!/usr/bin/env python

import pytest

from circuit import Vector
from circuit import Circuit


@pytest.fixture
def circuit():
    return Circuit()


def test_go_up(circuit):
    assert circuit.cursor.x == 0 and circuit.cursor.y == 0
    circuit.go('U', 6, 1)
    assert circuit.cursor.x == 0 and circuit.cursor.y == 6
    for i in range(1, 7):
        assert circuit.board[(0, i)] == 1


def test_go_right(circuit):
    assert circuit.cursor.x == 0 and circuit.cursor.y == 0
    circuit.go('R', 6, 1)
    assert circuit.cursor.x == 6 and circuit.cursor.y == 0
    for x in range(1, 7):
        assert circuit.board[(x, 0)] == 1


def test_go_down(circuit):
    assert circuit.cursor.x == 0 and circuit.cursor.y == 0
    circuit.go('D', 6, 1)
    assert circuit.cursor.x == 0 and circuit.cursor.y == -6
    for i in range(-6, 0):
        assert circuit.board[(0, i)] == 1


def test_go_left(circuit):
    assert circuit.cursor.x == 0 and circuit.cursor.y == 0
    circuit.go('L', 6, 1)
    assert circuit.cursor.x == -6 and circuit.cursor.y == 0
    for x in range(-6, 0):
        assert circuit.board[(x, 0)] == 1


def test_sample_1(circuit):
    circuit.run('U7,R6,D4,L4', 1)
    circuit.dump(21, 21)


def test_sample_2(circuit):
    circuit.run('R8,U5,L5,D3', 2)
    circuit.dump(21, 21)


def test_two_layers(circuit):
    circuit.run('U7,R6,D4,L4', 1)
    circuit.run('R8,U5,L5,D3', 2)
    circuit.dump(21, 21)
    for (dist, x, y, layer) in circuit.cross:
        print(dist, Vector(x, y), layer)


def test_run1(circuit):
    circuit.run("R75,D30,R83,U83,L12,D49,R71,U7,L72", 1)
    circuit.run("U62,R66,U55,R34,D71,R55,D58,R83", 2)
    print(sorted(circuit.cross))
    circuit.dump_png()


def test_run2(circuit):
    circuit.run("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", 1)
    circuit.run("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 2)
    print(sorted(circuit.cross))
    circuit.dump_png()


SAMPLES = [
    ('U7,R6,D4,L4', 3, 3, 20),
    ('R8,U5,L5,D3', 3, 3, 20),
    ('U7,R6,D4,L4', 6, 5, 15),
    ('R8,U5,L5,D3', 6, 5, 15),
]


@pytest.mark.parametrize("path,x,y,distance", SAMPLES)
def test_len_of_path_to_1(path, x, y, distance):
    c = Circuit()
    length = c.len_of_path_to(path, x, y)
    assert length == distance


def test_part_2_sample_1():
    path_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    path_2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    c = Circuit()
    c.run(path_1, 1)
    c.run(path_2, 2)
    results = []
    for (distance, x, y, layer) in c.cross:
        length = c.len_of_path_to(path_1, x, y)  \
               + c.len_of_path_to(path_2, x, y)
        results.append(length)
    assert min(results) == 610


def test_part_2_sample_2():
    path_1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    path_2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    c = Circuit()
    c.run(path_1, 1)
    c.run(path_2, 2)
    results = []
    for (distance, x, y, layer) in c.cross:
        length = c.len_of_path_to(path_1, x, y)  \
               + c.len_of_path_to(path_2, x, y)
        results.append(length)
    assert min(results) == 410


if __name__ == "__main__":
    pytest.main()
