#! /bin/python3

files = [ 'example' ]
#files = [ '1_victoria_lake', '2_himalayas', '3_budapest', '4_manhattan', '5_oceania' ]
map_chart = { '#': -1, '~': 800, '*': 200, '+': 150, 'X': 120, '_': 100, 'H': 70, 'T': 50 }

def cost(cell):
    return map[cell[0]][cell[1]]

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
