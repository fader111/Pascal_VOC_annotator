''' takes video, space - stop/ next frame, с - continue, m - save frame
'''
import cv2
import os
folder_name = "C:/Users/Anton/Downloads/ach_picts/"
video_src = "../../Videos/tula11.mp4"
img_list = os.listdir(folder_name)
img = None

def make_screenshot(img, fname, path_='pictures/', res_w = 1024, res_h = 768):
    """ resize img and save """
    full_path = path_+fname
    img = cv2.resize(img, (res_w, res_h))
    cv2.imwrite(full_path, img)

for file_ in {}:#img_list:
    full_name = folder_name + file_ 
    img = cv2.imread(folder_name + file_)
    cv2.imshow("img", img)
    key = cv2.waitKey()
    if key == 27:
        break

arg_key = 1
cap = cv2.VideoCapture(video_src)
frm_num = 0

while True:
    _, img = cap.read()
    show_img = cv2.resize(img, (1024,768))
    cv2.imshow("img", show_img)
    key = cv2.waitKey(arg_key)
    # if ESC - go out
    if key == 27:
        break
    # с - continue video
    elif key == ord("c"):
        arg_key = 1
    elif key == ord("с"): # ruussian "с" doesn't work
        arg_key = 1
    # SPACE - stop /next frame
    elif key == 32:
        arg_key = 0
    # m - make screenshot
    elif key == ord("m"):
        fname = f"{frm_num}.jpg"
        frm_num +=1
        make_screenshot(img, fname)