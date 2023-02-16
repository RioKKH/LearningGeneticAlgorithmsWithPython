#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt


from individual import create_random_inidividual, create_individual
from fitness import fitness
from settings import MIN_BORDER, MAX_BORDER


def gene_constraints(g, min_ = MIN_BORDER, max_ = MAX_BORDER):
    """
    Limits gene value inside interval [min_, min_]
    """
    if max_ and g > max_:
        g = max_
    if min_ and g < min_:
        g = min_
    return g

def mutate_gaussian(g, mu, sigma):
    """
    Gaussian Mutation. Explained in Chapter 5. Mutation
    """
    mutated_gene = g + random.gauss(mu, sigma)
    return gene_constraints(mutated_gene)

def mutate(ind):
    """
    Mutation of Individual
    """
    return create_individual(mutate_gaussian(ind.get_gene(), 0, 1))


if __name__ == '__main__':
    random.seed(37)

    # Random Individual
    individual = create_random_inidividual()

    # Mutated Individual
    mutated = mutate(individual)

    # Visualization
    x = np.linspace(MIN_BORDER, MAX_BORDER)
    plt.plot(x, fitness(x), '--', color='blue')
    plt.plot(
        [individual.get_gene()],
        [individual.fitness],
        'o', markersize=20, color='orange'
    )
    plt.plot(
        [mutated.get_gene()],
        [mutated.fitness],
        's', markersize=20, color='green'
    )
    plt.title("Circle : Before Mutation, Square: After Mutation")
    plt.show()


