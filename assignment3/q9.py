num_list=eval(input())
def MinMaxAvg(num_list):
    total = 0
    maxNum = -1000
    minNum = 1000
    for n in num_list:
        if n > maxNum:
            maxNum = n
        if n < minNum:
            minNum = n
        total += n
    print(f'Min: {minNum}')
    print(f'Max: {maxNum}')
    print(f'Avg: {total/len(num_list)}')
    
MinMaxAvg(num_list)