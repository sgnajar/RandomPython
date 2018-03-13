#   Author: Sasan Najar ##
#   Email: sasangnajar@gmail.com ##

#   This script include function that.. 
#    #1 Takes as input five scores and aggregates them to output a single rating *** 
#    #2 Takes the three middlle scores out of the five, discrading the highest ***
#       and lowest since the highest and lowest scores might be outliers and skew the results ***
#    #3 The mean(average) of those three scores ***
#    #4 Turn average into rating ***

## Avarge scores     Rating ##
## 0 <= score < 1	Terrible ##
## 1 <= score < 2	Bad ##
## 2 <= score < 3	OK ##
## 3 <= score < 4	Good ##
## 4 <= score <= 5	Excellent ##

def conv2num(score):
    ## Convert the score to numerical type ##
    convScore = float(score)
    return convScore

def midThreeSum(score1, score2, score3, score4, score5):
    ## Find the sum of the middle three numbers out of the five ##
    scoreMax = max(score1, score2, score3, score4, score5)
    scoreMin = min(score1, score2, score3, score4, score5)
    sum = score1 + score2 + score3 + score4 + score5 - scoreMax - scoreMin
    return sum

def score2rateStr(average):
    # Convert the average score into a string rating (between 0 - 5) ##
    if average < 1:
        rate = "terrible"
    elif average < 2:
        rate = "bad"
    elif average < 3:
        rate = "OK"
    elif average < 4:
        rate = "Good"
    else:
        rate = "excellent"
    return rate

def scores2Rate(score1, score2, score3, score4, score5):
    # STEP 1 convert scores to numbers ##
    score1 = conv2num(score1)
    score2 = conv2num(score2)
    score3 = conv2num(score3)
    score4 = conv2num(score4)
    score5 = conv2num(score5)

    # STEP 2 find middle three scores ##
    # STEP 3 take average of middle three scores ##
    aveScore = midThreeSum(score1, score2, score3, score4, score5)/3

    # STEP 4 turn average score into a rating ##
    rate = score2rateStr(aveScore)
    score2rateStr
    return rate