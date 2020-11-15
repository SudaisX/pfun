def convert_kg_to(masses, unit):
    if unit == 'lbs':
        for i in range(len(masses)):
            masses[i] = round(masses[i] * 2.2046, 4)
        return masses
    elif unit == 'g':
        for i in range(len(masses)):
            masses[i] = masses[i] * 1000
        return masses
    else:
        return masses
    
naturals = eval(input())