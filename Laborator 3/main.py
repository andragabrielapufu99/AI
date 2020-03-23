from readNetwork import readNet,readNetGML
from resolvGA import resolvGA
from modularityFunction import modularity
def main():
    network=readNetGML("dolphins.gml")
    noDim = network['noNodes']
    # initialise de GA parameters
    gaParam = {'popSize': 10, 'noGen': 4000, 'pc': 0.8, 'pm': 0.1}
    # problem parameters
    problParam = {'net':network, 'min': 0, 'max': network['noNodes']-1, 'function': modularity, 'noDim': noDim}
    solution = resolvGA(gaParam,problParam)

    i=1
    for community in solution['communities'].values():
        s="\nComunitatea "+str(i)+"\n"
        for elem in community:
            s += str(elem+1)+" "
        print(s)
        i += 1
    print()
    print("Fitness : "+str(solution['fitness']))

main()