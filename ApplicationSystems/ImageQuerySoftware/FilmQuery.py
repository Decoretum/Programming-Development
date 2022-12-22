import os
import sys
import subprocess
import exiftool
from PIL import Image
from PIL.ExifTags import TAGS
from iptcinfo3 import IPTCInfo

file = "p115_maynila.tif"

with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(file)
    for data in metadata:
        print(data['IPTC:Keywords'])
 

