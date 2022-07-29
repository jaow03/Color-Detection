import numpy as np 
import cv2 


# Capturing video through image 
image = cv2.imread('car6.png')
image = cv2.resize(image, (1000, 700))
rate_area = 1000

Color_Detect = []
Color_Num = {}

d = []
v = []

# Start a while loop 
# ret, image = image.read() 

SHV_Frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

# สีแดง --
red_lower = np.array([136, 87, 111], np.uint8) 
red_upper = np.array([180, 255, 255], np.uint8) 
red_mask = cv2.inRange(SHV_Frame, red_lower, red_upper)
# สีน้ำเงิน --
blue_lower = np.array([150, 52, 72], np.uint8) 
blue_upper = np.array([190, 255, 255], np.uint8) 
blue_mask = cv2.inRange(SHV_Frame, blue_lower, blue_upper) 
# สีเหลือง --
yellow_lower = np.array([30,52,176], np.uint8)
yellow_upper = np.array([49,255,255], np.uint8)
yellow_mask = cv2.inRange(SHV_Frame, yellow_lower, yellow_upper)
# สีขาว
white_lower = np.array([255,0,227], np.uint8)
white_upper = np.array([0,0,255], np.uint8)
white_mask = cv2.inRange(SHV_Frame, white_lower, white_upper)
# สีดำ       
black_lower = np.array([0,0,0], np.uint8)
black_upper = np.array([0,255,33], np.uint8)
black_mask = cv2.inRange(SHV_Frame, black_lower, black_upper)
# สีม่วง
violet_lower= np.array([191, 52, 72], np.uint8)
violet_upper = np.array([205,255,255], np.uint8)
violet_mask = cv2.inRange(SHV_Frame, violet_lower, violet_upper)
# สีเขียว --
green_lower = np.array([50, 52, 72], np.uint8) 
green_upper = np.array([110, 255, 255], np.uint8) 
green_mask = cv2.inRange(SHV_Frame, green_lower, green_upper) 
# สีส้ม --
orange_lower = np.array([15,52,176], np.uint8)
orange_upper = np.array([29,255,255], np.uint8)
orange_mask = cv2.inRange(SHV_Frame, orange_lower, orange_upper)
# สีน้ำตาล
brown_lower = np.array([24,255,255], np.uint8)
brown_upper = np.array([35,255,151], np.uint8)
brown_mask = cv2.inRange(SHV_Frame, brown_lower, brown_upper)
# สีชมพู
pink_lower = np.array([206,52, 72], np.uint8)
pimk_upper = np.array([231,255,255], np.uint8)
pink_mask = cv2.inRange(SHV_Frame, pink_lower, pimk_upper)
# สีเทา
gray_lower = np.array([0,0,226], np.uint8)
gray_upper = np.array([255,255,107], np.uint8)
gray_mask = cv2.inRange(SHV_Frame, gray_lower, gray_upper)
# สีฟ้า
light_blue_lower = np.array([111, 52, 72], np.uint8) 
light_blue_upper = np.array([149, 255, 255], np.uint8)
light_blue_mask = cv2.inRange(SHV_Frame, light_blue_lower, light_blue_upper) 


# Morphological Transform, Dilation 
# for each color and bitwise_and operator 
# between SHV_Frame and mask determines 
# to detect only that particular color 
kernal = np.ones((5, 5), "uint8") 


# แปลงค่าสำหรับสีแดง 
# res_red = cv2.bitwise_and(SHV_Frame, image, mask = red_mask)
# Creating contour to track red color 
contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area):
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
		
		# cv2.putText(image, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
		print("Red Colour")
		Color_Detect.append("Red Colour")


# แปลงค่าสำหรับสีส้ม
orange_mask = cv2.dilate(orange_mask, kernal) 
# res_orange = cv2.bitwise_and(SHV_Frame, image, mask = orange_mask)
# Creating contour to track Orange Colour
contours, hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > rate_area):
        x, y, w, h = cv2.boundingRect(contour)
        SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 128, 0), 2)
        
        # cv2.putText(image, "Orange Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 128, 0))
        print("Orange Colour")
        Color_Detect.append("Orange Colour")
        



# แปลงค่าสำหรับสีเหลือง
yellow_mask = cv2.dilate(yellow_mask, kernal) 
# res_yellow = cv2.bitwise_and(SHV_Frame, image, mask = yellow_mask) 
# Creating contour to track Yellow Colour
contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (49,255,255), 2) 
		
		# cv2.putText(image, "Yellow Colour", (x, y), 1.0, (49,255,255))
		print("Yellow Colour")
		Color_Detect.append("Yellow Colour")


