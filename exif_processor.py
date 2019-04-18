import sys
import os
import datetime
import re

if __name__ == "__main__":

    origin_file_name = sys.argv[1]
    if len(sys.argv) > 2:
        origin_file_name = sys.argv[1] + "\ " + sys.argv[2]

    print "file name", origin_file_name
    command = "exif " + origin_file_name
    ret = os.popen(command).read()
    print command, "returns", ret
    if ret.lower() == "":
        command = "exif -c " + origin_file_name + " -o " + origin_file_name
        os.popen(command).read()
        ret = os.popen("exif " + origin_file_name).read()
        print command, "returns", ret


    file_name = origin_file_name

    if origin_file_name.startswith("20") != -1:
        file_name = re.sub(r'\D', " ", file_name)
        file_name = file_name.strip();
        split = file_name.split(" ")
        time = split[-1]
        time = datetime.datetime(int(split[0]), int(split[1]), int(split[2]), int(time[0:2]), int(time[2:4]), int(time[4:6]))
        time = str(time).replace("-", ":")
        time = time.replace(" ", "\ ")

        ret = os.popen("exif " + origin_file_name + " -l ").read()
        index = ret.find("Date and Time")
        index2 = ret.rfind("0x", 0, index)
        tag = ret[index2:index]
        print "index ", index, index2, tag

        command = "exif " + origin_file_name +  " --ifd=0 --tag=" + tag + "--set-value=" + time + " -o " + origin_file_name;
        ret = os.popen(command).read()
        print command, "returns", ret

    print time
