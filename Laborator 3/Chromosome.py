import random
from random import randint

class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = [randint(problParam['min'], problParam['max']) for _ in range(problParam['noDim'])]
        self.__fitness = 0.0

    def getReprezentare(self):
        return self.__repres

    def getFitness(self):
        return self.__fitness


    def crossover(self, c):
        r = randint(0, len(self.__repres) - 1)
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        offspring = Chromosome(c.__problParam)
        offspring.setReprezentare(newrepres)
        return offspring

    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        maxValue = max(self.__repres)
        #self.__repres[pos] = randint(self.__problParam['min'], self.__problParam['max'])
        randValue = random.choice(self.__repres)
        self.__repres[pos] = randValue

    def setFitness(self,newFitness):
        self.__fitness = newFitness

    def setReprezentare(self,newRepres):
        self.__repres = newRepres

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness