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
    f = open(packName, 'r', encoding='latin1')

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




def computeSpam(spamDict, spamWordOccurence, path, vocabularySize, pSpam, hamDict):
    f = open(path, 'r', encoding='latin1')
    result = 0.0
    result += math.log(pSpam)

    for line in f:
        for word in line.split():
            if word in spamDict.keys():
                numerator = spamDict[word] + 1
                denumerator = int(spamWordOccurence[0]) + int(vocabularySize[0])
                p = float(numerator/denumerator)
                result += math.log(p)
            elif word in hamDict.keys():
                numerator = 1
                denumerator = int(vocabularySize[0])
                p = float(numerator/denumerator)
                result += math.log(p)
            else: continue
    f.close()
    return result

def computeHam(hamDict, hamWordOccurence, path, vocabularySize, pHam, spamDict):
    f = open(path, 'r', encoding='latin1')
    result = 0.0
    result += math.log(pHam)

    for line in f:
        for word in line.split():
            if word in hamDict.keys():
                numerator = hamDict[word] + 1
                denumerator = int(hamWordOccurence[0]) + int(vocabularySize[0])
                p = float(numerator/denumerator)
                result += math.log(p)
            elif word in spamDict.keys():
                numerator = 1
                denumerator = int(vocabularySize[0])
                p = float(numerator/denumerator)
                result += math.log(p)
            else: continue
    f.close()
    return result


def isHam(hamP, spamP):
    if hamP > spamP:   return True
    elif hamP < spamP: return False
    else:
        decide = random.randint(1, 2)
        if(decide == 1): return True
        elif(decide == 2): return False
        else:
            print("there are something wrong with random number.")
            raise NameError("random number is not 1 or 2")

def __main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help='the path as input for classifier')
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
        f = open(outputName, 'x+', encoding='latin1')
    except FileExistsError:
        f = open(outputName, 'w', encoding='latin1')

    for root, dirs, files in os.walk(arg_str):
        for file in files:
            if file.endswith('.txt'):
                absPath = os.path.join(root, file)
                hamP = computeHam(hamDict, hamWordsOccurence, absPath, vocabularySize, pHam, spamDict)
                spamP = computeSpam(spamDict, spamWordsOccurence, absPath, vocabularySize, pSpam, hamDict)
                if isHam(hamP, spamP):
                    f.write('ham ' + absPath + '\n')
                else:
                    f.write('spam ' + absPath + '\n')
            else:
                continue

    f.close()
    print("nbisHam main done.")

__main()



# def computeP(hamDict, spamDict, hamWordOccurence, spamWordOccurence, path, vocabularySize, pHam, pSpam, mode):
#     f = open(path, 'r', encoding='latin1')
#     result = 0.0
#     # change resultß and di ct reference according to the class
#     if mode == 'spam':
#         result += math.log(pSpam)
#         dict = spamDict
#         otherDict = hamDict
#         wordOccurence = hamWordOccurence[0]
#     elif mode == 'ham':
#         result += math.log(pHam)
#         dict = hamDict
#         otherDict = spamDict
#         wordOccurence = spamWordOccurence[0]
#     else:
#         raise NameError("Compute P: wrong mode given")
#
#     #read words in file
#     for line in f:
#         # line.strip()
#         for word in line.split():
#             # word.strip()
#             if word in dict.keys():
#                 p = (dict[word] + 1) / (wordOccurence + vocabularySize[0])
#                 result += math.log(p)
#             elif word in otherDict.keys():
#                 p = 1 / vocabularySize[0]
#                 result += math.log(p)
#             else:
#                 continue
#     f.close()
#     return result