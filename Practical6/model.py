#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Define population
N = 10000
#Define initial infected population
I = 1
#Define initial susceptible population
S = N - I
#Define initial recovered population
R = 0  
#Define initial infection rate
beta = 0.3
#Define recovery rate
gamma = 0.05

S_array = [S]
I_array = [I]   
R_array = [R]

# stimulate 1000 time points
for t in range(1000):
    # calculate number of infected individuals
    I = I + beta * S * I / N
    # calculate number of recovered individuals
    R = R + gamma * I
    # calculate number of susceptible individuals  
    S = S - beta * S * I / N - gamma * I
    # append values to arrays
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

# plot the graph
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_array, label='Susceptible')
plt.plot(I_array, label='Infected')
plt.plot(R_array, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('SIR Model')
plt.show()