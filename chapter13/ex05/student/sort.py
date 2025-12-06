# Write your code here
def selectionSort(lyst, reverse=False):
    """Sorts lyst in ascending order unless reverse=True."""
    n = len(lyst)
    for i in range(n - 1):
        target_index = i
        for j in range(i + 1, n):
            if reverse:
                # Choose the largest remaining item
                if lyst[j] > lyst[target_index]:
                    target_index = j
            else:
                # Choose the smallest remaining item
                if lyst[j] < lyst[target_index]:
                    target_index = j

        # Swap chosen item into position i
        swap(lyst, i, target_index)


def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""
    lyst[x], lyst[y] = lyst[y], lyst[x]


def main():
    """Tests with four lists."""
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst)
    print(lyst)

    lyst = list(range(6))
    selectionSort(lyst)
    print(lyst)

    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst, reverse=True)
    print(lyst)

    lyst = list(range(6))
    selectionSort(lyst, reverse=True)
    print(lyst)


if __name__ == "__main__":
    main()
