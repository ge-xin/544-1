import argparse
import os


def count(f, dict, totalWords, wordSet):
    for line in f:
        line.strip()
        for word in line.split():
            word.strip()
            wordSet.add(word)
            totalWords[0] = totalWords[0] + 1
            if(word in dict.keys()):
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

def learn(filePath, dict, totalWords, wordSet, numOfFile):
    numOfFile[0] += 1
    f = open(filePath, "r", encoding = "latin1")
    count(f, dict, totalWords, wordSet)
    f.close()

def pack(vocabularySize, numOfHamFile, numOfSpamFile, hamDict, hamWordOccurence, spamDict, spamWordOccurence):
    hamDictSize = len(hamDict)
    spamDictSize = len(spamDict)

    '''
    the format of pack
    vocabularySize
    numOfHamFile
    numOfSpamFile
    hamWordOccurence
    hamDictSize
    hamDict
    spamWordOccurence
    spamDictSize
    spamDict
    '''

    packName = 'nbmodel.txt'
    try:
        f = open(packName, 'x+', encoding='latin1')
    except FileExistsError:
        f = open(packName, 'w', encoding='latin1')
    f.write(str(vocabularySize) + '\n')

    f.write(str(numOfHamFile[0])+ '\n')
    f.write(str(numOfSpamFile[0]) + '\n')

    f.write(str(hamWordOccurence[0]) + '\n')
    f.write(str(hamDictSize) + '\n')
    for k in hamDict.keys():
        f.write(k + " " + str(hamDict[k]) + '\n')

    f.write(str(spamWordOccurence[0]) + '\n')
    f.write(str(spamDictSize) + '\n')
    for k in spamDict.keys():
        f.write(k + " " + str(spamDict[k]) + '\n')

    #print("pack is working")
    f.close()

def unpack(vocabularySize, numOfHamFile, numOfSpamFile, hamDict, hamWordOccurence, spamDict, spamWordOccurence):

    packName = "nbmodel.txt"
    f = open(packName, 'r', encoding='latin1')

    vocabularySize[0] = int(f.readline())
    numOfHamFile[0] = int(f.readline())
    numOfSpamFile[0] = int(f.readline())
    hamWordOccurence[0] = int(f.readline())
    hamDictSize = int(f.readline())

    for i in range(0, hamDictSize, 1):
        words = f.readline().split()
        k = words[0]
        v = int(words[1])
        hamDict[k] = v

    spamWordOccurence[0] = int(f.readline())
    spamDictSize = int(f.readline())

    for i in range(0, spamDictSize, 1):
        words = f.readline().split()
        k = words[0]
        v = int(words[1])
        spamDict[k] = v

def __main():
    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="the path as input")
    arg = parser.parse_args()
    arg_str = arg.path

    numOfSpamFile = [0]
    numOfHamFile = [0]
    spamWordOccurence = [0]
    hamWordOccurence = [0]
    spamDict = {}
    hamDict = {}
    wordSet = set()

    for root, dirs, files in os.walk(arg_str):
        for file in files:
            filePath = os.path.join(root, file)
            # print(filePath, end=' ')
            if root.endswith('ham'):
                if filePath.endswith('.txt'):
                    learn(filePath, hamDict, hamWordOccurence, wordSet, numOfHamFile)
            elif root.endswith('spam'):
                if filePath.endswith('.txt'):
                    learn(filePath, spamDict, spamWordOccurence, wordSet, numOfSpamFile)
            else:
                continue
                # print("Do Nothing:")
    '''
    ham = 0
    for k in hamDict.keys():
        ham += hamDict[k]

    spam = 0
    for k in spamDict.keys():
        spam += spamDict[k]
    '''

    pack(len(wordSet), numOfHamFile, numOfSpamFile, hamDict, hamWordOccurence, spamDict, spamWordOccurence)

    '''
     # Following are test message
        aTotalVocabularySize = [0]
        aNumOfHamFile = [0]
        aNumOfSpamFile = [0]
        aHamDict = {}
        ahamWordOccurence = [0]
        aSpamDict = {}
        aspamWordOccurence = [0]
        unpack(aTotalVocabularySize, aNumOfHamFile, aNumOfSpamFile, aHamDict, ahamWordOccurence, aSpamDict, aspamWordOccurence)

        if aTotalVocabularySize[0] != len(wordSet):   print("totalVocabulary Wrong!")
        if aNumOfHamFile[0] != numOfHamFile[0]:    print("numOfHamFile Wrong!")
        if aNumOfSpamFile[0] != numOfSpamFile[0]:   print("numOfSpamFile Wrong!")
        if aHamDict != hamDict: print("hamDict Wrong!")
        if ahamWordOccurence != hamWordOccurence: print("hamWordOccurence Wrong!")
        if aSpamDict != spamDict:  print("spamDict Wrong!")
        if aspamWordOccurence != spamWordOccurence: print("spamWordOccurence Wrong!")
        print("Done.")
    '''
__main()
