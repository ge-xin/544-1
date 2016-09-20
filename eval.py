import os


def eval():
    f = open('nboutput.txt', 'r', encoding = 'latin1')

    actualHams = 0
    actualSpams = 0

    hams = 0
    spams = 0

    correctHams = 0
    correctSpams = 0

    for line in f:
        words = line.split()

        result = words[0]
        file = words[1]

        if file.endswith('.ham.txt'):  actualHams += 1
        elif file.endswith('.spam.txt'): actualSpams += 1
        else: raise KeyError("Eval: bad filename")

        if(result == 'ham'): hams += 1
        elif(result == 'spam'): spams += 1
        else: raise KeyError("Eval: result")

        if((result == 'ham') and (file.endswith('.ham.txt'))): correctHams += 1
        elif((result == 'spam') and (file.endswith('.spam.txt'))): correctSpams +=1
        else: continue

    print("Spam:")
    print('Precision: ' + str(correctSpams / spams) + ' ' + 'Recall: ' + str(correctSpams / actualSpams))
    print("Ham:")
    print('Precision: ' + str(correctHams / hams) + ' ' + 'Recall: ' + str(correctHams / actualHams))
eval()
