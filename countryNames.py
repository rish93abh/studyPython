print ("This is country names using Dictionary")


countries = {}

for x in range(5):
    
    inputCountry = input('Enter country name: ')

    firstLetter = inputCountry[0].upper()
    if firstLetter not in countries:
        countries[firstLetter] = [inputCountry]

    else:
        countries[firstLetter].append(inputCountry)

print(countries)        