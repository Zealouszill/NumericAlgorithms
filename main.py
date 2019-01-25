# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

pip install pytest

pytest "filename".py
"""


def AND(a, b):
    """
    returns a single character '0'
    representing a logical AND of
    bit a and bit b (which are each 0 or 1

    >>> AND('0', '1')
    '0'
    >>> AND('1', '1')
    '1'
    """

    if (a == '1'):
        if (b == '1'):
            return '1'
        else:
            return '0'
    else:
        return '0'


def OR(a, b):
    """
    returns a single character '0'
    representing a logical AND of
    bit a and bit b (which are each 0 or 1

    >>> AND('0', '1')
    '0'
    >>> AND('1', '1')
    '1'
    """

    if (a == '1'):
        return '1'

    else:
        if (b == '1'):
            return '1'
        else:
            return '0'


def XOR(a, b):
    if (a == '1'):
        if (b == '1'):
            return '0'
        else:
            return '1'
    else:
        if (b == '1'):
            return '1'
        else:
            return '0'


def PLUS2(a, b):

    if a == '1':
        if b == '0':
            return '01'
    else:
        return a + b


def test_and():
    assert AND('0', '0') == '0'
    assert AND('0', '1') == '0'
    assert AND('1', '0') == '0'
    assert AND('1', '1') == '1'

    assert OR('0', '0') == '0'
    assert OR('0', '1') == '1'
    assert OR('1', '0') == '1'
    assert OR('1', '1') == '1'

    assert XOR('0', '0') == '0'
    assert XOR('0', '1') == '1'
    assert XOR('1', '0') == '1'
    assert XOR('1', '1') == '0'

    assert PLUS2('0', '0') == '00'
    assert PLUS2('0', '1') == '01'
    assert PLUS2('1', '0') == '01'
    assert PLUS2('1', '1') == '11'

















