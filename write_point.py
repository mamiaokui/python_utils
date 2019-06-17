import struct

content = ""
arr = []
base = 480
with open("/tmp/log.txt") as inf:
    content = inf.read()
    arr = content.split()

with open("/tmp/a.kpc", 'wb') as of:
    for i in range(0, 5):
        a = struct.pack('I', 0)
        of.write(a)


    a = struct.pack('I', len(arr)/2)
    of.write(a)
    for i in range(0, len(arr)):
        index = i
        mod = i % 8
        if mod == 4 or mod == 5:
            index = i + 2
        if mod == 6 or mod == 7:
            index = i - 2
        value = float(arr[index])/base
        print(value)
        a = struct.pack('f', value)
        of.write(a)
    a = struct.pack('I', 0)
    of.write(a)
