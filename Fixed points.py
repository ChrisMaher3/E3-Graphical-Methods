import numpy as np
import matplotlib.pyplot as plt

def verhulst(x, r, K):
    return r * x * (1 - x / K)

def runge_kutta(x0, t, r, K, dt):
    n = len(t)
    x = np.zeros(n)
    x[0] = x0
    
    for i in range(1, n):
        k1 = dt * verhulst(x[i-1], r, K)
        k2 = dt * verhulst(x[i-1] + 0.5 * k1, r, K)
        k3 = dt * verhulst(x[i-1] + 0.5 * k2, r, K)
        k4 = dt * verhulst(x[i-1] + k3, r, K)
        
        x[i] = x[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    return x

def plot_flow_on_line(r, K):
    x_vals = np.linspace(0, 2 * K, 400)
    dxdt_vals = verhulst(x_vals, r, K)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, dxdt_vals, label=f'r={r}, K={K}')
    plt.axhline(0, color='black', linestyle='--')
    plt.xlabel('Population (x)')
    plt.ylabel('Population Growth Rate (dx/dt)')
    plt.legend()
    plt.savefig(f'Flow on a Line for Verhulst Model (r={r}, K={K}).svg', bbox_inches='tight')
    plt.show()

def plot_population_growth(r, K, x0_list, t_max=10, dt=0.01):
    t = np.arange(0, t_max, dt)
    
    plt.figure(figsize=(8, 6))
    for x0 in x0_list:
        x = runge_kutta(x0, t, r, K, dt)
        plt.plot(t, x, label=f'x0={x0}')
    
    plt.xlabel('Time (t)')
    plt.ylabel('Population (x)')
    plt.legend()
    plt.savefig(f'Population Growth Over Time (r={r}, K={K}).svg', bbox_inches='tight')
    plt.show()

def experiment_conclusions():
    r_values = [0.5, 1, 1.5]
    K_values = [50, 100]
    initial_conditions = [5, 20, 50, 120]
    
    for r in r_values:
        for K in K_values:
            print(f"Exploring r={r}, K={K}")
            plot_flow_on_line(r, K)
            plot_population_growth(r, K, initial_conditions)

if __name__ == '__main__':
    experiment_conclusions()
