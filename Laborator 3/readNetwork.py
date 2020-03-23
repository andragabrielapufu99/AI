# read the network details
def readNet(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat 
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net

def readNetGML(fileName):
    f = open(fileName,"r")
    net = {}
    net['noNodes'] = 0
    net['noEdges'] = 0
    ok = 0
    while True:
        line = f.readline().strip()
        if line == "":
            break
        elif line == "node":
            net['noNodes'] += 1
        elif line == "edge":
            ok = 1
            break
    if ok == 1:
        net['mat'] = [[0 for _ in range(net['noNodes'])] for _ in  range(net['noNodes'])]
        degrees = [0 for _ in range(net['noNodes'])]
        f.readline()
        sourceElem = f.readline().strip().split(" ")
        source = int(sourceElem[1])
        targetElem = f.readline().strip().split(" ")
        target = int(targetElem[1])
        net['mat'][source][target] =1
        net['mat'][target][source] = 1
        degrees[source] += 1
        degrees[target] += 1
        net['noEdges'] += 1
        f.readline()
        while True:
            line = f.readline().strip()
            if line == "]":
                break
            f.readline()
            sourceElem = f.readline().strip().split(" ")
            source = int(sourceElem[1])
            targetElem = f.readline().strip().split(" ")
            target = int(targetElem[1])
            net['mat'][source][target] = 1
            net['mat'][target][source] = 1
            degrees[source] += 1
            degrees[target] += 1
            net['noEdges'] += 1
            f.readline()
    net['degrees'] = degrees
    f.close()
    return net