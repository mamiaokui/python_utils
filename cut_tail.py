import subprocess
import re
from decimal import Decimal
import math
import sys
def get_video_length(path):
    process = subprocess.Popen(['ffmpeg', '-i', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    print(stdout)
    pattern_duration = re.compile("Duration:\s{1}(\d+?):(\d+?):(\d+\.\d+?),")
    pattern_size = re.compile(",\s{1}(\d{3,4})x(\d{3,4})\s{0,2}")# ",\s{1}(\d+?)x(\d+?)\s{1}\["
    matches = re.search(pattern_duration, stdout.decode('utf-8')).groups()
    print(matches)
    size = re.search(pattern_size, stdout.decode('utf-8')).groups()
    print(size)
    #matches = re.search(r"Duration:\s{1}(?P\d+?):(?P\d+?):(?P\d+\.\d+?),", stdout, re.DOTALL).groupdict()
    hours = Decimal(matches[0])
    minutes = Decimal(matches[1])
    seconds = Decimal(matches[2])
    total = 0
    total += 60 * 60 * hours
    total += 60 * minutes
    total += seconds
    width = size[0]
    height = size[1]
    return [total,width,height]

#path = "/Users/mamk/Downloads/vmate_video/a9wr2nc4qb8.mp4"

path = sys.argv[1]
print(path)
print('*'*50)
newFile = path[:-4]+'_NEW.mp4'
print(newFile)
videoInfo = get_video_length(path)
print(videoInfo)
duration = videoInfo[0]
startPoint = 0
endPoint = duration*1000 - 3000


def millisecToAssFormat(time):
    time = int(time)/1000
    hours = time / 3600
    minutes = (time - 3600 * hours) / 60
    second = time - 3600 * hours - 60 * minutes
    return "%d:%02d:%02d" % (hours, minutes, second)

def cutVideo():
    command = ['ffmpeg', '-y', '-ss', millisecToAssFormat(startPoint), '-i', path, '-acodec', 'copy', '-vcodec', 'copy', '-t', millisecToAssFormat(endPoint), newFile]
    print command
    subprocess.call(command)
cutVideo()
