import random

from selection_propotional import selection_propotional
from individual import Individual

POPULATION_SIZE = 5
random.seed(4)

population = Individual.create_random_population(POPULATION_SIZE)
selected = selection_propotional(population)

print(f"Population: {population}")
print(f"Selected: {selected}")
