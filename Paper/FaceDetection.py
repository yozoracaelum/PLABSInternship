import cv2

face_cascade = cv2.CascadeClassifier(r'D:\G\UNPAD\Internship\Paper\xmlClassifiers\haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(r'D:\G\UNPAD\Internship\Paper\xmlClassifiers\haarcascade_eye.xml')  

cap = cv2.VideoCapture(0)

while True:  
    ret, img = cap.read()  
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray_img, 1.25, 4) 
  
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        rec_gray = gray_img[y:y+h, x:x+w] 
        rec_color = img[y:y+h, x:x+w] 
  
        eyes = eye_cascade.detectMultiScale(rec_gray)  
  
        for (x,y,w,h) in eyes: 
            cv2.rectangle(rec_color,(x,y),(x+w,y+h),(0,127,255),2) 
  
    cv2.imshow('Face Detection',img) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cap.release() 
cv2.destroyAllWindows()

