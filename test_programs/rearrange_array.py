def rearrangeArray(arr):
    temp = [0] * len(arr)
    for i in range(len(arr)):
        if i in arr:
            temp[i] = i
        else:
            temp[i] = -1
    return temp


def main():
    first_arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

    second_arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
                  11, 10, 9, 5, 13, 16, 2, 14, 17, 4]

    print(rearrangeArray(first_arr))
    print(rearrangeArray(second_arr))


main()