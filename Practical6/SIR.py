# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define initial conditions
N = 10000
S = N - 1  # susceptible
I = 1      # infected
R = 0      # recovered
beta = 0.3
gamma = 0.05

# Store history
S_array = [S]
I_array = [I]
R_array = [R]

# Simulate over 1000 time steps
for _ in range(1000):
    # Calculate new infections and recoveries using binomial sampling
    new_infections = np.random.binomial(S, beta * I / N)
    new_recoveries = np.random.binomial(I, gamma)

    # Update compartments
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries

    # Prevent negative values (safety check)
    S = max(S, 0)
    I = max(I, 0)
    R = max(R, 0)

    # Save to arrays
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

# Plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_array, label='Susceptible')
plt.plot(I_array, label='Infected')
plt.plot(R_array, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Stochastic SIR Model')
plt.grid()
plt.show()
