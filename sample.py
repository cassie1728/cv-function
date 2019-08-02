import os, random, shutil

def copyFile(fileDir):
    pathDir = os.listdir(fileDir)

    sample = random.sample(pathDir, 200)
    print sample

    for name in sample:
        shutil.copyfile(fileDir+name, tarDir+name)

    with open('./image_train_fi/train_label_fi.txt','r') as f1,open('./sample/sample.txt','a')as f2:
        lines=f1.readlines()
        for line in lines:
            line=line.strip('\n')
            words=line.split('\t')
            if words[0] in sample:
                f2.write(line+'\n')


if __name__ == '__main__':
    fileDir = "./image_train_fi/"
    tarDir = './sample/'
    if not os.path.exists(tarDir):
        os.makedirs(tarDir)
    else:
        os.rmdir(tarDir)
        os.makedirs(tarDir)

    copyFile(fileDir)
