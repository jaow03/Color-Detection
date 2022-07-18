import cv2
import numpy as np
image = cv2.imread("car.png")

hsv_frame = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
lowoer1 = np.array([160,0,0])
upper1 = np.array([179,255,255])
color = "RED"
        
lowoer2 = np.array([0,0,0])
upper2 = np.array([22,255,255])
color = "ORANRE"
            
lowoer3 = np.array([22,0,0])
upper3 = np.array([38,255,255])
color = "YELLOW"
        
lowoer4 = np.array([38,0,0])
upper4 = np.array([100,255,255])
color = "GREEN"

lowoer5 = np.array([100,0,0])
upper5 = np.array([130,255,255])
color = "BLUE"
  
lowoer6 = np.array([130,0,0])
upper6 = np.array([160,255,255])
color = "VIOLET"
           
lowoer7 = np.array([0,0,0])
upper7 = np.array([0,255,255])
color = "BLACK"
    
    
detect1 = cv2.inRange(hsv_frame,lowoer1,upper1)
detect2 = cv2.inRange(hsv_frame,lowoer2,upper2)   
detect3 = cv2.inRange(hsv_frame,lowoer3,upper3)   
detect4 = cv2.inRange(hsv_frame,lowoer4,upper4)   
detect5 = cv2.inRange(hsv_frame,lowoer5,upper5)   
detect6 = cv2.inRange(hsv_frame,lowoer6,upper6)   
detect7 = cv2.inRange(hsv_frame,lowoer7,upper7)      
    
cv2.imshow("Frame",image)

cv2.imshow("Dtect RED",detect1)
cv2.imshow("Dtect ORANRE",detect2)
cv2.imshow("Dtect YELLOW",detect3)
cv2.imshow("Dtect GREEN",detect4)
cv2.imshow("Dtect BLUE",detect5)
cv2.imshow("Dtect VIOLET",detect6)
cv2.imshow("Dtect BLACK",detect7)   

cv2.waitKey(0)

cv2.destroyAllWindows()
