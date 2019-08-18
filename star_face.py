#coding=utf-8
import os
import hashlib
import face
import dbscan
import database
import numpy as np
import faiss
import face_recognition

def process_one_star(name, db):
    hl = hashlib.md5()
    hl.update(name.encode(encoding='utf-8'))
    md5 = hl.hexdigest()
    output_image_path = "/tmp/face/%s/image" % (md5)
    if not os.path.exists(output_image_path):
        #command = "/Users/mamk/venv/flower_world/bin/python /Users/mamk/ssd/Image-Downloader/image_downloader.py --engine Google --max-number 200 --num-threads 20 --timeout 5 --output %s %s" % (output_image_path, name)
        command = "/Users/mamk/venv/flower_world/bin/python /Users/mamk/ssd/Image-Downloader/image_downloader.py --engine Google --max-number 20 --num-threads 20 --timeout 2 --face-only --output %s %s" % (output_image_path, name)
        command = command.encode('utf-8')
        #command = "/Users/mamk/venv/flower_world/bin/python /Users/mamk/ssd/Image-Downloader/image_downloader.py --engine Baidu --max-number 200 --num-threads 10 --timeout 5 --output %s %s" % (output_path, name)
        #print(command)
        os.system(command)
    output_face_path = "/tmp/face/%s/face" % (md5)
    if not os.path.exists(output_face_path):
        face.process_image(output_image_path, output_face_path)

    output_result_path = "/tmp/face/%s/result" % (md5)
    embd = None
    print(name)
    print(md5)
    if not os.path.exists(output_result_path) or True:
        embd = dbscan.process(output_face_path, output_result_path)

    if embd is None:
        return

    embd = np.array(embd)
    #embd = embd.tostring().encode("base64")
    name = name.replace("\ ", " ")
    db.insert(name, embd)


