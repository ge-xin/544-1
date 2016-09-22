import os
import random
import shutil

def __main():
    source = '/Users/Xin/Downloads/544-1'
    spam_lst = []
    spam_name = []
    ham_lst = []
    ham_name = []
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith('.ham.txt'):
                abs_path = os.path.join(root, file)
                ham_lst.append(abs_path)
                ham_name.append(file)
            elif file.endswith('.spam.txt'):
                abs_path = os.path.join(root, file)
                spam_lst.append(abs_path)
                spam_name.append(file)
            else: continue

    spam_size = len(spam_lst)
    ham_size = len(ham_lst)

    spam_fetch = round(0.1 * spam_size)
    ham_fetch = round(0.1 * ham_size)

    root = '/Users/Xin/Desktop/Pick/'
    train = root + 'train/'
    dev = root + 'dev/'
    try:
        shutil.rmtree(root)
    except:
        print('No pick folder, continue')
    dirs = [root, train, dev, train + 'ham/', train + 'spam/', dev + 'ham/', dev + 'spam/']
    for dir in dirs:

        try:
            os.stat(dir)
        except:
            os.mkdir(dir)

    while spam_fetch > 0:
        i = random.randint(0, (len(spam_lst) - 1))
        shutil.copyfile(spam_lst[i], train + 'spam/' + spam_name[i])
        spam_lst.remove(spam_lst[i])
        spam_name.remove(spam_name[i])
        spam_fetch -= 1
    while ham_fetch > 0:
        i = random.randint(0, (len(ham_lst) - 1))
        shutil.copyfile(ham_lst[i], train + 'ham/' + ham_name[i])
        ham_lst.remove(ham_lst[i])
        ham_name.remove(ham_name[i])
        ham_fetch -= 1

    for i in range(len(spam_lst)):
        shutil.copyfile(spam_lst[i], dev + 'spam/' + spam_name[i])
    for i in range(len(ham_lst)):
        shutil.copyfile(ham_lst[i], dev + 'ham/' + ham_name[i])

__main()