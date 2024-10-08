import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def lotka(t, y, a, b, c, d):
    x, v = y 
    dxdt = a * x - b * x * v  
    dvdt = c * x * v - d * v  
    dydt = np.array([dxdt, dvdt])
    return dydt

def plot_lotka_volterra(a, b, c, d, x0=4, v0=2, tf=10, n=1001):
    lfun = lambda t, y: lotka(t, y, a, b, c, d)
    
    y0 = (x0, v0)
    
    t0 = 0  
    t = np.linspace(t0, tf, n)
    
    result = integrate.solve_ivp(fun=lfun, 
                                 t_span=(t0, tf),
                                 y0=y0,  
                                 method="RK45",  
                                 t_eval=t)  
    
    x, v = result.y 
    t = result.t 
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 6)) 
    ax[0].plot(t, x, label=r"Rabbits")
    ax[0].plot(t, v, label=r"Foxes")
    ax[0].set_xlabel(r"Time")
    ax[0].set_ylabel(r"Number")
    ax[0].legend(loc='upper right')
    
    ax[1].plot(x, v, 'k')
    ax[1].set_xlabel(r"Rabbit population")
    ax[1].set_ylabel(r"Foxes population")
    
    plt.tight_layout()
    plt.savefig(f"a={a}, b={b}, c={c}, d={d}.svg", bbox_inches='tight')
    plt.show()


parameter_sets = [
    {"a": 3, "b": 2, "c": 0.5, "d": 1},
    {"a": 4, "b": 2, "c": 0.5, "d": 1}, 
    {"a": 4, "b": 5, "c": 0.5, "d": 1},
    {"a": 4, "b": 2, "c": 0.3, "d": 1},
    {"a": 4, "b": 2, "c": 0.5, "d": 3},
]
for params in parameter_sets:
    a = params["a"]
    b = params["b"]
    c = params["c"]
    d = params["d"]
    
    plot_lotka_volterra(a, b, c, d)