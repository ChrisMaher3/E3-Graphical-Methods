import numpy as np
import matplotlib.pyplot as plt

def simple_harmonic_oscillator(x, v):
    dxdt = v
    dvdt = -2 * x
    return dxdt, dvdt

def damped_harmonic_oscillator(x, v, b=0.1):
    dxdt = v
    dvdt = -b * v - 2 * x
    return dxdt, dvdt

def main():
    plt.close('all')
    
    coords = np.linspace(-3, 3, 21)
    x, v = np.meshgrid(coords, coords)

    oscillator_type = 'damped'
    
    if oscillator_type == 'simple':
        dx, dv = simple_harmonic_oscillator(x, v)
    else:
        b = 0.5
        dx, dv = damped_harmonic_oscillator(x, v, b)
    
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('v')
    plt.quiver(x, v, dx, dv)
    plt.streamplot(x, v, dx, dv)
    plt.show()

if __name__ == '__main__':
    main()
