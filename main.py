import cv2
#print(cv2.__version__)

'''def image_proc():
    img = cv2.imread('img_test.jpg')
    #cv2.imshow('frame',img)
    #print(img.shape)
    w,h = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    rotated = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('rotated',rotated)
'''

def video_proc():
    cap = cv2.VideoCapture('cam_video.mp4')

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21),0)
        ret, thresh = cv2.threshold(gray, 105,255, cv2.THRESH_BINARY_INV)
        c, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(c) > 0:
            c = max(c, key=cv2.contourArea)
            x,y,w,z = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w, y+z), (0,255,0), 2)
            stroka = str(x) + "," + str(y)
            cv2.putText(frame, stroka, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, bottomLeftOrigin=False)


        cv2.imshow('frame',frame)
        cv2.waitKey(100)
if __name__ =='__main__':
    video_proc()




#cv2.waitKey(1000)
#cv2.destroyAllWindows()
