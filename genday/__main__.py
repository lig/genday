from argparse import ArgumentParser

from .base import Population
from .runner import run_evolution


parser = ArgumentParser()
parser.add_argument('-n', '--population-size', type=int, default=20)
parser.add_argument('-m', '--mutation-probability', type=float, default=.1)

args = parser.parse_args()

population = Population(args.population_size, args.mutation_probability)

run_evolution(population)
