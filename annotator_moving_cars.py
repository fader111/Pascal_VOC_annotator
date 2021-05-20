''' takes cars pictures from the folder, defines moving cars, get the bboxes of them, put to the 
    the xml files. For one type of vehicle only
'''
from common import *
import os
import cv2
import requests
from motion_detect_probe import *
from xml_creator import create_xml
from pprint import pprint

regions = ['ru']  # Ruissa vperde!
img_folder = "saved_cars2"
xml_folder = "saved_xml2"
directory = os.path.abspath(os.curdir) + '/'
short_file_name_no_ext = 0

saved_jpg_width, saved_jpg_height = 1024, 768

if __name__ == "__main__":
    _gen = bboxes_from_frame()
    while 1:
        # get pictures and annotator
        pic, bboxes = next(_gen)        
        full_xml_fname = xml_folder + '/' + \
            str(short_file_name_no_ext) + '.xml'
        jpg_fname = directory + img_folder + '/' + \
            str(short_file_name_no_ext + 1) + ".jpg"

        # save pic to folder
        # pic = cv2.resize(pic, (saved_jpg_width, saved_jpg_height))
        cv2.imwrite(jpg_fname, pic)
        
        xml_content = create_xml(full_xml_fname, jpg_fname, pic.shape[0], pic.shape[1], bboxes)
        # saving xml file
        with open(full_xml_fname, 'w') as f:
            f.write(xml_content)
        
        short_file_name_no_ext += 1