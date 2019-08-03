# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os

def findone(filename):
    with open('./result.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            words = line.split("\t")
            for i in range(len(words[0])):
                if words[0] == filename:
                    return line
                else:
                    continue

with open('./test_titles_label.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        words = line.split("\t")
        filename = words[0]
        list = findone(filename)
        with open("./result_re.txt", "a") as f:
            f.write(list + '\n')