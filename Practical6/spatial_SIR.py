#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt


#array of all susceptiblw population
population = np. zeros ( (100, 100) ) #initialize a 100x100 matrix with zeros

#choose a random infected person from the array
outbreak = np.random. choice (range (100), 2)
population [outbreak [0], outbreak [1]] = 1 #set the outbreak location to 1

#draw thw wanted heat map using imshow 
plt. figure (figsize = (6, 4), dpi= 150)
plt. imshow (population, cmap = 'viridis', interpolation ='nearest')

#set the parameters of the SIR model
beta = 0.3 #infection rate
gamma = 0.1 #recovery rate
num_time_points = 100 #number of time points to simulate

#simulate the infection process
for t in range (num_time_points):
    #calculate the number of susceptible, infected, and recovered individuals at the current time point
    infected_indices = np.where (population == 1)
    for i in range(len(infected_indices[0])):
        x, y = infected_indices[0][i], infected_indices[1][i]
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 100 and 0 <= new_y < 100:
                    if population[new_x, new_y] == 0:  # the neighboring cell is susceptible
                        if np.random.random() < beta:  # the neighboring cell is infected with probability beta
                            population[new_x, new_y] = 1
    #revore the infected individuals with probability gamma
    recovered_indices = np.where(population == 1)
    for i in range(len(recovered_indices[0])):
        if np.random.random() < gamma:
            population[recovered_indices[0][i], recovered_indices[1][i]] = 2

#plot the final population state
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Final Population State")
plt.colorbar()  # add the color bar to the plot
plt.show()