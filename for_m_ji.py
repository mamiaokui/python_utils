import sys
import collections
import math

def validate(arr):
    if len(arr) != 3:

        return False


    for i in arr:
        try:
            float(i)
        except ValueError:
            return False

    return True


def find_next_filled(index, max_value, format_point):
    for i in range(index, max_value + 1):
        value = format_point.get(i)
        if value is None or len(value) != 8:
            continue
        return i
    return -1


def convert():
    path = sys.argv[1]
    points = []
    with open(path) as f:
        lines = f.readlines()

    for line in lines:
        result = line.split()
        #print(result)
        if validate(result):
            print(result)
            points.append(map(float, result))
    max_value = -1
    for i in points:
        if i[0] > max_value:
            max_value = int(i[0])

    format_point = {}
    for i in points:
        result = format_point.get(int(i[0]))
        if result is None:
            result = []

        result.append(i[1])
        result.append(i[2])
        format_point[int(i[0])] = result

    last_filled_index = -1
    last_filled_value = None
    for i in range(max_value):
        if format_point.get(i) is None:
            if last_filled_index == -1:
                print("error code 1")
                exit(0)
            index = find_next_filled(i, max_value, format_point)
            if index == -1:
                print("error code 2")
                exit(0)
            arr = format_point.get(index)
            distance_long = index - last_filled_index
            distance_short = i - last_filled_index

            calc = []
            for j in range(8):
                temp = last_filled_value[j] + (arr[j] - last_filled_value[j]) / distance_long * distance_short
                calc.append(round(temp, 3))
            format_point[i] = calc
            last_filled_index = i
            last_filled_value = calc
        else:
            last_filled_index = i
            last_filled_value = format_point.get(i)


    od = collections.OrderedDict(sorted(format_point.items()))
    with open(sys.argv[2], "w+") as f:
        for k, v in od.iteritems():
            # for i in range (0, len(v)/2):
            #     temp = v[i]
            #     v[i] = v[i+4]
            #     v[i+4] = temp
            str_convert = ' '.join(str(e) for e in v)
            print str_convert,
            f.write(str_convert + "\n")










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
def write_point():
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


