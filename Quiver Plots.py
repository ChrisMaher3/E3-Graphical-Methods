import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.close()

    x1, y1 = np.meshgrid(np.arange(0, 2 * np.pi, 0.2), np.arange(0, 2 * np.pi, 0.2))
    vx1 = np.cos(x1)  
    vy1 = np.sin(y1) 

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))  

    ax[0].set_aspect('equal', adjustable='box') 
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].quiver(x1, y1, vx1, vy1, pivot='mid', label='$v_x$ = cos($x$), $v_y$ = sin($y$)')
    ax[0].legend(loc='upper right')

    x, y = np.meshgrid(np.linspace(0, 2 * np.pi, 101), np.linspace(0, 2 * np.pi, 101))
    vx = np.cos(x) * y
    vy = np.sin(x) * x
    
    ax[1].set_aspect('equal', adjustable='box')  
    ax[1].set_xlabel('x')  
    ax[1].set_ylabel('y')  

    q = ax[1].quiver(x[::5, ::5], y[::5, ::5], vx[::5, ::5], vy[::5, ::5], pivot='mid', 
                     label='$v_x$ = cos($x$) y, $v_y$ = sin($y$) x')

    ax[1].quiverkey(q, X=0.9, Y=-0.1, U=2, label=r'$2\frac{m}{s}$', labelpos='E', coordinates='axes')
    ax[1].legend(loc="lower left")

    #plt.savefig('Quiver Plots.svg', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()

