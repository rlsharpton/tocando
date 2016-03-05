__author__ = 'tocando'

f = open('countries.txt', 'r')

print ('f is a ', type(f))

countries = []

for line in f:
    line = line.strip()
    countries.append(line)

f.close()

#print(countries)
print(len(countries))

for country in countries:
    if country[0] == 'T':
        print(country)
