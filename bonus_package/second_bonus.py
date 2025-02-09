import numpy as np

def trapezoidal_rule(time, power):
    total_energy = 0
    for i in range(1, len(time)):
        dt = time[i] - time[i - 1]
        avg_power = (power[i] + power[i - 1]) / 2
        total_energy += dt * avg_power
    return total_energy

def simpsons_rule(time, power):
    if len(time) % 2 == 0:
        raise ValueError("Simpson's rule requires an odd number")

    total_energy = power[0] + power[-1]
    for i in range(1, len(power) - 1, 2):
        total_energy += 4 * power[i]
    for i in range(2, len(power) - 1, 2):
        total_energy += 2 * power[i]

    dt = (time[-1] - time[0]) / (len(time) - 1)
    total_energy *= dt / 3
    return total_energy

time_hours = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
power_consumption = np.array([500, 480, 450, 600, 800, 950, 1000, 980, 920, 850, 700, 550, 500])

energy_trapezoidal = trapezoidal_rule(time_hours, power_consumption)
energy_simpsons = simpsons_rule(time_hours, power_consumption)

print("Total energy consumption with Trapezoidal Rule:", energy_trapezoidal, "MWh")
print("Total energy consumption with Simpson's Rule:", round(energy_simpsons, 2),  "MWh")

