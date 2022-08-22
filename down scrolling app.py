import cv2
import numpy as np
import pyautogui

#use this to capture the video
#if the webcam does not open up try using 1 or 2 inside video capture
cap = cv2.VideoCapture(0) 

# color tracking range 
yellow_upper = np.array([45,255,255])
yellow_lower = np.array([22, 93, 0])

previous_y = 0

#starts the camera loop
while True:
    # returns what the camera is seeing 
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    cv2.imshow('frame', frame)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.drawContours(frame, c, -1, (0, 255, 0,), 2)
            # scrolls down the page 
            if y < previous_y:
                pyautogui.press('space')
            previous_y = y
    #stops returning what the camera is seeing if "q" is pressed
    if cv2.waitKey(10) == ord('q'):
        break

# closes camera window
cap.release()
cv2.destroyAllWindows()

