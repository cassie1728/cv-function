import random
import sys
from PIL import Image
import numpy as np
import os

class resizeNormalize:

    def __init__(self, size, interpolation=Image.BILINEAR):
        self.size = size
        self.threshold = size[0]*1.0 / size[1]
        self.interpolation = interpolation
        #self.toTensor = transforms.ToTensor()

    def __call__(self, img):
        new_img = Image.new('RGB', self.size, (0,0,0))
        img_w, img_h = img.size
        if img_w*1.0 / img_h > self.threshold:
            new_img = img.resize(self.size, self.interpolation)
        else:
            resize = (int(img_w*1.0/img_h*self.size[1]), self.size[1])
            img = img.resize(resize, self.interpolation)
            new_img.paste(img, (int((self.size[0] - resize[0]) / 2), 0))
        #img = self.toTensor(new_img)
        #img.sub_(0.5).div_(0.5)
        return new_img

img_list = os.listdir('./images/')
for img in img_list:
    im = Image.open('./images/'+img)
    imgW, imgH = im.size

    transform1 = resizeNormalize((100, 32))
    im = transform1(im)
    im.save("./image2/"+img)