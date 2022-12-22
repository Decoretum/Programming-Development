import os
import sys
from exiftool import ExifToolHelper


filename = "24.jpg"
file = sys.path[0] + "/{}".format(filename)

with ExifToolHelper() as et:
    metadata = et.get_metadata(file)
    for data in metadata:
        print(data['IPTC:Keywords'][0])
        '''print(data['IPTC:Keywords'][0])
        print(data['IPTC:Keywords'][1])'''
        '''title = data['IPTC:Keywords'][0]
        year = data['IPTC:Keywords'][1]
        artist = data['IPTC:Keywords'][2]'''