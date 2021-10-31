#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

#from ch2.individual import create_random_inidividual
#from ch2.fitness import fitness
#from ch2.settings import MIN_BORDER, MAX_BORDER

from individual import create_random_inidividual
from fitness import fitness
from settings import MIN_BORDER, MAX_BORDER

def get_best_individual(population):
    return max(population, key = lambda ind: ind.fitness)

def get_average_fitness(population):
    return sum([i.fitness for i in population]) / len(population)

def plot_population(population):
    # best individual from the population
    best_ind = get_best_individual(population)

    # fitness of the best individual
    best_fitness = best_ind.fitness

    # average fitness of the population
    average_fitness = get_average_fitness(population)

    # plotting fitness curve
    x = np.linspace(MIN_BORDER, MAX_BORDER)
    plt.plot(x, fitness(x), '--', color = 'blue')

    # plotting whole population
    plt.plot(
        [ind.get_gene() for ind in population],
        [ind.fitness for ind in population],
        'o', color = 'orange'
    )

    # plotting best individual
    plt.plot(
        [best_ind.get_gene()], [best_ind.fitness],
        's', color = 'green'
    )

    # population average fitness
    plt.plot(
        [MIN_BORDER, MAX_BORDER],
        [average_fitness, average_fitness],
        color = 'gray'
    )

    plt.title(f"Best Individual: {best_ind}, Best Fitness: {best_fitness:.2f} \n"
              f"Average Population Fitness: {average_fitness:.2f}"
              )
    plt.show()


def run():
    # PARMETER: The size of initial population
    POPULATION_SIZE = 10
    random.seed(22)


    # Generating random population
    population = [create_random_inidividual() for _ in range(POPULATION_SIZE)]

    # plotting the distribution of the population on fitness curve
    plot_population(population)


if __name__ == "__main__":
    # PARMETER: The size of initial population
    POPULATION_SIZE = 10
    random.seed(22)


    # Generating random population
    population = [create_random_inidividual() for _ in range(POPULATION_SIZE)]

    # plotting the distribution of the population on fitness curve
    plot_population(population)

