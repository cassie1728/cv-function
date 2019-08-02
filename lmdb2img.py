import os
import lmdb
from PIL import Image
import cStringIO

one_lmdb = '/data/zhangjiaxuan/ali-crnn.pytorch/ocr_generator/sample/train_lmdb/'
env = lmdb.open(one_lmdb)
txn = env.begin()
database = txn.cursor()

image_index = 0
for key, value in database:
    if "image" in key:
        try:
            im = Image.open(cStringIO.StringIO(value))
            if im.format != "JPEG":
                print im.format
            w, h = im.size
            if w <= 0 or h <=0:
                print "ERROR: This is a unvalid image!", key
                raw_input()
                continue
            im.save("./images/image-%09d.jpg" %image_index)
        except Exception as e:
            print "Error in loading image!", str(e)
            raw_input()
            continue
        image_index += 1