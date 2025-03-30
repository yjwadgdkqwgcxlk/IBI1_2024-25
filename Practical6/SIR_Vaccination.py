import numpy as np
import matplotlib.pyplot as plt

# Define population size
N = 10000

# Define initial populations
I = 1   # Initial infected population
S = N - I  # Initial susceptible population
R = 0   # Initial recovered population

# Define model parameters
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Define the vaccination rates (fraction of susceptible population vaccinated per time step)
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Create a plot for each vaccination rate
plt.figure(figsize=(8, 6), dpi=150)

# Run the SIR model for each vaccination rate
for vaccination_rate in vaccination_rates:
    # Initialize arrays to store the values of S, I, and R for this vaccination rate
    S_temp = S
    I_temp = I
    R_temp = R

    # Arrays to track the population dynamics over time
    S_array = [S_temp]
    I_array = [I_temp]
    R_array = [R_temp]

    # Run the SIR model for 1000 time steps
    for t in range(1000):
        # Update the number of infected individuals
        I_temp = I_temp + beta * S_temp * I_temp / N
        
        # Update the number of recovered individuals
        R_temp = R_temp + gamma * I_temp
        
        # Update the number of susceptible individuals
        S_temp = S_temp - beta * S_temp * I_temp / N - gamma * I_temp - vaccination_rate * S_temp
        
        # Append the updated values to arrays
        S_array.append(S_temp)
        I_array.append(I_temp)
        R_array.append(R_temp)

    # Plot the infected population for each vaccination rate
    plt.plot(I_array, label=f'Vaccination Rate = {int(vaccination_rate * 100)}%')

# Final plot settings
plt.xlabel('Time')
plt.ylabel('Infected Population')
plt.legend()
plt.title('SIR Model with Different Vaccination Rates')
plt.show()