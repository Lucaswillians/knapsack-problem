import random

# Parameters
POPULATION_SIZE = 10
GENOME_SIZE = 8
GENERATIONS = 20
MUTATION_RATE = 0.1
KNAPSACK_CAPACITY = 15
TIME_LIMIT = 15 

# Items (weight, value, loading time)
items = [(2, 3, 2), (3, 4, 3), (4, 5, 4), (5, 8, 5), (8, 10, 8), (4, 7, 4), (2, 6, 2), (1, 2, 1)]

# Fitness Function
def fitness(individual):
    total_weight = 0
    total_value = 0
    total_time = 0
    
    for i in range(GENOME_SIZE):
        if individual[i] == 1: 
            total_weight += items[i][0]
            total_value += items[i][1]
            total_time += items[i][2]
    
    # Check if total weight exceeds the knapsack capacity
    if total_weight > KNAPSACK_CAPACITY:
        return 0 
    
    # Check if total loading time exceeds the limit
    if total_time > TIME_LIMIT:
        total_value -= (total_time - TIME_LIMIT) * 2  
    
    return total_value if total_value > 0 else 0  

# Create an individual (genome)
def create_individual():
    return [random.randint(0, 1) for _ in range(GENOME_SIZE)]

# Create a population
def create_population():
    return [create_individual() for _ in range(POPULATION_SIZE)]

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENOME_SIZE-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutation
def mutate(individual):
    for i in range(GENOME_SIZE):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# Selection
def selection(population):
    sorted_population = sorted(population, key=lambda ind: fitness(ind), reverse=True)
    return sorted_population[:POPULATION_SIZE//2]

# Evolution
def evolve(population):
    new_population = []
    selected_parents = selection(population)
    while len(new_population) < POPULATION_SIZE:
        parent1 = random.choice(selected_parents)
        parent2 = random.choice(selected_parents)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    return new_population

# GA Execution
population = create_population()
for generation in range(GENERATIONS):
    population = evolve(population)
    best_individual = max(population, key=lambda ind: fitness(ind))
    print(f"Generation {generation+1}: Best Fitness = {fitness(best_individual)}")

# Best solution
print("Best solution: ", best_individual)

# Display the final solution (selected items)
total_weight = 0
total_value = 0
total_time = 0
selected_items = []
for i in range(GENOME_SIZE):
    if best_individual[i] == 1:
        selected_items.append(items[i])
        total_weight += items[i][0]
        total_value += items[i][1]
        total_time += items[i][2]

print("Selected items:", selected_items)
print(f"Total weight: {total_weight}, Total value: {total_value}, Total time: {total_time}")
