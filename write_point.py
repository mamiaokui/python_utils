import struct
import sys

def WritePoint(srcFileName, dstKpcFileName, width, height):
    content = ""
    arr = []
    with open(srcFileName) as inf:
        content = inf.read()
        arr = content.split()

    with open(dstKpcFileName, 'wb') as of:
        for i in range(0, 5):
            a = struct.pack('I', 0)
            of.write(a)

        a = struct.pack('I', len(arr)/2)
        of.write(a)

        length = len(arr)
        #print ("len:" + str(length))
        for i in range(0, len(arr)):
            index = i
            mod = i % 8
            if mod == 4 or mod == 5:
                index = i + 2
            if mod == 6 or mod == 7:
                index = i - 2

            value = 0
            if index%2 == 0 :
                value = float(arr[index]) / width
            else :
                value = float(arr[index]) / height

            #print(value)
            a = struct.pack('f', value)
            of.write(a)
        a = struct.pack('I', 0)
        of.write(a)

# python2 WritePoint.py /Users/ali/Desktop/tmp1/test2/540_960_1.txt /Users/ali/Desktop/tmp1/test2/png2.kpc 540 960
if __name__ == '__main__':
    parameLen = len(sys.argv)
    #print("parameLen:" + str(parameLen))

    if parameLen == 5:
        srcFileName = sys.argv[1]
        dstKpcFileName = sys.argv[2]
        width = int(sys.argv[3])
        height = int(sys.argv[4])

        print("srcFileName:" + str(srcFileName))
        print("dstKpcFileName:" + str(dstKpcFileName))
        print("width:" + str(width))
        print("height:" + str(height))
    else :
        srcFileName="/Users/ali/Desktop/tmp1/test2/540_960_1.txt"
        dstKpcFileName="/Users/ali/Desktop/tmp1/test2/png2.kpc"
        width = 540
        height = 960

    WritePoint(srcFileName, dstKpcFileName, width, height)


