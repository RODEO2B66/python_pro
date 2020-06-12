import sympy as sym
from sympy.plotting import plot
sym.init_printing(use_unicode=True)
% matplotlib inline

  a,b,c,x,y = sym.symbols("a  b c x y")

expr = x**2-12*x+8
expr

plot(expr(x,-20,20))
