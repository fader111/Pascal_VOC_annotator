""" if some xml file has no cars, it deletes, corresponding pic file deletes also
"""

from common import *
import os
import cv2
import requests
from motion_detect_probe import *
from xml_creator import create_xml
from pprint import pprint

img_folder = "saved_cars2"
xml_folder = "saved_xml2"
directory = os.path.abspath(os.curdir) + '/'

DO_REMOVE = True

img_names = os.listdir(directory + img_folder)
xml_names = os.listdir(directory + xml_folder)
print(f"{len(img_names)} files in img folder ")
print(f"{len(xml_names)} files in xml folder ")

# list of files to remove, names without extentions [1, 34, 55, ]
raw_names_to_remove = []

for xml_file in xml_names:
    # считываем файл
    full_path_xml = directory + xml_folder + "/" + xml_file
    with open(full_path_xml, 'r') as f:
        # if no annotation in xml file, put its name to the list to remove
        cont = f.read()
        if not "object" in cont:
            raw_fname = xml_file.split('.')[0]
            raw_names_to_remove.append(raw_fname)

print(
    f"{len(raw_names_to_remove)} files in list to delete - {raw_names_to_remove[:3]} ...")

# delete files according to the names in list
for raw_fname in raw_names_to_remove:
    full_img_fname = directory + img_folder + '/' + raw_fname + '.jpg'
    full_xml_fname = directory + xml_folder + '/' + raw_fname + '.xml'
    if DO_REMOVE:
        os.remove(full_img_fname)
        os.remove(full_xml_fname)

img_names = os.listdir(directory + img_folder)
xml_names = os.listdir(directory + xml_folder)
print(f"{len(img_names)} files in img folder after deleting")
print(f"{len(xml_names)} files in xml folder after deleting")
