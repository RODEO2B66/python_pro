#常微分方程式 2f'(x)+5f(x)=0

import sympy as sym
from sympy.plotting import plot
sym.init_printing(use_unicode=True)
% matplotlib inline


eq = sym.Eq(2 * f(x).diff(x, 1 ) + 5* f(x) )
eq

ans = sym.dsolve(eq)
print(ans)
ans

Eq(f(x), C1*exp(-5*x/2))

ans = sym.dsolve(eq, ics={f(0):1})
print(ans)
ans
Eq(f(x), exp(-5*x/2))

plot(ans,rhs, (x, -10, 10))
