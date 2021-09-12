#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

from ch2.individual import create_random_inidividual, create_individual
from ch2.fitness import fitness
from ch2.settings import MIN_BORDER, MAX_BORDER


def gene_constraints(g, min_ = MIN_BORDER, max_ = MAX_BORDER):
    """
    Limits gene value inside interval [min_, max_]
    """
    if max_ and g > max_:
        g = max_
    if min_ and g < min_:
        g = min_
    return g


def crossover_blend(g1, g2, alpha = 0.3):
    """
    Gene blending. Explained in Chapter 4. Crossover
    """
    shift = (1. + 2. * alpha) * random.random() - alpha
    new_g1 = (1. - shift) * g1 + shift * g2
    new_g2 = shift * g1 + (1. - shift) * g2
    return gene_constraints(new_g1), gene_constraints(new_g2)
