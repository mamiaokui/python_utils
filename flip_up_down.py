from PIL import Image
import os
import os.path


def upside_down_file_list():
    for i in range (1, 73):
        if i % 2 == 1:
            continue
        path = r"/Users/mamk/Documents/opengles/filter/filter/"+str(i)+".png"
        im = Image.open(path)

        out = im.transpose(Image.FLIP_TOP_BOTTOM)
        newname=r"/Users/mamk/Documents/opengles/filter/filter/"+str(i)+"_1.png"
        out.save(newname)
        if os.path.exists(path):
            os.remove(path)


path = r"/tmp/abcdefg.png"
im = Image.open(path)

out = im.transpose(Image.FLIP_TOP_BOTTOM)
newname = r"/tmp/abcdefgh.png"
out.save(newname)

with open("imageToSave.png", "wb") as fh:
    fh.write(img_data.decode('base64'))