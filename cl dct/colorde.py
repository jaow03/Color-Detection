import cv2 
import numpy as np

#การนำรูปภาพเข้ามา
image = cv2.imread("color.png")

#การแปลงรูปจากRGBเป็นHSV
hsv = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)

#ค่าตำสุดของสี
lowoer = np.array([0,0,0])
#ต่าสูงสูดของสี
upper = np.array([30,255,255])

#ตรวจสอบค่าแปลงภาพ
detect = cv2.inRange(hsv,lowoer,upper)

cv2.imshow("image",image)
cv2.imshow("Detected Result",detect)

cv2.waitKey(0)

cv2.destroyAllWindows()