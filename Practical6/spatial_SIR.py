# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Pseudocode:
# * Step 1: Initialize 100x100 population array, all susceptible (0)
# * Step 2: Randomly infect one individual (set to 1)
# * Step 3: For each time step:
#     - Infect susceptible neighbors of infected individuals (probability = beta)
#     - Infected individuals recover (probability = gamma)
#     - Save snapshots at selected time points (e.g., t=0,10,50,99)
# * Step 4: Plot snapshots to show disease spread
# -------------------------------

# Initialize population grid (0 = susceptible, 1 = infected, 2 = recovered)
population = np.zeros((100, 100), dtype=int)

# Randomly choose one person to be initially infected
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # Set to infected

# Parameters
beta = 0.3   # infection probability per neighbor
gamma = 0.1  # recovery probability per infected individual
num_time_points = 100

# Store snapshots at selected time points
snapshots = []

for t in range(num_time_points):
    new_population = population.copy()

    # Infection step: infected individuals may infect 8 neighbors
    infected_indices = np.where(population == 1)
    for i in range(len(infected_indices[0])):
        x, y = infected_indices[0][i], infected_indices[1][i]
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < 100 and 0 <= ny < 100:
                    if population[nx, ny] == 0:  # susceptible
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1

    # Recovery step: infected individuals may recover
    for i in range(len(infected_indices[0])):
        x, y = infected_indices[0][i], infected_indices[1][i]
        if np.random.random() < gamma:
            new_population[x, y] = 2  # recovered

    # Update population state
    population = new_population.copy()

    # Save snapshot for visualization
    if t in [0, 10, 50, 99]:
        snapshots.append((t, population.copy()))

# Plot snapshots at selected time points
for t, snap in snapshots:
    plt.figure(figsize=(5, 4))
    plt.imshow(snap, cmap='viridis', interpolation='nearest')
    plt.title(f"Time step {t}")
    plt.colorbar(label='0=Susceptible, 1=Infected, 2=Recovered')
    plt.axis('off')
    plt.show()
