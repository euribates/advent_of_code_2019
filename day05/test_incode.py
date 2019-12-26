#!/usr/bin/env python

import pytest

from intcode import IntCode


def test_example1():
    """Example 1: 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2)
    """
    int_code = IntCode()
    int_code.set_memory("1,0,0,0,99")
    assert int_code.mem.dump() == "1,0,0,0,99"
    int_code.run()
    assert int_code.mem.dump() == "2,0,0,0,99"


def test_example2():
    """Example 2: 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6)
    """
    p = IntCode("2,3,0,3,99")
    p.run()
    assert p.mem.dump() == "2,3,0,6,99"


def test_example3():
    """Example 3: 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801)
    """
    assert IntCode("2,4,4,5,99,0").run().mem.dump() == "2,4,4,5,99,9801"


def test_example4():
    """Example 4: 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99
    """
    assert IntCode("1,1,1,4,99,5,6,0,99").run().mem.dump() == "30,1,1,4,2,5,6,0,99"


if __name__ == "__main__":
    pytest.main()

