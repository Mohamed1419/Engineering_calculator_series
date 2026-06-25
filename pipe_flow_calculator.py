import math
import matplotlib.pyplot as plt
import numpy as np

def get_inputs():
    print("--- Flow Pipe Calculator ---\n")
    diameter = float(input("Enter the pipe diameter (in meters): "))
    length = float(input("Enter the pipe length (in meters): "))
    velocity = float(input("Enter the flow velocity (in meters per second): "))
    density = float(input("Enter the fluid density (in kg/m^3): "))
    viscosity = float(input("Enter the fluid viscosity (in Pa.s): "))
    roughness = float(input("Enter the pipe roughness (in meters): "))
    return diameter, length, velocity, density, viscosity, roughness

def calculate_reynolds_number(density, velocity, diameter, viscosity):
    return (density * velocity * diameter) / viscosity 

def calculate_friction_factor(reynolds_number, roughness, diameter):
    if reynolds_number < 2300:
        friction_factor = 64 / reynolds_number  # Laminar flow  
    else:
        friction_factor = 0.25 / (math.log10((roughness / (3.7 * diameter)) + (5.74 / (reynolds_number ** 0.9)))) ** 2  # Turbulent flow
    return friction_factor

def calculate_results(diameter, length, velocity, density, friction_factor):
    pressure_drop = (friction_factor * (length/diameter) * 0.5 *density * velocity**2)
    flow_rate = (math.pi * (diameter/2)**2) * velocity
    return pressure_drop, flow_rate

def plot_pressure_drop(diameter, length, density, viscosity, roughness):
    velocities = np.linspace(0.1, 5, 100)
    pressure_drops = []

    for v in velocities:
        re = calculate_reynolds_number(density, v, diameter, viscosity)
        ff = calculate_friction_factor(re, roughness, diameter)
        pd = ff * (length / diameter) * 0.5 * density * v ** 2
        pressure_drops.append(pd)

    plt.figure(figsize=(10, 6))
    plt.plot(velocities, pressure_drops, color='steelblue', linewidth=2)
    plt.title('Pressure Drop vs Flow Velocity')
    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Pressure Drop (Pa)')
    plt.grid(True)
    plt.axvline(x=1.5, color='red', linestyle='--', label='Your input velocity')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    diameter, length, velocity, density, viscosity, roughness = get_inputs()

    reynolds_number = calculate_reynolds_number(density, velocity, diameter, viscosity)

    print(f"\nReynolds Number: {reynolds_number:.2f}")

    if reynolds_number < 2300:
        regime = "Laminar"
    elif reynolds_number < 4000:
        regime = "Transitional"
    else:
        regime = "Turbulent"

    print(f"Flow regime: {regime}")

    friction_factor = calculate_friction_factor(reynolds_number, roughness, diameter)
    pressure_drop, flow_rate = calculate_results(diameter, length, velocity, density, friction_factor)

    print(f"\n--- RESULTS ---")
    print(f"Reynolds Number:  {reynolds_number:.2f}")
    print(f"Flow Regime:      {regime}")
    print(f"Friction Factor:  {friction_factor:.6f}")
    print(f"Pressure Drop:    {pressure_drop:.2f} Pa")
    print(f"Flow Rate:        {flow_rate:.6f} m³/s")
    plot_pressure_drop(diameter, length, density, viscosity, roughness)

if __name__ == "__main__":
    main()