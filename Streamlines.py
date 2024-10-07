import matplotlib.pyplot as plt
import numpy as np

def harmonic_oscillator(x, v, omega=1.0):
    dx = v
    dv = -omega**2 * x
    return dx, dv

def damped_harmonic_oscillator(x, v, b=0.2, omega=1.0):
    dx = v
    dv = -b * v - omega**2 * x
    return dx, dv

def main():
    plt.close('all')
    
    # Create a grid for position (x) and velocity (v)
    coords = np.linspace(-3, 3, 21)
    x, v = np.meshgrid(coords, coords)
    
    # Choose which system to plot: Uncomment one of these options.
    # For Simple Harmonic Oscillator (SHO)
    #dx, dv = harmonic_oscillator(x, v, omega=1.0)

    # For Damped Harmonic Oscillator
    dx, dv = damped_harmonic_oscillator(x, v, b=0.5, omega=1.0)

    # Plot configuration
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('Position (x)')
    plt.ylabel('Velocity (v)')
    
    # Set titles based on the oscillator chosen

    # Quiver plot (red vectors)
    plt.quiver(x, v, dx, dv)
  
    # Streamplot (blue streamlines)
    plt.streamplot(x, v, dx, dv)
    #plt.savefig('damped harmonic.svg', bbox_inches='tight')
    # Display the plot
    plt.show()

if __name__ == '__main__':
    main()
