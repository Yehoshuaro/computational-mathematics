import numpy as np
import matplotlib.pyplot as plt

def sir_model(t, S, I, R, beta, gamma):
    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I
    return np.array([dS, dI, dR])

def rk4_step(f, t, S, I, R, beta, gamma, h):
    k1 = f(t, S, I, R, beta, gamma)
    k2 = f(t + h / 2, S + h * k1[0] / 2, I + h * k1[1] / 2, R + h * k1[2] / 2, beta, gamma)
    k3 = f(t + h / 2, S + h * k2[0] / 2, I + h * k2[1] / 2, R + h * k2[2] / 2, beta, gamma)
    k4 = f(t + h, S + h * k3[0], I + h * k3[1], R + h * k3[2], beta, gamma)
    return np.array([S, I, R]) + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

def simulate(beta, gamma, S0, I0, R0, days, h=0.1):
    t_values = np.arange(0, days, h)
    S, I, R = S0, I0, R0
    results = np.zeros((len(t_values), 3))

    for i, t in enumerate(t_values):
        results[i] = [S, I, R]
        S, I, R = rk4_step(sir_model, t, S, I, R, beta, gamma, h)

    return t_values, results[:, 0], results[:, 1], results[:, 2]

beta, gamma = 0.3, 0.1
S0, I0, R0 = 0.99, 0.01, 0.0
days = 100

t, S, I, R = simulate(beta, gamma, S0, I0, R0, days)

plt.figure(figsize=(8, 5))
plt.plot(t, S, label='Susceptible (S)')
plt.plot(t, I, label='Infected (I)')
plt.plot(t, R, label='Recovered (R)')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SIR Model - Virus Spread Over Time')
plt.legend()
plt.grid()
plt.show()
