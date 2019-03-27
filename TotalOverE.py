import math
import numpy as np

def randomTrain():
    actual = np.random.uniform(1, 1000, 1000)
    #actual = np.around(actual)
    #print(actual)
    #totalCount = int(input('Number of values?: '))
    totalCount = len(actual)
    sampleSize = totalCount // math.e
    sample = []
    for i in range(totalCount):
        #userAnswer = int(input('%s Enter a value: ' %i))
        userAnswer = actual[i]
        if (i < sampleSize):
            sample.append(userAnswer)
            #print(sample)
            continue
        if (userAnswer > np.amax(sample)):
            return (userAnswer, np.amax(actual), np.amax(sample))

    return (0, np.amax(actual), np.amax(sample))
    

correctGuesses = 0
for i in range(100):
    predict, actual, temp = randomTrain()
    if (predict == actual):
        correctGuesses += 1

print(correctGuesses)
