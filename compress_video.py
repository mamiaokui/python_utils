import sys
import time
import os
import datetime
from apscheduler.schedulers.background import BackgroundScheduler



def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files

def create_dirs(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def process():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    files = list_all_files(input_dir)

    for file_name in files:
        try:
            file_name_base= os.path.basename(file_name)
            file_name_base = file_name_base.split(".")[0]
            time_value = int(file_name_base.split("_")[1])
            print(file_name_base)
            timeArray = time.localtime(time_value)
            file_name_full = time.strftime("%Y_%m_%d_%H_%M_%S", timeArray)
            file_name_full += ".mp4"
            file_name_hour = time.strftime("%Y%m%d%H", timeArray)
            file_name_hour = os.path.join(output_dir, file_name_hour)
            create_dirs(file_name_hour)
            output_path = os.path.join(file_name_hour, file_name_full)
            command = "ffmpeg -y -i %s -vf scale=320:-1 %s" %(file_name, output_path)
            print(command)
            ret = os.system(command)
            if ret == 0:
                os.remove(file_name)
        except:
            pass


def schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process, 'interval', seconds=2)
    scheduler.start()


if __name__ == "__main__":
    schedule()
    while True:
        time.sleep(1000)
