#!/usr/bin/env python

import pytest

from circuit import Vector


@pytest.fixture
def v():
    return Vector(0, 0)


def test_up(v):
    assert v.x == 0 and v.y == 0
    v = v.move('U')
    assert v.x == 0 and v.y == 1


def test_down(v):
    assert v.x == 0 and v.y == 0
    v = v.move('D')
    assert v.x == 0 and v.y == -1


def test_left(v):
    assert v.x == 0 and v.y == 0
    v = v.move('L')
    assert v.x == -1 and v.y == 0


def test_right(v):
    assert v.x == 0 and v.y == 0
    v = v.move('R')
    assert v.x == 1 and v.y == 0


def test_len_dunder(v):
    assert len(v) == 0
    v.x = 3
    v.y = -5
    assert len(v) == 8


