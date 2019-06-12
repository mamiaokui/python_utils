from PIL import Image
import os
import os.path


dir_path =  r"/Users/mamk/Desktop/lookup/"
img_count = 9
def upside_down_file_list():
    for i in range (1, img_count):
        path = dir_path + str(i) + ".png"
        im = Image.open(path)

        out = im.transpose(Image.FLIP_TOP_BOTTOM)
        newname = dir_path + str(i)+ "_1.png"
        out.save(newname)


upside_down_file_list()