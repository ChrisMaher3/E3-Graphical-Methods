import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.close()

    x = np.linspace(0, 2, 101)
    y = np.linspace(0, 2, 101)
    X, Y = np.meshgrid(x, y)

    Vx = np.cos(X) * Y
    Vy = np.sin(X) * X

    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.quiver(X[::5, ::5], Y[::5, ::5], Vx[::5, ::5], Vy[::5, ::5], pivot='mid', label='$v_x$ = cos($x$)$y$, $v_y$ = sin($y$)$x$')
    plt.legend(loc='lower left')
    plt.show()

if __name__ == '__main__':
    main()
