month_names = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December' }

def popular_month(t):
    months = [0 for i in range(12)]
    for each in t:
        months[each['month']-1] += 1
        
    famousMonths = sorted([month_names[i+1] for i, val in enumerate(months) if val == max(months)])
    s = ''
    for month in famousMonths:
        s += f'{month}, '
    return s[:len(s)-2]
    
t = eval(input().strip())
print(popular_month(t))