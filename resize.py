import os
from PIL import Image

def resize_image():
    # 获取输入文件夹中的所有文件
    files = os.listdir("./1_img/")

    output_dir = "./re_img/"
    # 判断输出文件夹是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in files:
        img = Image.open("./1_img/"+ file)
        if img.mode == "P":
            img = img.convert('RGB')
        if img.mode == "RGBA":
            img = img.convert('RGB')
        img = img.resize((608, 608), Image.ANTIALIAS)
        img.save(os.path.join(output_dir, file))


if __name__ == '__main__':
    resize_image()
