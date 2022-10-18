import sympy as smp
from sympy import Derivative, Function, symbols, Subs
from sympy.abc import x, y
x, y = smp.symbols('x y')
def f(x, y):
  return 3*x**2*y+x**2-y**3
smp.Derivative(f(x,y), x) # x e gore kismi turev sembolu
 # x e gore kismi turev sonucu
smp.Derivative(f(x, y), x).doit() # x e gore kismi turev sonucu
smp.Derivative(f(x,y), y) # y e gore kismi turev sembolu
# y e gore kismi turev sonucu
smp.Derivative(f(x,y), y).doit()