import cv2
import time
import winsound

import DirModule
import LogModule

DirModule.Dir()

net=cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolov4-tiny.cfg")
model=cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320,320), scale=1/255)

classes=[]

with open("dnn_model/classes.txt","r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
        #print(classes)

cap=cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1288)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        
while True:
    ret, frame=cap.read()

    (class_ids, scores, bboxes) = model.detect(frame)

    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x,y,w,h) = bbox

        class_name = classes[class_id]

        if(class_name == 'person'):
            cv2.putText(frame, str(class_name), (x, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
            cv2.rectangle(frame,(x,y), (x+w, y+h), (200, 0, 50), 3)

            winsound.Beep(2000,200)

            t = time.strftime("%d-%m-%Y-%H-%M-%S")
            print("Image "+t+" Is Saved")
            LogModule.Mode2()
            file = ('Records/Mode2/Captures/'+t+'.jpg')
            cv2.imwrite(file, frame)

            
    cv2.imshow("Mode 2",frame)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
