#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def fitness(x):
    return np.sin(x) - .2 * abs(x)


if __name__ == "__main__":
    #from individual import Individual
    from ch2.individual import Individual
    ind = Individual([1], fitness)
    print(f"Individual fitness: {ind.fitness}")
