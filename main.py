import cv2

face_cascade = cv2.CascadeClassifier("<location_to_open_cv>\opencv\data\haarcascades\haarcascade_frontalface_default.xml")
img=  cv2.imread("istockphoto-1032897084-640x640.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,3)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
	
cv2.rectangle(img,(0,0),(300,40),(255,255,255),-1)
cv2.putText(img,"Number of faces detected"+str(faces.shape[0]),(0,25),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0),1)

cv2.imshow("Counting faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()