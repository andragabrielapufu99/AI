from Chromosome import Chromosome
from GA import GA
from modularityFunction import modularity


def cooldown(temperature):
    return (90*temperature)/100


def resolvGA(gaParam,problParam):
    ga = GA(gaParam, problParam)
    sol = Chromosome(problParam)
    sol.setFitness(float('-inf'))
    #creez o populatie
    ga.initialisation()
    ga.evaluation()

    print("POPULATIA INITIALA")
    for chromo in ga.population():
        print("Reprezentare : "+str(chromo.getReprezentare())+" Fitness : "+str(chromo.getFitness()))

    temperature = 10000
    gen = 1
    while temperature>1000 and gen<=gaParam['noGen']:
        sorted(ga.population(),key=lambda x:x.getFitness(),reverse=True)
        print("\nTemperatura curenta : " + str(temperature))
        new_population = []
        while len(new_population)!=gaParam['popSize']:
            #aleg 2 parinti
            mother = ga.population()[ga.selection()]
            father = ga.population()[ga.selection()]

            #ii incrusisez
            child = mother.crossover(father)


            while True:
                # caut cel mai bun copil
                child.mutation()
                new_cromo = Chromosome(problParam)
                new_cromo.setReprezentare(child.getReprezentare())
                new_cromo.setFitness(modularity(new_cromo.getReprezentare(),problParam['net']))

                if new_cromo.getFitness() > mother.getFitness() and new_cromo.getFitness() > father.getFitness():
                    # il adaug pe cel mai bun in noua populatie
                    new_population.append(new_cromo)
                    break
                else:
                    """inca nu am gasit cel mai bun copil, dar ofer sansa celorlalti 
                    gasiti pana acum de a intra in noua populatie daca probabilitatea > 0.5 
                    (pot obtine un material genetic bun din ei)"""
                    if mother.getFitness() > father.getFitness():
                        parent = mother
                    else:
                        parent = father
                    prob = pow(2.7, -1 * ((parent.getFitness()-new_cromo.getFitness()) / temperature))
                    if prob > 0.5:
                        new_population.append(new_cromo)
                        break
                    new_population.append(new_cromo)
                    break
        # scad temperatura
        temperature = cooldown(temperature)
        population = new_population

        print("Generatia " + str(gen))
        for i in range(gaParam['popSize']):
            print("Cromozom : " + str(population[i].getReprezentare()) + " Fitnes : " + str(population[i].getFitness()))

        #cel mai bun din aceasta generatie
        bestChromo = ga.bestChromosome()
        if(bestChromo.getFitness() > sol.getFitness()):
            sol.setReprezentare(bestChromo.getReprezentare())
            sol.setFitness(bestChromo.getFitness())

        gen += 1  # trecem la urmatoarea generatie

    """for t in range(gaParam['noGenIterations']):
        for g in range(gaParam['noGen']):
            # logic alg
            ga.oneGeneration()
            #ga.oneGenerationElitism()
            #ga.oneGenerationSteadyState()
            bestChromo = ga.bestChromosome()
            if (bestChromo.fitness > vmax):
                vmax = bestChromo.fitness
                rez = bestChromo.repres
        sol = {}
        for i in range(len(rez)):
            if rez[i] not in sol:
                sol[rez[i]] = [i]
            else:
                sol[rez[i]].append(i)
                """
    chromoRezultat = {}
    rezultat = {}
    for i in range(len(sol.getReprezentare())):
        if sol.getReprezentare()[i] not in rezultat:
            rezultat[sol.getReprezentare()[i]] = [i]
        else:
            rezultat[sol.getReprezentare()[i]].append(i)
    chromoRezultat['communities'] = rezultat
    chromoRezultat['fitness'] = sol.getFitness()
    return chromoRezultat