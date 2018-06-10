def columnChecker(s):
    magic_num = 15

    for j in range(len(s)):
        total = 0
        for k in range(len(s)):
            total += s[k][j]
        print(total)
        if total != magic_num:
            return False

    return True

def rowChecker(s):
    magic_num = 15

    for i in range(len(s)):
        total = 0
        for j in range(len(s)):
            total += s[i][j]
        print(total)
        if total != magic_num:
            return False
    return True

def diagChecker(s):
    magic_num = 15
    first_total = 0
    second_total = 0
    for i in range(len(s)):
        first_total += s[i][i]
    print('The first diagonal is', first_total)
    if first_total != magic_num:
        return False

    for i in range(len(s)):
        second_total += s[len(s)-1-i][i]
    print('The second diagonal is', second_total)
    if second_total != magic_num:
        return False

    return True





def main():
    s = []

    for _ in range(3):
        s.append(list(map(int, input('Enter the numbers: ').rstrip().split())))

    #Checks Columns
    print('This checks the columns')
    column = columnChecker(s)
    if column:
        print('columns are magic')
    else:
        print('Houston we have a problem')

    #Checks Rows
    print('This checks the rows')
    row = rowChecker(s)
    if row:
        print('rows are magic')
    else:
        print('Houston we have a problem')

    # Checks Diagonals
    print('This checks the diagonals')
    diag = diagChecker(s)
    if diag:
        print('Diagonals are magic')
    else:
        print('Houston we have a problem')

    #Whole Square
    if column and row and diag:
        print('You have a magic square!')
    else:
        print('Better luck next time :(')

main()