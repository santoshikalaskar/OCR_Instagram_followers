import cv2
import numpy as np
from PIL import Image
from pytesseract import *

def fetch_user_name():
    width, height = 550, 200
    pts1 = np.float32([[69,36],[382,37],[70,70],[381,67]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOut = cv2.warpPerspective(img, matrix, (width,height))
    cv2.imshow("Account Holder Name", imgOut)
    return imgOut


def fetch_followers():
    width, height = 300, 600
    pts1 = np.float32([[102,110],[299,110],[105,688],[296,688]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOut = cv2.warpPerspective(img, matrix, (width,height))
    cv2.imshow("Account Followers Names", imgOut)
    # cv2.imshow("original", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    return imgOut

img = cv2.imread('Data/test_s3.jpg')
height, width, _ = img.shape
if (height < 2500) and (height > 2180):
    img = cv2.resize(img, (500, 760))
else:
    img = cv2.resize(img, (500, 750))

imgOut = fetch_user_name()
user_name_output_list = pytesseract.image_to_string(imgOut)
print("------------------------------------\n ")
print("Account Holder Name \n ",user_name_output_list)
print("------------------------------------\n ")
imgOut = fetch_followers()
followers_list = pytesseract.image_to_string(imgOut)
print("Account Followers Name \n ",followers_list)
print("------------------------------------\n ")
followers_list = followers_list.replace("\n \n", "\n")
followers_list = followers_list.replace("\n\n\n", "\n").replace("\n\n","\n")
print(repr(followers_list),"*************")
updated_followers_list = followers_list.splitlines()

print("Account Followers Name List \n ")
for followers in updated_followers_list[::2]:
    print(followers)