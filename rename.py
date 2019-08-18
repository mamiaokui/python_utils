import os
import sys

def rename(file, suffix):
    print(file, suffix)
    list = os.popen("ls " + file).read().split()

    for file in list:
        segment = file.split(".")
        new_file_name = segment[0] + "." + suffix
        if sys.argv[2] == segment[1]:
            continue
        command = "ffmpeg -y -i %s %s" % (file, new_file_name)
        print(file)
        print(segment)
        print(sys.argv[2])
        print(command)
        os.system(command)

def main():
    for file in sys.argv[1:-1]:
        rename(file, sys.argv[-1])
if __name__ == "__main__":
    main()