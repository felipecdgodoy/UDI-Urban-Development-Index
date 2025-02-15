from math import log, exp

def index_pib(realPIBpercapita):
    "Returns the index value for PIB per capita. Takes in the value in dollars. I.e. 3451"
    return 100.0 * ((log(realPIBpercapita) - log(604)) / (log(145894) - log(604)))

def index_unemployement(unemployement_rate):
    "Returns the index value for Unemployement Rate. Takes in a percentage such as 0.0659"
    return round((-99/22) * (100 * unemployement_rate)) + 113.5

def index_literatepopulation(literate_rate):
    "Return the index value for Literacy. Takes in a percentage such as 0.947"
    return round(((99/50) * (100 * literate_rate)) - 98, 2)

def index_accessToCleanWater(water_access_rate):
    "Returns the index value for Access to Clean Water. Takes in a percentage such as 0.982"
    return ((99/90) * (100 * water_access_rate)) - 10

def index_accessToHealth(number_doc_1000_people):
    "Returns the index value for Access to Health, measured by the number of health professionals "
    "per 1000 residents in the city. Takes in the raw number of doctors / 1000 people such as 10.3"
    return 100 / (1 + (99 * exp(-0.91902397 * number_doc_1000_people)))

def index_lifeExpectancy(lifeExpectancy):
    "Returns the index value for Life Expectancy. Takes in the expected age such as 77.6"
    return 100 / (1 + (36129.25286 * exp(-0.155256271 * lifeExpectancy)))

def UDI(realPIBpercapita, unemployement_rate, literate_rate, water_access_rate,
        number_doc_1000_people, lifeExpectancy):
    "Calculates the final UDI value for a city"
    return round((
                    index_pib(realPIBpercapita)
                  * index_unemployement(unemployement_rate)
                  * index_literatepopulation(literate_rate)
                  * index_accessToCleanWater(water_access_rate)
                  * index_accessToHealth(number_doc_1000_people)
                  * index_lifeExpectancy(lifeExpectancy))
                    ** (1/6), 2)

def describeCity(cityName, realPIBpercapita, unemployement_rate, literate_rate, water_access_rate,
        number_doc_1000_people, lifeExpectancy):
    "Prints the description of a specific city's UDI results"
    print("Analyzing city: " + cityName)
    print("Index value for PIB: " + index_pib(realPIBpercapita))
    print("Index value for Unemployement: " + index_unemployement(unemployement_rate))
    print("Index value for Literacy: " + index_literatepopulation(literate_rate))
    print("Index value for Water Access: " + index_accessToCleanWater(water_access_rate))
    print("Index value for Health: " + index_accessToHealth(number_doc_1000_people))
    print("Index value for Life Expectancy: " + index_lifeExpectancy(lifeExpectancy))
    print("UDI: " + UDI(realPIBpercapita, unemployement_rate, literate_rate, water_access_rate,
            number_doc_1000_people, lifeExpectancy))
