import cv2,time
video=cv2.VideoCapture(0)
a=0

face_cascade=cv2.CascadeClassifier("face.xml")
while True:
      a=a+1
      check, frame=video.read()
      print(check)
      print(frame)

      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      
      faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=1)
      for x,y,w,h in faces:
            img=cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),3)
            
      print("co-ordinates of face")
      print(faces)
      cv2.imshow("CAPTURING",gray)
      key=cv2.waitKey(1)

      if key==ord("q"):
            break
print(a)

video.release()
cv2.destroyAllWindows
