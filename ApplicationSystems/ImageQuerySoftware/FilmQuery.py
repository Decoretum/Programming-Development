import os
import shutil
import sys
from exiftool import ExifToolHelper
from PIL import Image
from PIL.ExifTags import TAGS
from iptcinfo3 import IPTCInfo

os.chdir('../../../')
curr = os.getcwd()
filename = "p115_maynila.tif"
file = sys.path[0] + "/{}".format(filename)
film = curr + "/Films"


artist = ''
year = ''
title = ''

with ExifToolHelper() as et:
    metadata = et.get_metadata(file)
    for data in metadata:
        #print("{:20.20}".format(data[  'IPTC:Keywords']))
        title = data['IPTC:Keywords'][0]
        year = data['IPTC:Keywords'][1]
        artist = data['IPTC:Keywords'][2]


yearpath = curr + "/Films/{}".format(year)
artistpath = curr + "/Films/{}/{}".format(year,artist)

if not os.path.exists(film):
    os.makedirs(film)
    print("Film directory created")

if not os.path.exists(yearpath):
    os.makedirs(yearpath)
    print("Year path created")

if not os.path.exists(artistpath):
    os.makedirs(artistpath)
    print("Artist path created")

destpath =  artistpath + "/{}".format(filename)
shutil.move(file,destpath)
print(destpath)


