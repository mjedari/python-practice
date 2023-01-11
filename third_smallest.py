def main():
    array = [1, 2, 22, 3, 4, 65, 212, 43, 546, 675, 76, 5]
    array.sort()
    print(array)
    print("solution one: ", array.pop(2))
    print("solution two:", new_solution(array))

# O(3/2 * n)
def new_solution(array):
    if len(array) < 2:
        return None

    smallest = array[0]
    third_smallest = []
    while len(third_smallest) <= 3:
        # iterate for 3 times
        for i in range(len(array)):
            if array[i] < smallest:
                third_smallest.append(smallest)
                array.pop(i)

    print("here", third_smallest.pop())
    return 0


if __name__ == "__main__":
    main()
