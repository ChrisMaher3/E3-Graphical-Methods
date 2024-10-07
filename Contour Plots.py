import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.close()

    q = 10

    coords = np.linspace(-2, 2, 101)
    x, y = np.meshgrid(coords, coords)

    z = q / (x**2 + y**2 )

    dx, dy = np.gradient(z)  

    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    contour_filled = plt.contourf(x, y, z, 20) 
    plt.set_cmap('coolwarm')  
    plt.colorbar(contour_filled)  

    plt.contour(x, y, z, 10, colors='black', linewidth = 0.5)  

    skip = 10
    x_skipped, y_skipped = x[::skip, ::skip], y[::skip, ::skip]  # note the indexing [start:end:skip]
    dx_skipped, dy_skipped = dx.T[::skip, ::skip], dy.T[::skip, ::skip]  # not

    plt.quiver(x_skipped, y_skipped, dx_skipped, dy_skipped, scale=0.8)
    #plt.savefig('contour plots 2.svg', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()
