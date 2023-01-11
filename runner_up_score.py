if __name__ == '__main__':
    n = int(input())

    arr = map(int, input().split())
    sorted_array = list(arr)

    sorted_array.sort()
    my_set = set(sorted_array)
    print(my_set)
    new_array = list(my_set)
    print("sorted ", new_array[len(new_array) - 2])
