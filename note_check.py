amount = int(input())
notes = [0 for i in range(10)]
remainder = [amount]

def note_check(x, note):
    if remainder[0] >= note:
        notes[x] = int(remainder[0]/note)
        remainder[0] = (remainder[0] % note)
    print(f'{note} : {notes[x]}')

def countCurrency(amount):
    
    print("Total number of notes:")
    note_check(0, 5000)
    note_check(1, 1000)
    note_check(2, 500)
    note_check(3, 100)
    note_check(4, 50)
    note_check(5, 20)
    note_check(6, 10)
    note_check(7, 5)
    note_check(8, 2)
    note_check(9, 1)

countCurrency(amount)