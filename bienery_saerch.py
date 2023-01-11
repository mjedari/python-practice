def bsearch(array, param):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == param:
            return mid
        if param < guess:
            high = mid - 1
        else:
            low = mid + 1

    return None


def main():
    sorted_array = [1, 2, 6, 8, 23, 56, 87, 610, 789]
    index = bsearch(sorted_array, 610)
    print("the index of element is:", index)


if __name__ == "__main__":
    main()
