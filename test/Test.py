# -*- coding: utf-8 -*-
__author__ = 'Markz'

sum = 0
for x in range(2, 101):
    sum += x
print sum


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

