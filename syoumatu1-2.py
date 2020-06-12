# -*- coding: utf-8 -*-

from sympy import *

var("x")
equation = Eq(a*x**2 + b*x + c, 0)
answer = solve(equation)
print(answer)
