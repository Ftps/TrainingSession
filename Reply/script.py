#! /bin/python3

from numpy import zeros
from math import exp

#files = [ 'example' ]
files = [ '1_victoria_lake', '2_himalayas', '3_budapest', '4_manhattan', '5_oceania' ]
map_chart = { '#': -1, '~': 800, '*': 200, '+': 150, 'X': 120, '_': 100, 'H': 70, 'T': 50 }

def cost(cell):
    return map[cell[0]][cell[1]]

'''
Sigmoid based distance function so that points really close to a headquarter
don't have too much of a lower cost
'''
def distance(hq, i, j, size):
    return 1/(1 + exp(2.5*((abs(hq[0]-j) + abs(hq[1]-i)) - size)/size))

'''
Density function that takes into account the position of the headquarters,
the size of the map and the type of terrain around the point
'''
def density_map(map, head, N, M):
    map_den = zeros((M, N))
    size = 0.5*(N+M)/len(head)
    for i in range(0, M):
        for j in range(0, N):
            for hq in head:
                if map[i][j] == -1:
                    continue
                aux = 1/distance(hq, i, j, size)
                if j > hq[0]:
                    map_den[i][j] += aux*map[i][j-1]
                elif j < hq[0]:
                    map_den[i][j] += aux*map[i][j+1]
                if i > hq[1]:
                    map_den[i][j] += aux*map[i-1][j]
                elif i < hq[0]:
                    map_den[i][j] += aux*map[i+1][j]
    return map_den


if __name__ == '__main__':
    for filename in files:
        with open(filename + '.txt', 'r') as fp:
            N, M, C, R = [int(x) for x in next(fp).split()]
            #print(str(N) + " " + str(M) + " " + str(C) + " " + str(R))
            head = []
            for i in range(0, C):
                head.append([int(x) for x in next(fp).split()])
            map = []
            for line in fp:
                l = []
                for c in line:
                    if c != '\n':
                        l.append(map_chart[c])
                map.append(l)
            print(filename, end=": density map . . .\n")
            map_den = density_map(map, head, N, M)
            print("Done\n\n")
