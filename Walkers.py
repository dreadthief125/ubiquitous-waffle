import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    peds=face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in peds:
      cv2.prectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
