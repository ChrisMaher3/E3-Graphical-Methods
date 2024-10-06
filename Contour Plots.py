import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.close()

    q = 1  

    coords = np.linspace(-2, 2, 101)
    x, y = np.meshgrid(coords, coords)

    z = q * (x**2 + y**2)

    dx, dy = np.gradient(z)  

    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'2D function: $Z = q(x^2 + y^2), q={q}$')

    contour_filled = plt.contourf(x, y, z, 20) 
    plt.set_cmap('coolwarm')  
    plt.colorbar(contour_filled)  

    contour_lines = plt.contour(x, y, z, 10, colors='black')  
    plt.clabel(contour_lines, inline=True, fontsize=8) 

    skip = 5  
    x_skipped, y_skipped = x[::skip, ::skip], y[::skip, ::skip]
    dx_skipped, dy_skipped = dx[::skip, ::skip], dy[::skip, ::skip]

    plt.quiver(x_skipped, y_skipped, dx_skipped, dy_skipped)

    plt.show()


if __name__ == '__main__':
    main()
