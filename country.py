from operator import attrgetter
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = population

    def __repr__(self): #this makes the information available from outside
        return repr((self.name, self.population, self.area)) #This is a tuple



countries = [Country('India',1200,100),
             Country('China',1400,200),
             Country('USA',120,300)]

countries.append(Country('Russia',80,900))

countries.sort(key=attrgetter('population'), reverse=True)
print(max(countries, key=attrgetter('population')))
print(countries)
print(countries[0])
print(countries[0:2])

