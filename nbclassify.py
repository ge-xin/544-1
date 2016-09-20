import argparse
import os
import random
import math


def unpack(vocabularySize, numOfHamFile, numOfSpamFile, hamDict, hamWordsOccurence, spamDict, spamWordsOccurence):

    '''
    the format of pack
    vocabularySize
    numOfHamFile
    numOfSpamFile
    hamWordsOccurence
    hamDictSize
    hamDict
    spamWordsOccurence
    spamDictSize
    spamDict
    '''

    packName = "nbmodel.txt"
    f = open(packName, 'r')

    vocabularySize[0] = int(f.readline())
    numOfHamFile[0] = int(f.readline())
    numOfSpamFile[0] = int(f.readline())
    hamWordsOccurence[0] = int(f.readline())
    hamDictSize = int(f.readline())

    for i in range(0, hamDictSize, 1):
        words = f.readline().split()
        k = words[0]
        v = int(words[1])
        hamDict[k] = v

    spamWordsOccurence[0] = int(f.readline())
    spamDictSize = int(f.readline())

    for i in range(0, spamDictSize, 1):
        words = f.readline().split()
        k = words[0]
        v = int(words[1])
        spamDict[k] = v

def unpacky(vocabularySize, numOfHamFile, numOfSpamFile, hamDict, hamWordsOccurence, spamDict, spamWordsOccurence):
    packName = 'nbmodel1.txt'

    f = open(packName, 'r', encoding='latin1')
    vocabularySize[0] = int(f.readline().strip())
    numOfHamFile[0] = int(f.readline().strip())
    hamWordsOccurence[0] = int(f.readline().strip())

    line = f.readline().strip()
    while line != '---------':
        words = line.split(' ')
        hamDict[words[0]] = int(words[1])
        line = f.readline().strip()

    numOfSpamFile[0] = int(f.readline().strip())
    spamWordsOccurence[0] = int(f.readline().strip())

    line = f.readline().strip()
    count = 0
    while line != '':
        words = line.split(' ')
        spamDict[words[0]] = int(words[1])
        line = f.readline().strip()

    '''
    # ham dict
    for line in f:
        line.strip()
        if (line == "---------"): break
        words = line.split()
        k = words[0]
        v = words[1]
        hamDict[k] = v

    numOfSpamFile[0] = int(f.readline())
    spamWordsOccurence[0] = int(f.readline())
    # spam dict
    for line in f:
        words = line.split()
        k = words[0]
        v = words[1]
        spamDict[k] = v
    '''





def computeScore(hamDict, spamDict, wordOccurence, path, vocabularySize, pHam, pSpam, mode):
    f = open(path, 'r', encoding='latin1')
    score = 0.0
    # change score and dict reference according to the class
    if mode == 'spam':
        score = score + math.log2(pSpam)
        dict = spamDict
        otherDict = hamDict
    elif mode == 'ham':
        score = score + math.log2(pHam)
        dict = hamDict
        otherDict = spamDict
    else:
        raise NameError("Compute Score: wrong mode given")

    #read words in file
    for line in f:
        for word in line.split():
            if word in dict.keys():
                wordScore = math.log2((dict[word] + 1) / (wordOccurence[0] + vocabularySize[0]))
                score = score + wordScore
            elif word in otherDict.keys():
                wordScore = math.log2(1 / vocabularySize[0])
                score = score + wordScore
            else:
                continue
    f.close()
    return score


def classify(hamScore, spamScore):
    if(hamScore > spamScore):   return True
    elif(hamScore < spamScore): return False
    else:
        decide = random.randint(1, 2)
        if(decide == 1): return True
        elif(decide == 2): return False
        else:
            print("there are something wrong with random number.")
            raise NameError("random number is not 1 or 2")

def __main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help = 'the path as input for classifier')
    arg = parser.parse_args()
    arg_str = arg.path

    vocabularySize = [0]
    numOfHamFile = [0]
    numOfSpamFile = [0]
    spamWordsOccurence = [0]
    hamWordsOccurence = [0]
    spamDict = {}
    hamDict = {}

    # unpack(vocabularySize, numOfHamFile, numOfSpamFile, hamDict, hamWordsOccurence, spamDict, spamWordsOccurence)
    unpacky(vocabularySize, numOfHamFile, numOfSpamFile, hamDict, hamWordsOccurence, spamDict, spamWordsOccurence)

    numOfFile = numOfHamFile[0] + numOfSpamFile[0]
    pHam = float(numOfHamFile[0] / numOfFile)
    pSpam = float(numOfSpamFile[0] / numOfFile)

    outputName = 'nboutput.txt'
    try:
        f = open(outputName, 'x+')
    except FileExistsError:
        f = open(outputName, 'w')

    for root, dirs, files in os.walk(arg_str):
        for file in files:
            if file.endswith('.txt'):
                absPath = os.path.join(root, file)
                print(absPath, end = ' ')
                # print(absPath)
                hamScore = computeScore(hamDict, spamDict, hamWordsOccurence, absPath, vocabularySize, pHam, pSpam, 'ham')
                spamScore = computeScore(hamDict, spamDict, spamWordsOccurence, absPath, vocabularySize, pHam, pSpam, 'spam')
                if classify(hamScore, spamScore) :
                    f.write('ham ' + absPath + '\n')
                else:
                    f.write('spam ' + absPath + '\n')
            else:
                continue

    f.close()
    print("nbclassify main done.")

__main()
