from tkinter.tix import Form
import cv2
import numpy as np

image = cv2.imread("color.png")

lowoer = np.array([0,0,0])
upper = np.array([0,0,0])
#color0 = ("BLACK")    

lowoer_0 = np.array([0,0,0])
upper_0 = np.array([0,0,100])
#color0 = ("BLACK")    

lowoer1 = np.array([0,0,0])
upper1 = np.array([255,255,255])
#color1 = ("WHITE") 
         
lowoer2 = np.array([100,0,0])
upper2 = np.array([159,255,255])
#color2 = ("ORANRE")
            
lowoer3 = np.array([22,0,0])
upper3 = np.array([38,255,255])
#color3 = ("YELLOW")
        
lowoer4 = np.array([38,0,0])
upper4 = np.array([100,255,255])
#color4 = ("GREEN")

lowoer5 = np.array([90,0,0])
upper5 = np.array([100,255,255])
#color5 = ("LIGKT BLUE")

lowoer6 = np.array([102,0,0])
upper6 = np.array([126,255,255])
#color6= ("BLUE")
  
lowoer7 = np.array([127,0,0])
upper7 = np.array([160,255,255])
#color7 = ("VIOLET")

lowoer8 = np.array([160,0,0])
upper8 = np.array([179,255,255])
#color8 = ("RED")
           
List_color =[(lowoer,upper),
             (lowoer1,upper1),
             (lowoer2,upper2),
             (lowoer3,upper3),
             (lowoer4,upper4),
             (lowoer5,upper5),
             (lowoer6,upper6),
             (lowoer7,upper7),]

List_colorname = ["BLACK",
                  "WHITE",
                  "ORANRE",
                  "YELLOW",
                  "GREEN",
                  "BLUE",
                  "VIOLET",
                  "RED"]

hsv_frame = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
                    
#detect = cv2.inRange(hsv_frame,lowoer,upper)   
#detect1 = cv2.inRange(hsv_frame,lowoer1,upper1) 
detect2 = cv2.inRange(hsv_frame,lowoer2,upper2)
detect3 = cv2.inRange(hsv_frame,lowoer3,upper3)  
#detect4 = cv2.inRange(hsv_frame,lowoer4,upper4) 
#detect5 = cv2.inRange(hsv_frame,lowoer5,upper5)  
#detect6 = cv2.inRange(hsv_frame,lowoer6,upper6)  
#detect7 = cv2.inRange(hsv_frame,lowoer7,upper7) 
detect8 = cv2.inRange(hsv_frame,lowoer8,upper8)


cv2.imshow("Frame",image)
cv2.imshow("hsv_frame",hsv_frame)
#cv2.imshow("Dtect BLACK",detect)
#cv2.imshow("Dtect WHITE",detect1)
cv2.imshow("Dtect ORANRE",detect2)
cv2.imshow("Dtect YELLOW",detect3)
#cv2.imshow("Dtect GREEN",detect4)
#cv2.imshow("Dtect LIGKT BLUE",detect5)
#cv2.imshow("Dtect BLUE",detect6)
#cv2.imshow("Dtect VIOLET",detect7)
cv2.imshow("Dtect RED",detect8)
 





cv2.waitKey(0)

cv2.destroyAllWindows()
