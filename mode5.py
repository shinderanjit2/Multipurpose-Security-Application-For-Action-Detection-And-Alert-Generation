import cv2
import time
import DirModule
import LogModule

DirModule.Dir()
LogModule.Mode5()

video = cv2.VideoCapture(0)

video.set(cv2.CAP_PROP_FRAME_WIDTH,1288)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

if (video.isOpened() == False):
	print("Error Reading Video File")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

t = time.strftime("%d-%m-%Y-%H-%M-%S")
t1 = time.strftime("%d/%m/%Y")

result = cv2.VideoWriter('Records/Mode5/Captures/'+t+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, size)
	
while(True):
	ret, frame = video.read()

	cv2.putText(frame, t1, (30, 68), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

	if ret == True:

	    result.write(frame)

	    cv2.imshow('Mode 5', frame)

	    if cv2.waitKey(1) & 0xFF == ord('q'):
    		break

	else:
		break

video.release()
result.release()
	
cv2.destroyAllWindows()

print("The Video Was Successfully Saved")
