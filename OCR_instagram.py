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
    cv2.imwrite("user_name_output.jpeg", imgOut)
    cv2.imshow("Account Holder Name", imgOut)


def fetch_followers():
    width, height = 300, 600
    pts1 = np.float32([[102,114],[299,114],[105,676],[296,673]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOut = cv2.warpPerspective(img, matrix, (width,height))
    cv2.imwrite("followers_output.jpeg", imgOut)
    cv2.imshow("Account Followers Names", imgOut)
    # cv2.imshow("original", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

img = cv2.imread('test2.jpeg')

img = cv2.resize(img, (500, 750))

fetch_user_name()
image_file = 'user_name_output.jpeg'
user_name_output_list = pytesseract.image_to_string(Image.open(image_file))
print("------------------------------------\n ")
print("Account Holder Name \n ",user_name_output_list)
print("------------------------------------\n ")
fetch_followers()
image_file = 'followers_output.jpeg'
followers_list = pytesseract.image_to_string(Image.open(image_file))
print("Account Followers Name \n ",followers_list)
print("------------------------------------\n ")
updated_followers_list = followers_list.splitlines()
print("Account Followers Name List \n ")
for followers in updated_followers_list[::3]:
    print(followers)