# แปลงค่าสำหรับสีเขียว
green_mask = cv2.dilate(green_mask, kernal) 
# res_green = cv2.bitwise_and(SHV_Frame, image, mask = green_mask) 
# Creating contour to track Green Colour
contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
		
		# cv2.putText(image, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
		print("Green Colour")
		Color_Detect.append("Green Colour")


# แปลงค่าสำหรับสีฟ้า
blue_mask = cv2.dilate(blue_mask, kernal) 
# res_blue = cv2.bitwise_and(SHV_Frame, image, mask = blue_mask)
# Creating contour to track Blue Colour
contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) 
		
		# cv2.putText(image, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
		print("Blue Colors")
		Color_Detect.append("Blue Colour")


# แปลงค่าสำหรับสีม่วง
violet_mask = cv2.dilate(violet_mask, kernal) 
# res_violet = cv2.bitwise_and(SHV_Frame, image, mask = violet_mask)
# Creating contour to track Violet Colour
contours, hierarchy = cv2.findContours(violet_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (204,102,255), 2) 
		
		# cv2.putText(image, "Violet Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (204,102,255))
		print("Violet Colour")
		Color_Detect.append("Violet Colour")


# แปลงค่าสำหรับสีดำ
black_mask = cv2.dilate(black_mask, kernal) 
# res_black = cv2.bitwise_and(SHV_Frame, image, mask = black_mask)
# Creating contour to track Black Colour
contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
		
		# cv2.putText(image, "Black Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
		print("Black Colour")
		Color_Detect.append("Black Colour")


# แปลงค่าสำหรับสีขาว
white_mask = cv2.dilate(white_mask, kernal) 
# res_white = cv2.bitwise_and(SHV_Frame, image, mask = white_mask)
# Creating contour to track White Colour
contours, hierarchy = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2) 
		
		# cv2.putText(image, "White Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
		print("White Colour")
		Color_Detect.append("White Colour")


# แปลงค่าสำหรับสีเทา
gray_mask = cv2.dilate(gray_mask, kernal) 
# res_gray = cv2.bitwise_and(SHV_Frame, image, mask = gray_mask)
# Creating contour to track Gray Colour
contours, hierarchy = cv2.findContours(gray_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
		
		# cv2.putText(image, "Gray Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
		print("Gray Colour")
		Color_Detect.append("Gray Colour")


# แปลงค่าสำหรับสีชมพู
pink_mask = cv2.dilate(pink_mask, kernal) 
# res_pink = cv2.bitwise_and(SHV_Frame, image, mask = pink_mask)
# Creating contour to track Pink Colour
contours, hierarchy = cv2.findContours(pink_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
		
		# cv2.putText(image, "Pink Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
		print("Pink Colour")
		Color_Detect.append("Pink Colour")
 

# แปลงค่าสำหรับสีน้ำตาล
brown_mask = cv2.dilate(brown_mask, kernal) 
# res_brown = cv2.bitwise_and(SHV_Frame, image, mask = brown_mask)
# Creating contour to track Brown Colour
contours, hierarchy = cv2.findContours(brown_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
		
		# cv2.putText(image, "Brown Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
		print("Brown Colour")
		Color_Detect.append("Brown Colour")
 

# แปลงค่าสำหรับสีฟ้า
light_blue_mask = cv2.dilate(light_blue_mask, kernal) 
# res_light_blue = cv2.bitwise_and(SHV_Frame, image, mask = light_blue_mask)
# Creating contour to track Light Blue Colour
contours, hierarchy = cv2.findContours(light_blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate(contours): 
	area = cv2.contourArea(contour) 
	if(area > rate_area): 
		x, y, w, h = cv2.boundingRect(contour) 
		SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (149, 255, 255), 2) 
		
		# cv2.putText(image, "Light Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (149, 255, 255))
		print("Light Blue Colour")
		Color_Detect.append("Light Blue Colour")


for x in Color_Detect:
    if x in Color_Num:
        Color_Num[x] += 1
    else:
        Color_Num[x] = 1
        


def myFunc(e):
	return e[1]

Color_Car = [(k, v) for k, v in Color_Num.items()]

Color_Car.sort(key=myFunc, reverse=True)
print(Color_Car[0])
# print(v)
# print(d)
# Program Termination 
cv2.imshow("Multiple Color Detection in Real-TIme", image)

# if cv2.waitKey(10) & 0xFF == ord('q'): 
# cap.release() 
# cv2.destroyAllWindows() 
cv2.waitKey(0)
cv2.destroyAllWindows()
