# How to make all 3 size combinations of a set

if __name__ == '__main__':
    x = 1
    y = 1
    z = 1
    n = 2

    my_set = []
    for a in range(0, x + 1):
        for b in range(0, y + 1):
            for c in range(0, z + 1):
                if a + b + c != n:
                    my_set.append([a, b, c])
    print(my_set)
