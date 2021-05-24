
import face_recognition
import numpy as np
import cv2

#detect the face
cap = cv2.VideoCapture(0)
cascades = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    success, picha = cap.read()
    gray = cv2.cvtColor(picha, cv2.COLOR_BGR2RGB)
    faces = cascades.detectMultiScale(gray, scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        )
    
    ##recognize the faces eneo#
    #for (x, y, w, h) in zip (faces):
        #cv2.rectangle(picha, (x, y, w, h), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("Face Detection & Recognition", picha)
    cv2.resize(picha, (300, 400))
    cv2.imwrite('image.png', picha)
    if cv2.waitKey(10) & 0xFF == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()














#locations = face_recognition.face_locations(picha, 2)
#faces = face_recognition.face_encodings(picha, locations)