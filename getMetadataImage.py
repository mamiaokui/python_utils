import os
import base64
import json


def main(args):
    if len(args) < 2:
        print "pls input video file name!"
        return 1

    downFn = args[1]

    parserCmd = 'mediainfo ' + downFn + ' | grep "Description" | awk -F ": " \'{print $2}\' '
    # print parserCmd

    videoDesc = os.popen(parserCmd).read()
    a = 1
    if a == 1:
        videoDesc = base64.b64decode( videoDesc.replace(' / ', '') )
    else :
        videoDesc = base64.b64decode(videoDesc)

    print 'desc', videoDesc
    try:
        desc = json.loads(videoDesc)
    except:
        print downFn + ',json error!'
    else:
        if desc.get('base') and desc['base'].get('brand-model-api'):
            modelInfo = desc['base']['brand-model-api']
            pos_f = modelInfo.find('-')
            pos_l = modelInfo.find('-', -1)
            brand = modelInfo[:pos_f]
            api = modelInfo[pos_l - 1:]
            model = modelInfo[pos_f + 1:pos_l - 2]
            print downFn + ',' + brand + ',' + model + ',' + api
        else:
            print downFn + ',json empty!'

        if desc.get('detect') and desc['detect'].get('hand-data'):
            image = desc['detect'].get('hand-data')
            #image = base64.b64decode(image.replace('/', ''))
            #image = base64.b64decode(image)
            value = [ord(ele) for ele in image]
            print image, value

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
