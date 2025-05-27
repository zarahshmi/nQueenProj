import random

def fitness(individual):
    n = len(individual)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    max_conflicts = n * (n - 1) // 2
    return max_conflicts - conflicts

def generate_individual(n):
    # ساخت فردی که درصدی از ژن‌ها بدون تکرارند
    individual = []
    used = set()
    for _ in range(n):
        val = random.randint(0, n - 1)
        # سعی کن تکراری نباشه، ولی اگر شد، بپذیر
        if val not in used:
            used.add(val)
        individual.append(val)
    return individual

def crossover(parent1, parent2):
    n = len(parent1)
    point1 = random.randint(1, n // 2)
    point2 = random.randint(point1 + 1, n - 1)
    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    return child

def mutate(individual, mutation_rate=0.1):
    n = len(individual)
    for i in range(n):
        if random.random() < mutation_rate:
            # به جای مقدار تصادفی، جابجایی دو ژن را امتحان کن
            j = random.randint(0, n - 1)
            individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm(n, population_size=100, generations=1000, mutation_rate=0.1):
    population = [generate_individual(n) for _ in range(population_size)]

    for gen in range(generations):
        population.sort(key=lambda ind: -fitness(ind))
        best = population[0]

        if fitness(best) == (n * (n - 1)) // 2:
            print(f"✅ جواب پیدا شد در نسل {gen}")
            return best

        top_k = population[:max(2, population_size // 10)]
        new_population = top_k[:]  # حفظ بهترین‌ها

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(top_k, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    print("❌ جوابی پیدا نشد.")
    return None
