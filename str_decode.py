import sys
import codecs
if __name__ == "__main__":
    file_path = sys.argv[1]
    f = codecs.open(file_path, encoding='utf-8')
    file_content = f.read()
    file_content = list(file_content)
    str = ""
    for i in range(len(file_content)):
        char = file_content[i]
        print chr((ord(char) - 21)//3)
    #print file_content
    #f = open("abc.txt", 'w')
    #f.write(str)
    #f.close()

