import math
import os
import random
import re
import sys

def groupTransactions1(transactions):
    items_list = []
    items = {transactions[i]:0 for i in range(len(transactions))}

    for each in transactions:
        if each in items:
            items[each] += 1

    for key, val in items.items():
        items_list.append(f'{key} {val}')
        
    return(sorted(items_list))

def groupTransactions(transactions):  
    items = {transactions[i]:0 for i in range(len(transactions))}
    for each in transactions:
        if each in items:
            items[each] += 1 
    return(sorted([f'{key} {val}' for key, val in items.items()]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    transactions_count = int(input().strip())

    transactions = []

    for _ in range(transactions_count):
        transactions_item = input()
        transactions.append(transactions_item)

    result = groupTransactions(transactions)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
