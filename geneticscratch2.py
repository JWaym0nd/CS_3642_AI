import random
import numpy as np
import sys

# this initializes a list called "chromosome."
def createchromosome1():
    chromosome = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        chromosome[i] = i
    random.shuffle(chromosome)
    print("This is a chromosome:")
    print(chromosome)
    return chromosome


# this determines the fitness (a.k.a utility) of a generation (aka chromosome).
def fitness(generation):
    chessboard = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    hits = 0
    solution = chessboard
    col = 0
    # need to apply generation to board; gene reps a row
    # for chromosome in range(8):
    # iterate across columns and place genes on designated row
    # ex: board[chromo][0] = row is chromo; [0] is column
    # board[ generation[i] ][ i]=1
    for gene in range(8):
        # print(generation[gene])
        #for dna in range(8):
        solution[gene][generation[gene]] = 1
    # print(np.matrix(solution))

    for gene in generation:
        # try:
        #   for i in range(col - 1, -1, -1):
        #      if solution[gene][i] == 1:
        #         hits += 1
        # except:
        #   print("error")

        # for every queen(gene) see if board contains a queen
        for x, y in zip(range(gene - 1, -1, -1), range(col - 1, -1, -1)):
            if solution[x][y] == 1:
                hits += 1
        for x, y in zip(range(gene + 1, 8, 1), range(col - 1, -1, -1)):
            if solution[x][y] == 1:
                hits += 1
        for x, y in zip(range(gene - 1, -1, -1), range(col + 1, 8, 1)):
            if solution[x][y] == 1:
                hits += 1
        for x, y in zip(range(gene + 1, 8, 1), range(col + 1, 8, 1)):
            if solution[x][y] == 1:
                hits += 1
        col += 1
    print(np.matrix(solution))
    return hits


# making two 'parents' and exchanging parts of them with each other
def crossbreed(gen1, gen2):
    newgen1 = []  # list(gen1)
    newgen2 = []  # list(gen2)

    for i in range(random.randint(1, 8)):
        newgen1.append(gen2[i])
        newgen2.append(gen1[i])

    x = 8 - len(newgen1)
    print("# of uncrossed elements upon breeding: " + str(x))
    for j in range(x):
        newgen1.append(gen1[j - x])
        newgen2.append(gen2[j - x])
    print("New gen 1 after crossbreeding: " + str(newgen1))
    print("New gen 2 after crossbreeding: " + str(newgen2))
    return [newgen1, newgen2]


def mutation(gen):
    r = random.randint
    s = np.size(gen)
    bound = s // 2
    leftSideIndex = r(0, bound)
    rightSideIndex = r(bound + 1, s)
    newGen = []
    for dna in gen:
        if dna not in newGen:
            newGen.append(dna)
    for i in range(s):
        if i not in newGen:
            newGen.append(i)
    gen = newGen
    try:
        gen[leftSideIndex], gen[rightSideIndex] = gen[rightSideIndex], gen[leftSideIndex]
    except:
        print("Out of range.")
    return gen


sys.setrecursionlimit(10 ** 8)


def gensolver(generations):
    genx = createchromosome1()
    geny = createchromosome1()
    while True:
        print("Fitness of genx: " + str(fitness(genx)))
        print("Fitness of geny: " + str(fitness(geny)))
        print()
        genz = crossbreed(genx, geny)
        print("beginning of if-else")
        if fitness(genz[0]) < fitness(genz[1]):
            genx = mutation(genz[1])
            geny = genz[0]
            z_fit = fitness(genx)
        else:
            genx = mutation(genz[0])
            geny = genz[1]
            z_fit = fitness(genx)
        print("(after if-else)")

        print("Fitness of z: " + str(z_fit))
        #generations = 0
        if z_fit <= 5:
            print(z_fit)
            break
        else:
            generations += 1
            print("Gens: " + str(generations))
            #gensolver(generations)
        #print("Gens: " + str(generations))
    return z_fit


gensolver(0)