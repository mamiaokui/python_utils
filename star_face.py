#coding=utf-8
import os
import hashlib
import face
import dbscan
import database
import numpy as np
import faiss

def process_one_star(name, db):
    hl = hashlib.md5()
    hl.update(name.encode(encoding='utf-8'))
    md5 = hl.hexdigest()
    output_image_path = "/tmp/face/%s/image" % (md5)
    if not os.path.exists(output_image_path):
        command = "/Users/mamk/venv/flower_world/bin/python /Users/mamk/ssd/Image-Downloader/image_downloader.py --engine Baidu --max-number 200 --num-threads 20 --timeout 5 --output %s %s" % (output_image_path, name)
        command = command.encode('utf-8')
        #command = "/Users/mamk/venv/flower_world/bin/python /Users/mamk/ssd/Image-Downloader/image_downloader.py --engine Baidu --max-number 200 --num-threads 10 --timeout 5 --output %s %s" % (output_path, name)
        print(command)
        os.system(command)
    output_face_path = "/tmp/face/%s/face" % (md5)
    if not os.path.exists(output_face_path):
        face.process_image(output_image_path, output_face_path)

    output_result_path = "/tmp/face/%s/result" % (md5)
    embd = None
    if not os.path.exists(output_result_path) or True:
        embd = dbscan.process(output_face_path, output_result_path)

    if embd is None:
        return

    embd = np.array(embd)
    embd = embd.tostring().encode("base64")
    db.insert(name, embd)


def create():
    db = database.EmbdedDatabase()
    db.open(drop_exist=True)
    stars = [u"王宝强", u"刘德华", u"郑爽", u"赵丽颖", u"宋佳", u"关之琳", u"霸王别姬张国荣", u"张卫健", u"王宝强马蓉"]
    # stars = [u"范冰冰李晨",u"王宝强马蓉", u"宋佳", u"霸王别姬张国荣", u"长得像王宝强"]
    # stars = [u"霸王别姬张国荣", u"张国荣"]

    for star in stars:
        process_one_star(star, db)

    embd = db.get_embd()
    print embd

def search(search_embd):
    db = database.EmbdedDatabase()
    db.open(drop_exist=False)
    embd = db.get_embd()
    num = np.asarray(embd)
    arr = num[:,1]
    float_arr = []
    for i in range(arr.shape[0]):
        temp = np.fromstring(arr[i].decode("base64"))
        float_arr.append(temp)
    float_arr = np.asarray(float_arr)

    index = faiss.IndexFlatL2(128)
    print(index.is_trained)
    float_arr = float_arr.astype('float32')
    index.add(float_arr)  # add vectors to the index
    k = 4  # we want to see 4 nearest neighbors
    print(index.ntotal)

    temp = []
    temp.append(search_embd)
    query = np.asarray(temp)
    D, I = index.search(query, k)
    #D, I = index.search(float_arr, k)

    print(embd[I[0][0]][0])
    print(D)



if __name__ == "__main__":
    #create()
    filename, embd = dbscan.calc_embded(["/tmp/face/95d50dd624df9a4bde2a41629d2310a1/result/negative1/Baidu_0042.jpeg"])
    embd = np.array(embd)
    embd = embd.astype('float32')
    search(embd[0])