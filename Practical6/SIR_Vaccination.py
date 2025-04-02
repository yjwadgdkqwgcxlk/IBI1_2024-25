#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#set initial values
N = 10000
I_initial, S_initial, R_initial = 1, N-1, 0
beta, gamma = 0.3, 0.05

#set vaccination rates
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

#initialize plot
plt.figure(figsize=(10,6), dpi=120)

#run simulation for each vaccination rate
for rate in vaccination_rates:
    vaccinated = rate * N
    S, I, R = S_initial - vaccinated, I_initial, R_initial
    S1, I1, R1 = [S], [I], [R]

    #run simulation for 1000 time steps
    for _ in range(1000):
        new_infections = beta * S * I / N
        new_recoveries = gamma * I
        
        # update S, I, R
        S_new = S - new_infections 
        I_new = I + new_infections - new_recoveries
        R_new = R + new_recoveries 
        
        # make sure population doesn't go below zero
        S = max(S_new, 0)
        I = max(I_new, 0)
        R = max(R_new, 0)
        
        # append to history
        S1.append(S)
        I1.append(I)
        R1.append(R)
    
    plt.plot(I1, label=f'Vaccination Rate={int(rate*100)}%')

plt.xlabel('Time'); plt.ylabel('Infected Population')
plt.title('SIR Model with Vaccination (Corrected)')
plt.legend(); plt.grid()
plt.show()