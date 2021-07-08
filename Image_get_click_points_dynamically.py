import cv2
import numpy as np
from PIL import Image
from pytesseract import *

circles = np.zeros((4,2), np.int)
counter =0

def mousePoints(event, x,y, flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] =x,y
        counter = counter +1
        print(circles)

img = cv2.imread('Data/test.jpeg')
print("original shape:", img.shape)

img = cv2.resize(img, (500, 700))

while True:
    if counter == 4:
        width, height = 300, 600
        pts1 = np.float32([circles[0],circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOut = cv2.warpPerspective(img, matrix, (width,height))
        cv2.imwrite("user_name_output.jpeg", imgOut)
        cv2.imshow("output", imgOut)


    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]), 3, (0,255,0), cv2.FILLED)

    cv2.imshow("original", img)
    cv2.setMouseCallback("original", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

image_file = 'user_name_output.jpeg'
followers_list = pytesseract.image_to_string(Image.open(image_file))
print(followers_list)