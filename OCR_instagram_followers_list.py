import cv2
import numpy as np
from PIL import Image
from pytesseract import *

class OCR:
    def __init__(self):
        """
            initialize veriables
        """
        pass

    def fetch_croped_img(self, img, crop_points, width, height):
        overlapping_area_pts = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(crop_points, overlapping_area_pts)
        imgOut = cv2.warpPerspective(img, matrix, (width, height))
        return imgOut

    def get_acc_holder_name_text(self, cropped_img):
        result_acc_holder_name = pytesseract.image_to_string(cropped_img)
        return result_acc_holder_name

    def get_acc_followers_name_text(self, cropped_img):
        result_text = pytesseract.image_to_string(cropped_img)
        followers_list = result_text.replace("\n \n", "\n")
        followers_list = followers_list.replace("\n\n\n", "\n").replace("\n\n", "\n")
        # print(repr(followers_list), "*************")
        final_follower_list = followers_list.splitlines()
        return final_follower_list[::2]

    def read_input(self):
        img = cv2.imread('Data/test2.jpg')
        height, width, _ = img.shape
        acc_holder_width, acc_holder_height = 550, 200
        acc_follower_width, acc_follower_height = 290, 600
        if (height < 2500) and (height > 2180):
            img = cv2.resize(img, (500, 760))
            followers_crop_pints = np.float32([[102, 110], [299, 110], [105, 682], [296, 682]])
            acc_holder_crop_pints = np.float32([[69,36],[382,37],[70,70],[381,67]])
        else:
            img = cv2.resize(img, (500, 750))
            followers_crop_pints = np.float32([[102, 110], [299, 110], [105, 688], [296, 688]])
            acc_holder_crop_pints = np.float32([[69,36],[382,37],[70,70],[381,67]])
        return img, followers_crop_pints, acc_holder_crop_pints, acc_holder_width, acc_holder_height, acc_follower_width, acc_follower_height

if __name__ == "__main__":

    # Initialize instances
    ocr_obj = OCR()
    # Read Input Image
    img, followers_crop_pints, acc_holder_crop_pints, acc_holder_width, acc_holder_height, acc_follower_width, acc_follower_height = ocr_obj.read_input()
    # get cropped img for account holder
    acc_holder_imgOut = ocr_obj.fetch_croped_img(img, acc_holder_crop_pints, acc_holder_width, acc_holder_height)
    # get Account Holder Name
    result_acc_holder_name = ocr_obj.get_acc_holder_name_text(acc_holder_imgOut)
    # get cropped img for account follower list
    acc_follower_imgOut = ocr_obj.fetch_croped_img(img, followers_crop_pints, acc_follower_width, acc_follower_height)
    # get Account Followers List
    cv2.imshow("Account follower Name", acc_follower_imgOut)
    cv2.imshow("Account Holder Name", acc_holder_imgOut)
    final_follower_list = ocr_obj.get_acc_followers_name_text(acc_follower_imgOut)

    print("\n Account Holder Name :", result_acc_holder_name)
    print("\n Account Holder Follower List :", final_follower_list)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