def create():
    db = database.EmbdingDatabase()
    db.open(drop_exist=True)
    #stars = [u"王宝强", u"刘德华", u"郑爽", u"赵丽颖", u"宋佳", u"关之琳", u"霸王别姬张国荣", u"张卫健", u"王宝强马蓉"]
    # stars = [u"范冰冰李晨",u"王宝强马蓉", u"宋佳", u"霸王别姬张国荣", u"长得像王宝强"]
    # stars = [u"霸王别姬张国荣", u"张国荣"]
    #stars = [u"\"Baby \(I\) Taapsee Pannu\""]
    #stars = []
    stars = [u"Virat\ Kohli",u"MS\ Dhoni",u"Rohit\ Sharma",u"Jasprit\ Bumrah",u"Shikhar\ Dhawan",u"KL\ Rahul",u"Hardik\ Pandya",u"Rishabh\ Pant",u"Mayank\ Agrwal",u"Yuzvendra\ Chahal",u"Kedar\ Jadhav",u"Dinesh\ Karthik",u"Kuldeep\ Yadav",u"Bhuvneshwar\ Kumar",u"Mohammed\ Shami",u"Vijay\ Shankar",u"Shreyas\ Iyer",u"Prithvi\ Shaw",u"Umesh\ Yadav",u"Manish\ Pandey",u"Shumman\ Gill",u"Sachin\ Tendulkar",u"Virender\ Sehwag",u"Rahul\ Dravid",u"Sourav\ Ganguly",u"Anil\ Kumble",u"Yuvraj\ Singh",u"Harbhajan\ Singh",u"Gautam\ Gambhir",u"Irfan\ Pathan",u"VVS\ Laxman",u"Parthiv\ Patel", u"Hrithik\ Roshan",u"Salman\ Khan",u"Dharmendra",u"Shahid\ Kapoor",u"Ranbir\ Kapoor",u"Ranveer\ Singh",u"Aditya\ Roy\ Kapur",u"Sidharth\ Malhotra",u"Arjun\ Kapoor",u"Harshvardhan\ Kapoor",u"Vicky\ Kaushal",u"Ayushamann\ Khurrana",u"Aparshakti\ Khurana",u"Diljit\ Dosanjh",u"Sunny\ Deol",u"Bobby\ Deol",u"Abhay\ Deol",u"Kunal\ Khemu",u"Saif\ Ali\ Khan",u"Shah\ Rukh\ Khan",u"Aryan\ Khan",u"Rohit\ Shetty",u"Prabhas",u"Ram\ Kapoor",u"Arbaaz\ Khan",u"Sohail\ Khan",u"Kartik\ Aaryan",u"Jimmy\ Sheirgill",u"Sushant\ Singh\ Rajput",u"Milind\ Soman",u"Aamir\ Khan",u"Irrfan\ Khan",u"Akshay\ Kumar",u"John\ Abraham",u"Abhishek\ Bachchan",u"Amitabh\ Bachchan",u"Karan\ Johar",u"Tiger\ Shroff",u"Pulkit\ Samrat",u"Vivek\ Oberoi",u"Anurag\ Kashyap",u"Vikas\ Bahl",u"Anand\ Ahuja",u"Arijit\ Singh",u"Armaan\ Malik",u"Abhijeet\ Sawant",u"Manoj\ Bajpayee",u"Jackie\ Shroff",u"Naseeruddin\ Shah",u"Rajkummar\ Rao",u"Riteish\ Deshmukh",u"Varun\ Dhawan",u"Ishaan\ Khatter",u"Katrina\ Kaif",u"Priyanka\ Chopra",u"Kiara\ Advani",u"Tara\ Sutaria",u"Malaika\ Arora",u"Ananya\ Panday",u"Kareena\ Kapoor",u"Disha\ Patani",u"Sapna\ Chaudhary",u"Sunny\ Leone",u"Karisma\ Kapoor",u"Sonam\ Kapoor",u"Shweta\ Bachchan",u"Aishwarya\ Rai\ Bachchan",u"Dia\ Mirza",u"Parineeti\ Chopra",u"Sushmita\ Sen",u"Riddhima\ Kapoor",u"Alia\ Bhatt",u"Vidya\ Balan",u"Taapsee\ Pannu",u"Bhumi\ Pednekar",u"Nargis\ Fakre",u"Deepika\ Padukone",u"Neha\ Dhupia",u"Amrita\ Arora",u"Amrita\ Singh",u"Sara\ Ali\ Khan",u"Janhvi\ Kapoor",u"Khushi\ Kapoor",u"Rhea\ Kapoor",u"Rhea\ Chakraborty",u"Sana\ Khan",u"Gauhar\ Khan",u"Monalisa",u"Kirti\ Kulhari",u"Rakul\ Preet\ Singh",u"Tabu",u"Kajol",u"Juhi\ Chawla",u"Madhuri\ Dixit",u"Raveena\ Tandon",u"Sonakshi\ Sinha",u"Radhika\ Apte",u"Radhika\ Madan",u"Sanya\ Malhotra",u"Celina\ Jaitley",u"Esha\ Deol",u"Esha\ Gupta",u"Konkana\ Sen\ Sharma",u"Mrunal\ Thakur",u"Shraddha\ Kapoor",u"Nithya\ Menen",u"Kriti\ Sanon",u"Iulia\ Vantur",u"Neha\ Kakkar",u"Amisha\ Patel",u"Preity\ Zinta",u"Shilpa\ Shetty",u"Rakhi\ Sawant",u"Ankita\ Lokhande",u"Kangana\ Ranaut"]
    #stars = [u"Virat\ Kohli", u"MS\ Dhoni", u"Rohit\ Sharma"]

    for star in stars:
        process_one_star(star, db)

    embd = db.get_embd()

def search(search_embd):
    db = database.EmbdingDatabase()
    db.open(drop_exist=False)
    embd = db.get_embd()
    num = np.asarray(embd)
    arr = num[:, 1]
    float_arr = []
    for i in range(arr.shape[0]):
        temp = arr[i]
        float_arr.append(temp)
    float_arr = np.asarray(float_arr)

    index = faiss.IndexFlatL2(128)
    #print(index.is_trained)
    float_arr = float_arr.astype('float32')
    index.add(float_arr)  # add vectors to the index
    k = 4  # we want to see 4 nearest neighbors
    #print(index.ntotal)

    temp = []
    temp.append(search_embd)
    query = np.asarray(temp)
    D, I = index.search(query, k)

    #print(embd[I[0][0]][0])
    #print(D[0])



if __name__ == "__main__":
    # create()
    #
    # filename, embd = dbscan.calc_embded(["/Users/mamk/Desktop/cz4.jpg"])
    # embd = np.array(embd)
    # embd = embd.astype('float32')
    # search(embd[0])
    path = "/Users/mamk/Desktop/cz4.jpg"
    face_recognition.face_landmarks()
