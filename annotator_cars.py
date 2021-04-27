''' takes cars pictures from the folder, put them to the alpr site, parses response, 
    makes the xml files. For Cars, Buses, Trucks
'''
from common import *
import os
import cv2
import requests
from xml_creator import create_xml
from pprint import pprint

regions = ['ru']  # Ruissa vperde!
img_folder = "saved_cars"
xml_folder = "saved_xml"
directory = os.path.abspath(os.curdir) + '/'

if __name__ == "__main__":
    images = os.listdir(img_folder)
    print ( f"{len(images)} images in source folder, {images[:5]} ...")
    print ('current dir: ', directory)
    plt_marg = 10 # plate bbox margin, px

for short_file_name in images:
    # print(short_file_name)
    fname = directory + img_folder + '/' + short_file_name
    print(fname)

    with open(fname, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions),  # Optional
            files=dict(upload=fp),
            headers={'Authorization': 'Token a65f261760e19000dcf808dfec86d5f3de9e5f5a'})
        # pic = cv2.imread(fp)
    pprint(response.json())
    ans = response.json()
    pic = cv2.imread(fname)
    if not 'results' in ans: 
        continue

    if ans["results"] != []:
        plt_pt1 =   ans["results"][0]["box"]["xmin"]-plt_marg, \
                    ans["results"][0]["box"]["ymin"]-plt_marg
        plt_pt2 =   ans["results"][0]["box"]["xmax"]+plt_marg, \
                    ans["results"][0]["box"]["ymax"]+plt_marg
        # print(f'pt1 {pt1}')
        plate_text = ans["results"][0]["plate"].upper()
        vecl_type = ans["results"][0]["vehicle"]["type"]
        score = ans["results"][0]["score"]
        car_pt1 = ans["results"][0]["vehicle"]["box"]["xmin"], \
                ans["results"][0]["vehicle"]["box"]["ymin"]
        car_pt2 = ans["results"][0]["vehicle"]["box"]["xmax"], \
                ans["results"][0]["vehicle"]["box"]["ymax"]

        print("plate ", plate_text)
        print("type ", vecl_type)
        print("score ", score)

        full_text = plate_text + ' ' + vecl_type

        # draw car bbox
        cv2.rectangle(pic, car_pt1, car_pt2, blue, 2)
        
        # draw license plate bbox
        cv2.rectangle(pic, plt_pt1, plt_pt2, green, 2)
        cv2.putText(pic, vecl_type + " " + str(score),
                    (plt_pt1[0], plt_pt1[1]-42), cv2.FONT_HERSHEY_SIMPLEX, 0.6, blue, 2)
        cv2.putText(pic, plate_text, (plt_pt1[0], plt_pt1[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, red, 2)
        # cv2.imshow(fname, pic)
        cv2.imshow('pic', pic)
        k = cv2.waitKey(800)
        if k == 27:
            break

        # create full path to xml filename
        short_file_name_no_ext = short_file_name.replace('.jpg', '') # removes jpg extention from fname
        full_xml_fname = xml_folder + '/' + short_file_name_no_ext + '.xml'
        
        # create xml file in 
        create_xml(full_xml_fname, fname, pic.shape[0], pic.shape[1], plt_pt1, plt_pt2)
    else:
        print(f"bad picture {short_file_name}")
        continue
    
