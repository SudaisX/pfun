def print_matrix(rows, columns):
    lst = [[0 for i in range(columns)] for j in range(rows)]
    spaces = '     '
    
    for row in range(len(lst)):
        if row == 0:
            continue
        for column in range(len(lst[row])):
            if column == 0:
                continue
            lst[row][column] = row * column
            
    for row in lst:
        for n in row:
            print(f'{n}{spaces}', end='')
            
        if row == lst[-1]:
            pass
        else:
            print('\n')

rows = int(input())
columns = int(input())
print_matrix(rows, columns)