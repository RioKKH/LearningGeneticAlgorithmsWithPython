#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

#from fitness import fitness
#from settings import MIN_BORDER, MAX_BORDER

#from ch2.fitness import fitness
#from ch2.settings import MIN_BORDER, MAX_BORDER

from fitness import fitness
from settings import MIN_BORDER, MAX_BORDER


class Individual:

    def __init__(self, gene_list, fitness_function) -> None:
        self.gene_list = gene_list
        self.fitness = fitness_function(self.gene_list[0])

    def __str__(self) -> str:
        return f"{self.gene_list[0]:.2f} -> {self.fitness:.2f}"

    def get_gene(self):
        return self.gene_list[0]


def create_random_inidividual():
    return Individual([random.uniform(MIN_BORDER, MAX_BORDER)], fitness)


def create_individual(gene):
    return Individual([gene], fitness)

