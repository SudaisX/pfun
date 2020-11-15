
singlesymbol = False
symbol = input('Enter a symbol for the hollow triangle. \n')
while not(singlesymbol):
    if len(symbol) != 1:
        symbol = input('Invalid input, Enter a symbol for the hollow triangle. \n')
    if len(symbol) == 1:
        singlesymbol = True

integer = False
num = int(input("Enter an odd number between 0 and 99 \n"))
while not(integer):
    if num % 2 == 0:
        num = int(input("Invalid input, Enter an odd number between 0 and 99 \n"))
    else:
        integer = True

maxspace = int(num/2)

for i in range(maxspace):
    if i == 0:
        spaces = " " * maxspace
        print(spaces + symbol)
    elif i != 0 and i != maxspace:
        symbols = symbol + (" " * (2*(i-1) + 1)) + symbol
        spaces = " " * (maxspace - i)
        print(f"{spaces}{symbols}")

print(symbol * num)

