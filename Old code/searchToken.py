import argparse
import os


def search(filePath, keyword):
    f = open(filePath, "r", encoding = "latin1")
    for line in f:
        for word in line.split():
            if word == keyword:
                print('find keyword: ' + keyword+' in file:' + filePath)
                return

def __main():
    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="the path as input")
    arg = parser.parse_args()
    arg_str = arg.path

    keyword = 'más'

    for root, dirs, files in os.walk(arg_str):
        for file in files:
            filePath = os.path.join(root, file)
            if filePath.endswith('txt'):
                search(filePath, keyword)


__main()
