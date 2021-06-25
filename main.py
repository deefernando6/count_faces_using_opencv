import cv2

face_cascade = cv2.CascadeClassifier("<location_to_open_cv>\opencv\data\haarcascades\haarcascade_frontalface_default.xml")
img=  cv2.imread("istockphoto-1032897084-640x640.jpg")