#   Author: Sasan Najar
#   Email: sasangnajar@gmail.com

#   This code is designed to:
##  STEP #1: Take as input a list of five answers from a quiz along with a list of the five correct solutions
##  STEP #2: Checks the answers against the solutions and outputs a message
##  STEP #3: Checks each answer, and then it adds up the number of correct and incorrect answers, and then it outputs a message.

def chkAnswer(userAnswer, key):
    if userAnswer == key:
        return True
    else:
        return False

def chkAnswers(userAnswers, keys):
    # check the answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(userAnswers)):
        results.append(chkAnswer(userAnswers[i], keys[i]))
    countCorrect = 0

    for result in results:
        if result:
            countCorrect += 1

    score = "Your correct answers are " + str(countCorrect) + " out of 5."
    if countCorrect/len(results) > 0.7:
        return "You passed with the score of " + score
    elif (len(results) - countCorrect)/len(results) >= 0.3:
        return "You failed. Your score is " + score