#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from crossover import crossover
from individual import create_random_inidividual
from mutate import mutate
from population import plot_population
from selection import select_tournament


if __name__ == '__main__':
    # PARAMETERS
    POPULATION_SIZE = 10
    CROSSOVER_PROBABILITY = 0.8
    MUTATION_PROBABILITY = 0.1
    MAX_GENERATIONS = 10

    random.seed(29)

    # Initial random population
    population  = [create_random_inidividual() for _ in range(POPULATION_SIZE)]

    for generation_number in range(POPULATION_SIZE):

        # SELECTION OPERATION
        selected = select_tournament(population, 3)

        # CROSSOVER
        crossed_offspring = []
        for ind1, ind2 in zip(selected[::2], selected[1::2]):
            if random.random() < CROSSOVER_PROBABILITY:
                # Applying crossover to pair of individuals
                children = crossover(ind1, ind2)
                crossed_offspring.append(children[0])
                crossed_offspring.append(children[1])
            else:
                # Passing individuals further without crossover
                crossed_offspring.append(ind1)
                crossed_offspring.append(ind2)

        # MUTATION
        mutated = []
        for ind in crossed_offspring:
            if random.random() < MUTATION_PROBABILITY:
                # Applying mutation to an individual
                mutated.append(mutate(ind))
            else:
                # Passing individual further without mutation
                mutated.append(ind)

        # Next generation
        population = mutated

        plot_population(population)

