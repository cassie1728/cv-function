import os
import lmdb
from PIL import Image
import cStringIO

def merge_lmdb(lmdb_list, lmdb_result):
    env_result = lmdb.open(lmdb_result, map_size=1099511627776)
    txn_result = env_result.begin(write=True)
    print txn_result

    total = 0
    image_index = 0
    label_index = 0
    for index, one_lmdb in enumerate(lmdb_list):
        print index, one_lmdb
        env = lmdb.open(one_lmdb)
        txn = env.begin()
        database = txn.cursor()

        count = 0
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
                new_key = 'image-%09d' % image_index
            elif 'label' in key:
                label_index += 1
                new_key = "label-%09d" % label_index
            else:
                continue

            txn_result.put(new_key, value)
            count = count + 1
            total = total + 1
            if count % 1000 == 0:
                txn_result.commit()
                print "Written %d / %d" %(total, count)
                count = 0
                txn_result = env_result.begin(write=True)

        if count != 0:
            txn_result.commit()
            txn_result = env_result.begin(write=True)
            print "Written %d / %d" %(total, count)

    txn_result.put('num-samples', str(image_index))
    txn_result.commit()
    env_result.close()
        
def test():
    env = lmdb.open("./20180504/test_lmdb/", map_size=1099511627776)
    txn = env.begin()
    database = txn.cursor()

    for key, value in database:
        if key == "num-samples":
            print "num-samples:", value
    raw_input()

if __name__ == "__main__":
    #test()
    lmdb_list = ["/data/heneng/data/scene/20180502/", "/data/heneng/data/scene/20171122/", "/data/heneng/data/scene/20170829-1/"]

    lmdb_result = "./20180504-1/"
    if os.path.exists(lmdb_result):
        os.system("rm -r " + lmdb_result)
    os.system("mkdir " + lmdb_result)

    # train lmdb
    train_lmdb = []
    for one_lmdb in lmdb_list:
        train_lmdb.append(one_lmdb+"train_lmdb")

    merge_lmdb(train_lmdb, lmdb_result + "train_lmdb")

    # test lmdb
    test_lmdb = []
    for one_lmdb in lmdb_list:
        test_lmdb.append(one_lmdb+"test_lmdb")

    merge_lmdb(test_lmdb, lmdb_result + "test_lmdb")
