import os
import json
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PIL import Image, ImageDraw, ImageFont
from multiprocessing import Pool

def draw_lines_for_rect(dr, rect, color, width):
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]

    dr.line((x1,y1,x2,y1), fill=color, width=width)
    dr.line((x2,y1,x2,y2), fill=color, width=width)
    dr.line((x1,y1,x1,y2), fill=color, width=width)
    dr.line((x1,y2,x2,y2), fill=color, width=width)

def draw_rect(src_img, rect):
    draw = ImageDraw.Draw(src_img)
    draw_lines_for_rect(draw, rect, color=(0,255,0), width=3)

    return src_img

def draw_text(src_img, text, rect):
    if len(text) == 0:
        return src_img
    print "len of text:", len(text), text
    text = text.decode('utf-8')
    fnt = ImageFont.truetype('./simhei.ttf', 30)
    d = ImageDraw.Draw(src_img)

    text_width, text_height = fnt.getsize(text)
    offset = rect[3] - rect[1] + 5 
    rect[1] += offset
    rect[3] += offset
    d.text(rect, text, font=fnt, fill=(255,0,0))

    return src_img

# draw text and rect onto the image.
def draw_text_and_rect_to_image(src_img, text, rect):
    text_img = draw_rect(src_img, rect)

    dst_img = draw_text(text_img, text, rect)

    return dst_img

def process(line):
    line = line.strip("\n")
    words = line.split("\t")
    words_len = len(words)
    if words_len < 1 or words_len%2 != 1:
        print "Unvalid line:", line
        return

    file_name = words[0]
    try:
        src_img = Image.open(os.path.join("./ocr_data/"+file_name))
    except Exception as e:
        print str(e)
        return

    for i in range(1, words_len-1, 2):
        bbox = words[i]
        label = words[i+1]

        bbox = map(int, bbox.split(","))
        [x1,y1,w,h] = bbox
        x2 = x1 + w
        y2 = y1 + h

        src_img = draw_text_and_rect_to_image(src_img, label, [x1,y1,x2,y2])

        save_name = "./test_result_t1/" + file_name
        src_img.save(save_name)

if __name__ == "__main__":
    if not os.path.exists("./test_result_t1"):
        os.mkdir("./test_result_t1")
    f = open("./new_result_t1.txt", 'r')
    lines = f.readlines()
    f.close()

    MP = False
    if MP == True:
        pool = Pool(processes=15)
        pool.map_async(process, lines)
        pool.close()
        pool.join()
    else:
        for line in lines:
            process(line)

    print "Finished!"

