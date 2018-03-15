#   Author: Sasan Najar
#   Email: sasangnajar@gmail.com

#   This code is designed to:
##  STEP #1: Take a list as its argument
##  STEP #2: Return a new list containing the unique elements of the original list
##  STEP #3: The elements in the new list without duplicates can be in any order

def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target