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


def compare(s, t):
    for k in s.keys():
        if k in t.keys():
            if s[k] != t[k]:
                print("s[k]:" + str(k) + ': ' + str(s[k]))
                print("t[k]:" + str(k) + ': ' + str(t[k]))

        else:  print("t Do not have key:" + str(k) + '  value:  ' +  str(s[k]))


def __main():
    sham = {}
    sspam = {}
    tham = {}
    tspam = {}

    unpack([0], [0], [0], sspam, [0], sspam, [0])
    unpacky([0], [0], [0], tspam, [0], tspam, [0])

    print('compare ham:')
    compare(sham, tham)

    print()
    print()
    print('compare spam:')
    compare(sspam, tspam)




__main()