#! /bin/python3

files = [ "a_example", "b_small", "c_medium", "d_quite_big", "e_also_big" ]

def solve(max_s, piz, pizza_list):
    pizzas = []
    slices = 0
    for i in reversed(range(0, piz)):
        if slices + pizza_list[i] < max_s:
            slices += pizza_list[i]
            pizzas.append(i)
    print("Number of points: " + str(slices))
    print("Max Number of Slices: " + str(max_s), end = "\n\n")
    return list(reversed(pizzas))

if __name__ == '__main__':
    for filename in files:
        file = open(filename + ".in",'r')
        str_1 = file.readline()
        max_s, piz = [int(x) for x in str_1.split()]
        str_2 = file.readline()
        piz_vec = [int(x) for x in str_2.split()]
        print(filename)
        pizza_list = solve(max_s, piz, piz_vec)
        file.close()

        fh = open(filename + ".out", 'w')
        fh.write(str(len(pizza_list)) + "\n")
        for x in pizza_list:
            fh.write(str(x) + " ")
        fh.close()
