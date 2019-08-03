import os
from PIL import Image

def crop_bbox(img_path,text,save_path,titles_label):
    with open(text,'r') as f1,open(titles_label,'a') as f2:
        lines = f1.readlines()
        for line in lines:
            line = line.strip('\n')
            words = line.split('\t')
            file_name = words[0]
            for i in range(1, len(words), 2):
                title_index = i/2
                rect_info = words[i]
                label = words[i+1]
                bbox = map(int,rect_info.split(','))
                [x1,y1,w,h] = bbox
                x2 = x1 + w
                y2 = y1 + h

                src_img = Image.open(os.path.join(img_path+file_name))
                src_img = src_img.crop((x1,y1,x2,y2))
                s='%02d' %title_index
                save_img = file_name[:-4] + '_'+ s + '.jpg'
                src_img.save(save_path + save_img)
                f2.write(save_img+'\t'+label+'\n')


if __name__ == "__main__":
    if not os.path.exists("./crop_img"):
        os.mkdir("./crop_img")
    crop_bbox("./ocr_data/","./new_result_f1.txt","./crop_img/",'./titles_label.txt')
    print ("Finish!")
