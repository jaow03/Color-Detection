import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    _, frame= cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height,width,_ = frame.shape
    
    cx = int(width/2)
    cy = int(height/2)
    
    pixel_center = hsv_frame[cy,cx]
    hue_value = pixel_center[0]
    
    color = "Undefined"
    color = "#FF0000"
    if hue_value < 5:
        #color = "RED"
        color = 30
    
    elif hue_value < 22:
        #color = "ORANRE"
        color = 60
    elif hue_value < 33:
        #color = "YELLOW"
        color = 90
        
    elif hue_value < 78:
        #color = "GREEN"
        color = 120
    elif hue_value < 131:
        #color = "BLUE"
        color = 150
    
    elif hue_value < 170:
        #color = "VIOLET"
        color = 180
    
    else:
        #color = "RED"
        color = 210
    
    # colors = "FF0000"
    # font = cv2.FONT_HERSHEY_SIMPLEX
    
    # pixel_center_bgr = frame[cy,cx]
    # cv2.putText(frame, colors,(10,50),0,1,pixel_center_bgr,2)
  
    # cv2.circle(frame,(cy,cx),5,(255,0,0),3)

        
    # Window name in which image is displayed
    window_name = 'Image'
    
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # org
    org = (50, 50)
    
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.putTe
    # xt() method
    image = cv2.putText(frame, 'OpenCV', org, font,fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == 27 :
        break
    
cap.release()
cv2.destroyAllWindows()
