''' takes video, space - stop/ next frame, с - continue, m - save frame
'''
import cv2
import os
# video_src = "../../Videos/tula11.mp4"
video_src = "../../Videos/tula12n.mp4"
start_frm_num = 0
# img = None

def make_screenshot(img, fname, path_='pictures/', res_w = 1024, res_h = 768):
    """ resize img and save """
    full_path = path_+fname
    img = cv2.resize(img, (res_w, res_h))
    cv2.imwrite(full_path, img)

arg_key = 1 # for cv2.waitKey(arg_key)
cap = cv2.VideoCapture(video_src)
frm_num = start_frm_num

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
    elif key == ord("с"): # ruussian "с" doesn't work dont know why
        arg_key = 1
    # SPACE - stop /next frame
    elif key == 32:
        arg_key = 0
    # m - make screenshot
    elif key == ord("m"):
        fname = f"{frm_num}.jpg"
        frm_num +=1
        make_screenshot(img, fname)
