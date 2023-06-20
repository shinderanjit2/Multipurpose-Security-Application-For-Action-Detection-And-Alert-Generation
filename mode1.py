import cv2
import time
import winsound
import DirModule
import LogModule

DirModule.Dir()

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,1288)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    count = 0

    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dialated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.Beep(2000,400)

        t = time.strftime("%d-%m-%Y-%H-%M-%S")

        print("Image "+t+" Is Saved")

        file = ('Records/Mode1/Captures/'+t+'.jpg')

        cv2.imwrite(file, frame1)

        count+= 1

        LogModule.Mode1()


    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("Mode 1", frame1)
cam.release()
cv2.destroyAllWindows()
