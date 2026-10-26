import numpy as np
import cv2
import imutils

gun_cascade = cv2.CascadeClassifier('cascade.xml')

if gun_cascade.empty():
    raise FileNotFoundError(
        "Error: cascade.xml could not be loaded. "
        "Check the file path."
    )
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Error:Could not open the camera.")

guns_detected = False

try:
    while True:
        ret, frame = camera.read()
        
        if not ret or frame is None:
            print("Error: Could not read a frame from the camera.")
            break
        
        frame = imutils.resize(frame, width=500)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        guns = gun_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.3,
            minNeighbors = 5,
            minSize = (100, 100)
        )
        
        if len(guns) > 0:
            guns_detected = True
            
        for (x, y, w, h) in guns:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )
            
            cv2.putText (
                frame,
                "Possible Gun",
                (x, y -10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0 ,255),
                2
            )
            
        cv2.imshow("Security Feed", frame)
                    
        key = cv2.waitKey(1) & 0xFF
                    
        if key == ord("q"):
            break
            
finally:
    camera.release()
    cv2.destroyAllWindows()
    
if guns_detected:
    print("A possible gun was detected during the session.")
    
else:
    print("No guns was detected during the session.")