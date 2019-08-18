import sys
import os
file_name_before = sys.argv[1]
file_name_after = file_name_before.replace("ogg", "mp3")

command = "ffmpeg -i \"%s\" \"%s\"" % (file_name_before, file_name_after)
os.system(command)
