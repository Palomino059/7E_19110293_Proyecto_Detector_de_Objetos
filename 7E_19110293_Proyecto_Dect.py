import cv2

cap = cv2.VideoCapture(0)
GloboTer = cv2.CascadeClassifier('cascade.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

   ret,frame = cap.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   toy = GloboTer.detectMultiScale(gray,1.3,3,2)

   for(x,y,w,h) in toy:
      pt1 = (x,y)
      pt2 = (x+w,y+h)
       
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255.0),2)
      cv2.rectangle(frame,(x,y),(x+100,y+40),(0,255.0),-1)
      cv2.putText(frame,'Globo Terraquio',(x+10,y+30),font,0.7,(255,255,255),2) 

   cv2.imshow('frame',frame) 

   if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
