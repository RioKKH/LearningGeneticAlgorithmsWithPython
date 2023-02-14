#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Individual:

    def __init__(self, name) -> None:
        self.name = name
        self.fitness = random.randint(0, 10)

    def __str__(self):
        # __str__()はprint()に渡された場合に呼ばれる
        return f'{self.name}: {self.fitness}'

    def __repr__(self):
        return str(self)

    @classmethod
    def create_random_population(cls, num):
        population = []
        for i in range(97, 97 + num):
            population.append(Individual(chr(i).upper()))
        return population
