import random

def random_chromosome(size):
    # Generate a random permutation of queens in each column (one per row)
    return random.sample(range(size), size)

def fitness(chromosome):
    n = len(chromosome)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Check for diagonal attacks
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                attacks += 1
    return -attacks  # Lower is better

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    child = parent1[:point]
    for gene in parent2:
        if gene not in child:
            child.append(gene)
    return child

def mutate(chromosome):
    # Swap two genes (rows of two queens)
    i, j = random.sample(range(len(chromosome)), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm(n, population_size=300, generations=1000):
    population = [random_chromosome(n) for _ in range(population_size)]

    for gen in range(generations):
        population.sort(key=fitness, reverse=True)

        # Print the best chromosome of this generation
        best = population[0]
        print(f"Generation {gen} → Best: {best}, Fitness: {fitness(best)}")

        if fitness(best) == 0:
            print(f"✅ Solved in generation {gen}")
            return best

        new_population = population[:10]  # Elitism

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:50], k=2)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:
                mutate(child)
            new_population.append(child)

        population = new_population

    print("❌ No perfect solution found.")
    return population[0]  # Best possible solution found
