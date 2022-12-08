#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        for i in range(len(sentence)):
            sentence = None
            
    if sentence:
        for i in range(len(sentence)):
            return len(sentence), sentence[0]