import cv2

face_cascade = cv2.CascadeClassifier("<location_to_open_cv>\opencv\data\haarcascades\haarcascade_frontalface_default.xml")
img=  cv2.imread("istockphoto-1032897084-640x640.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,3)