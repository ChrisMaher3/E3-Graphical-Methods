import numpy as np
import matplotlib.pyplot as plt

def coupled_ode(t, z):
    x, y = z
    dxdt = y
    dydt = -x + (1 - x**2) * y
    return np.array([dxdt, dydt])

def rk4(f, t, z, dt):
    k1 = f(t, z)
    k2 = f(t + 0.5 * dt, z + 0.5 * dt * k1)
    k3 = f(t + 0.5 * dt, z + 0.5 * dt * k2)
    k4 = f(t + dt, z + dt * k3)
    return z + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

def plot_phase_space(isoclines=False):
    # Custom meshgrid for quiver and streamplot, adapted from your previous code
    coords = np.linspace(-3, 3, 21)
    X, Y = np.meshgrid(coords, coords)
    U = Y
    V = -X + (1 - X**2) * Y

    # Quiver and Streamline Plot
    plt.quiver(X, Y, U, V, color='lightgray')  # Quiver in light gray
    plt.streamplot(X, Y, U, V, color='blue', density=1.5)  # Streamlines in blue

    # Optional isoclines
    if isoclines:
        plt.contour(X, Y, Y, levels=[0], colors='red', linestyles='dashed')  # Red isocline for dy/dt = 0
        plt.contour(X, Y, -X + (1 - X**2) * Y, levels=[0], colors='green', linestyles='dashed')  # Green for dx/dt = 0

initial_conditions = [(3, 3), (-2, 2), (0.1, 0.1), (0.5, 1)]
t0, tf, dt = 0, 30, 0.1
t_values = np.arange(t0, tf, dt)

plt.figure(figsize=(15, 10))

# Phase space plot with quiver and streamlines
plt.subplot(2, 2, 1)
plot_phase_space(isoclines=True)
plt.title('Quiver and Streamline Plot')
plt.xlabel('x')
plt.ylabel('y')

# Solve the system for each initial condition and plot results
for x0, y0 in initial_conditions:
    z = np.zeros((len(t_values), 2))
    z[0] = [x0, y0]
    
    # Use RK4 to solve the coupled ODEs
    for i in range(1, len(t_values)):
        z[i] = rk4(coupled_ode, t_values[i-1], z[i-1], dt)

    x_values, y_values = z[:, 0], z[:, 1]

    # Time series plot for x(t)
    plt.subplot(2, 2, 2)
    plt.plot(t_values, x_values, label=f'x0={x0}, y0={y0}')
    plt.xlabel('time')
    plt.ylabel('x(t)')
    plt.title('Time Series of x(t)')
    plt.legend()
    
    # Time series plot for y(t)
    plt.subplot(2, 2, 3)
    plt.plot(t_values, y_values, label=f'x0={x0}, y0={y0}')
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.title('Time Series of y(t)')
    plt.legend()

    # Phase space plot for x vs. y
    plt.subplot(2, 2, 4)
    plt.plot(x_values, y_values, label=f'IC: ({x0}, {y0})')

# Final Phase space plot
plt.subplot(2, 2, 4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Phase Space Diagram')
plt.legend()
plt.tight_layout()
plt.savefig('Limit Cycle.svg', bbox_inches='tight')
plt.show()
