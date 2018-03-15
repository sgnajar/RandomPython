#   Author: Sasan Najar
#   Email: sasangnajar@gmail.com

# This code is designed to take a country list as an input and give a dictionary as an output
# The output of this code is going to be a dictionary whose keys are country names and whose values are
# the number of times the country occurs in the countries list.

from countries import countryList # Since the list is so large, a separate file of countries created.

countryCounts = {}
for country in countryList:
    # todo: insert countries into the countryCount dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count

    if country in countryCounts:
        countryCounts[country] += 1
    else:
        countryCounts[country] = 1
