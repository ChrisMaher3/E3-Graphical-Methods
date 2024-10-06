import numpy as np
import matplotlib.pyplot as plt

def lotka_volterra(t, z, a, b, c, d):
    x, y = z
    dxdt = a * x - b * x * y
    dydt = c * x * y - d * y
    return np.array([dxdt, dydt])

def rk4(f, t, z, dt, a, b, c, d):
    k1 = f(t, z, a, b, c, d)
    k2 = f(t + 0.5 * dt, z + 0.5 * dt * k1, a, b, c, d)
    k3 = f(t + 0.5 * dt, z + 0.5 * dt * k2, a, b, c, d)
    k4 = f(t + dt, z + dt * k3, a, b, c, d)
    return z + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

a, b, c, d = 4.0, 2.0, 13.0, 1.0
x0, y0 = 4.0, 2.0
t0, tf, dt = 0, 10, 0.1
t_values = np.arange(t0, tf, dt)
z = np.zeros((len(t_values), 2))
z[0] = [x0, y0]

for i in range(1, len(t_values)):
    z[i] = rk4(lotka_volterra, t_values[i-1], z[i-1], dt, a, b, c, d)

x_values, y_values = z[:, 0], z[:, 1]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t_values, x_values, label='rabbits', color='blue')
plt.plot(t_values, y_values, label='foxes', color='green', linestyle='--')
plt.xlabel('time')
plt.ylabel('number')
plt.title('Population over Time')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, y_values, color='red')
plt.xlabel('rabbits')
plt.ylabel('foxes')
plt.title('Phase Space Diagram')

plt.tight_layout()
plt.show()