import cv2
import time
import numpy as np
import winsound

import DirModule
import LogModule

DirModule.Dir()

cam=cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,720)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

p1=0
q1=0

def Call(p,q):
    #print(p,q)
    global p1
    global q1
    p1=p
    q1=q

_,prev=cam.read()
prev=cv2.flip(prev,1)
_,new=cam.read()
new=cv2.flip(new,1)

while True:
    diff=cv2.absdiff(prev,new)
    diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    diff=cv2.blur(diff,(5,5))
    _,thresh=cv2.threshold(diff,10,255,cv2.THRESH_BINARY)
    thresh=cv2.dilate(thresh,None,3)
    thresh=cv2.erode(thresh,np.ones((4,4)),1)
    dialated = cv2.dilate(thresh, None, iterations=3)
    contor,_=cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.circle(prev,(p1,q1),5,(0,0,255),-1)    
    
    for contors in contor:
        
        if cv2.contourArea(contors)>5000:
            (x,y,w,h)=cv2.boundingRect(contors)
            (x1,y1),red=cv2.minEnclosingCircle(contors)

            x1=int(x1)
            y1=int(y1)
            
            cv2.line(prev,(p1,q1),(x1,y1),(255,0,0),2)
            t=cv2.putText(prev,"{}".format(int(np.sqrt((x1-p1)**2+(y1-q1)**2))),(20,150),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255))
            cv2.rectangle(prev,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(prev,(x1,y1),5,(0,0,255),-1)
            
            # print(format(int(np.sqrt((x1-20)**2+(y1-200)**2))))

            if(int(np.sqrt((x1-p1)**2+(y1-q1)**2))<=q1):
                winsound.Beep(2000,200)

                #print(p1,q1)
                
                t = time.strftime("%d-%m-%Y-%H-%M-%S")
                print("Image "+t+" Is Saved")
                LogModule.Mode3()
                file = ('Records/Mode3/Captures/'+t+'.jpg')
                cv2.imwrite(file, prev)
                
    cv2.imshow("Mode3",prev)
    def click_button(event,p,q,flags,parents):
        if event==cv2.EVENT_LBUTTONDOWN:
            #print(x,y)
            Call(p,q)

    # cv2.namedWindow("orig")
    cv2.setMouseCallback("Mode3",click_button)

    prev=new
    _,new=cam.read()

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
