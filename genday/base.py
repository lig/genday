from collections import deque
from enum import Enum
from random import choice, random


class Delta(Enum):
    sleep = +0
    eat = +1
    work = -1
    fun = -1


class MinCount(Enum):
    sleep = 4
    eat = 3
    work = 4
    fun = 0


class MaxCount(Enum):
    sleep = 8
    eat = 4
    work = 8
    fun = 24


class Display(Enum):
    sleep = '_'
    eat = '+'
    work = '/'
    fun = '*'


class Subject:
    actions = ['sleep', 'eat', 'work', 'fun']
    hours = 24
    energy = 100
    fun = 0

    def __init__(self, m_factor):
        self.m_factor = m_factor
        self.dna = []
        for _ in range(Subject.hours):
            self.dna.append(self.new_action())
        self.resurect()

    def __str__(self):
        return ''.join(map(lambda a: Display[a].value, self.dna))

    def live(self):
        return self.energy > 0 and all(map(
            lambda action:
                MinCount[action].value
                <= self.dna.count(action)
                <= MaxCount[action].value,
            self.actions))

    def cycle(self):
        self.fun += self.dna.count('fun')
        self.energy += sum(map(lambda gene: Delta[gene].value, self.dna))

    def mutate(self):
        self.resurect()
        success = False
        while not success:
            for i in range(Subject.hours):
                if random() < self.m_factor / Subject.hours:
                    self.dna[i] = self.new_action()
            success = self.live()

    def resurect(self):
        self.energy = Subject.energy
        self.fun = Subject.fun

    def new_action(self):
        return choice(self.actions)


class Population:

    def __init__(self, size, m_factor):
        self.subjects = deque(Subject(m_factor) for _ in range(size))
        self.generation = 0
        self.best = 0
        self.best_generation = 0

    def __str__(self):
        return 'Generation: {}\nBest: {}\nBest generation: {}\n{}\n'.format(
            self.generation,
            self.best,
            self.best_generation,
            '\n'.join(map(str, self.subjects)))

    def cycle(self):
        self.generation += 1

        for subject in self.subjects:

            if subject.live():
                subject.cycle()
            elif subject.fun > self.best:
                self.best = subject.fun
                self.best_generation = self.generation
            elif subject.fun <= self.best:
                subject.mutate()
            else:
                subject.resurect()
