# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import random
import os

with open('./bbox_label.txt') as f:
    lines = f.readlines()
    random.seed(1234)
    train = random.sample(lines, 4500) 
    test = list(set(lines).difference(set(train)))
    with open("./train_label.txt", "w") as f1:
        for i in train:
            f1.write(i)
    with open("./test_label.txt", "w") as f2:
        for j in test:
            f2.write(j)