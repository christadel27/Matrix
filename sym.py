import numpy as np
import matplotlib.pyplot as plt
import sympy
import ipywidgets as widgets

x = sympy.symbols('x')
f = 1 / (1 + x**2)
print(f)
# tambahan pelajaran
def func(p):
    x = np.linspace(-10, 10, 100)
    def inner_func(x):
        return 25/x
    if p != 0 : 
      y = inner_func(x)
      plt.plot(x, y)
      plt.scatter(p, inner_func(p))
      plt.title(f"x:{p} y:{inner_func(p):.2f}")
      plt.show()
    else : 
      print("division by zero undefined")    
    
widgets.interact(
    func,
    p=widgets.FloatSlider(value=5, min=-10, max=10, step=0.5)
    )