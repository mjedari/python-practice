def find_smallest_index(array):
    smallest_index = 0
    smallest = array[0]
    for i in range(len(array)):
        if array[i] < smallest:
            smallest_index = i
            smallest = array[i]

    return smallest_index


def selection_sort(array):
    sorted = []
    for i in range(len(array)):
        smallest_index = find_smallest_index(array)
        sorted.append(array.pop(smallest_index))
    return sorted


def main():
    array = [1, 2, 20, 3, 43, 5, 65678, 9989, 856]
    print("here is array", array)
    print("here is sorted array", selection_sort(array))


if __name__ == '__main__':
    main()
