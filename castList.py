#   Author: Sasan Najar
#   Email: sasangnajar@gmail.com

#   This code is designed to:
##  STEP 1: Take a filename as input (in this case: flyingCircusCast) xxx this information was collected from imdb.com
##  STEP 2: Returns a list of actors' names

def getCastList(filename):
    castList = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to castList
    with open(filename) as f:
    # use the for loop syntax to process each line and add the actor name to castList
        for line in f:
            lineData = line.split(',')
            castList.append(lineData[0])
    return castList

