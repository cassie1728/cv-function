import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import os

save_path='./result_re.txt'

if os.path.exists(save_path):
    os.remove(save_path)

with open('./result.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        words = line.split("\t")
        re = words[1].replace("━","一")
        re = re.replace("─","一")
        re = re.replace("—", "一")
        re = re.replace("─", "一")
        re = re.replace("–", "一")
        re = re.replace("'", '"')
        re = re.replace("'", '"')
        re = re.replace("_","")
        re = re.replace("廬","盧")
        re = re.replace("巿","市")
        re = re.replace(";",":")
        re = re.replace("旳","的")
        re = re.replace("″",'"')
        re = re.replace('“', '"')
        re = re.replace('”','"')
        re = re.replace("∵",":")
        with open(save_path,'a') as f_pp:
            f_pp.write(words[0]+'\t'+re + '\n')