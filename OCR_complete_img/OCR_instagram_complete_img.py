import cv2
import numpy as np
from PIL import Image
from pytesseract import *
import re

class OCR_instagram:
    def __init__(self):
        """
            initialize variables
        """
        pass

    def fetch_text(self, img):
        text_result = pytesseract.image_to_string(img)
        return text_result

    def get_acc_holder_name_text(self, img_text):
        """
            get Account holder name in text format
        """
        try:
            holder_name = img_text.split("<")[1].split('\n')[0]
            regexp = "(?:^|(?<= ))[a-zA-Z0-9]+(?= |$)"
            holder_name = re.findall(regexp, holder_name)
            if len(holder_name) > 0:
                return holder_name[0]
            else:
                holder_name = img_text.split("<")[1].strip().split("\n")[0]
                return holder_name
        except Exception as e:
            print(e)

    def check_followers(self, followers_list, check_list):
        """
            Check list of followers present or not from result list
        """
        if all(i in followers_list for i in check_list):
            return True
        else:
            return False

    def instagram_handler(self, img_path, check_followers_list):
        """
           Instagram OCR
           input : img_path, social_media_name & followers_list for checking
           Output : Followers present or not Present
        """

        img = cv2.imread(img_path)
        text_result = self.fetch_text(img)
        print(text_result,"------------------")
        acc_holder_name = self.get_acc_holder_name_text(text_result)
        print("Account Holder Name : ",acc_holder_name)
        followers_list = text_result.split("<")[1].split()
        print("Followers List : ",self.check_followers(followers_list, check_followers_list))


# if __name__ == "__main__":
#     ocr_obj = OCR_instagram()
# 
#     img_path = "Data/test_s3.jpg"
#     # check_followers_list = ['harshu_kitty_lover_20', 'ganeshkondawar88']
#     check_followers_list = ['_c_h_h_a_', 'a_x_a_y_2_2_2']
#     social_media_name = "instagram"
# 
#     ocr_obj.instagram_handler(img_path,social_media_name,check_followers_list)
    