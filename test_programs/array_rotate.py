def arrayRotation(arr, n, d):
    holding = []
    for i in range(d):
        holding.append(arr[i])
    print('This is the holding array', holding)
    print('This is the regular array', arr)

    return arr[d:] + holding

def main():
    array = [1, 2, 3, 4, 5, 6, 7]

    print(arrayRotation(array, 7, 2))

main()
