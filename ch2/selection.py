#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from ch2.individual import create_random_inidividual


def select_tournament(population, tournament_size):
    new_offspring = []
    for _ in range(len(population)):
        # populationの数だけtournament selectionを実行する
        candidates = [random.choice(population) for _ in range(tournament_size)]
        # tournament_sizeの数だけindを選択する
        new_offspring.append(max(candidates, key = lambda ind: ind.fitness))
        # 選ばれたindの中でfitnessが最大のものを選択する。
        # これだと同じindが複数回選択される可能性があるがそれを許容する。
        # 優秀なindが親として選ばれやすいということ
    return new_offspring


def run():
    random.seed(29)

    # PARAMETER: the size of initial population
    POPULATION_SIZE = 5

    # Generationg random population
    generation_1 = [create_random_inidividual() for _ in range(POPULATION_SIZE)]

    # Population after applying selection
    generation_2 = select_tournament(generation_1, 3)

    # Printing results
    print("Generation 1")
    [print(ind) for ind in generation_1]

    print("Generation 2")
    [print(ind) for ind in generation_2]
