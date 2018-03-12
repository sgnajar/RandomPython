def punctuate(sentence, type):
    
    """ Defaults to an ordinary sentence with a full stop.
    sentence: string, the phrase that is to have punctuation added
    type: string, defines what kind of sentence to create."""

    if type == "exclamation":
        sentencePunct = sentence + "!"
    elif type == "question":
        sentencePunct = sentence + "?"
    elif type == "aside":
        sentencePunct = "(" + sentence + ".)"
    else:
        sentencePunct = sentence + "."
    return sentencePunct