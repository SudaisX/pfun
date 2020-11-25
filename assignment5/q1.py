import math
import os
import random
import re
import sys

def priceCheck(products, productPrices, productSold, soldPrice):
    error = 0
    products = {products[i]:productPrices[i] for i in range(len(products))}
    sold = {productSold[i]:soldPrice[i] for i in range(len(productSold))}

    for prod, cost in sold.items():
        if products[prod] != cost:
            error += 1
    return error

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    products_count = int(input().strip())

    products = []

    for _ in range(products_count):
        products_item = input()
        products.append(products_item)

    productPrices_count = int(input().strip())

    productPrices = []

    for _ in range(productPrices_count):
        productPrices_item = float(input().strip())
        productPrices.append(productPrices_item)

    productSold_count = int(input().strip())

    productSold = []

    for _ in range(productSold_count):
        productSold_item = input()
        productSold.append(productSold_item)

    soldPrice_count = int(input().strip())

    soldPrice = []

    for _ in range(soldPrice_count):
        soldPrice_item = float(input().strip())
        soldPrice.append(soldPrice_item)

    result = priceCheck(products, productPrices, productSold, soldPrice)

    fptr.write(str(result) + '\n')

    fptr.close()
