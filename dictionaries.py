ages = {'Hallie': 17, 'Paris': 18, 'Caroline': 19}

ages['Caroline'] = 20

ages['Carly'] = 16

ages['Carrington'] = 15

ages['Mena'] = 15

for name in ages:
    currentAge = ages[name]
    ages[name] = currentAge + 1
    print(ages[name])
