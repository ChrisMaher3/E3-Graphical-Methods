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
    quiver = plt.quiver(X[::5, ::5], Y[::5, ::5], Vx[::5, ::5], Vy[::5, ::5], pivot='mid')
    plt.quiverkey(quiver, X=1.8, Y=1.8, U=0.5, label='Vector Magnitude: 0.5', labelpos='E')
    plt.show()

if __name__ == '__main__':
    main()
