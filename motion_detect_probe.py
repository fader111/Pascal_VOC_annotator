import cv2
import numpy as np
import time

# src ="C:/Users/Anton/Videos/snowy5.ts"
# src = "C:/Users/Anton/Videos/U524802_1_400_0.avi"


def bboxes_from_video(src):
    ''' define moving objects and return bboxes of them 
        bbox format = [x, y, w, h]
    '''
    cap = cv2.VideoCapture(src)
    # frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
    # fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    # out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    frame1 = cv2.resize(frame1, (1080,720))
    frame2 = cv2.resize(frame2, (1080,720))

    print(frame1.shape)
    spend =""
    while cap.isOpened():
        ts = time.time()
        bboxes = []
        out_pic = frame2.copy()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=5)
        # contours, cont_sec = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS ) # only external contours
        
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 1000:
                continue
            bboxes.append((x, y, w, h))
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
            cv2.putText(frame1, str(spend)+" ms", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255,0),2)
        #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        # image = cv2.resize(frame1, (1280,720))
        #out.write(image)
        cv2.imshow("feed", frame1)
        # cv2.imshow("thresh", thresh)
        # cv2.imshow('dilated', dilated)
        # cv2.imshow('contours', cont_sec)
        # print ('cont_sec',contours)
        frame1 = frame2
        spend = round((time.time()-ts)*1000, 1)
        # print (spend)
        ret, frame2 = cap.read()
        frame2 = cv2.resize(frame2, (1080,720))
        if not ret:
            print('End of file')
            cap.release()
            break
        #print (time.time()-ts)
        if cv2.waitKey(1) == 27:
            cap.release()
            break
        yield (frame2, bboxes)

if __name__ == "__main__":
    bboxes_from_frame()
    cv2.destroyAllWindows()
    # out.release()