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


if __name__ == "__main__":
    path = sys.argv[1]
    points = []
    with open(path) as f:
        lines = f.readlines()

    for line in lines:
        result = line.split()
        print(result)
        if validate(result):
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
            for i in range (0, len(v)/2):
                temp = v[i]
                v[i] = v[i+4]
                v[i+4] = temp
            str_convert = ' '.join(str(e) for e in v)
            print str_convert
            f.write(str_convert + "\n")








