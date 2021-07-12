import cv2
import numpy as np
from PIL import Image
from pytesseract import *
import re

class OCR:
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
        holder_name = img_text.split("<")[1].split('\n')[0]
        reexp = "(?:^|(?<= ))[a-zA-Z0-9]+(?= |$)"
        holder_name = re.findall(reexp, holder_name)
        # print("---------------- \n",holder_name,"\n------------------")
        return holder_name[0]

    def check_followers(self, followers_list, check_list):
        """
            Check list of followers present or not from result list
        """
        if all(i in followers_list for i in check_list):
            return True
        else:
            return False

    def instagram_handler(self, img_path, social_media, check_followers_list):
        """
           Instagram OCR
           input : img_path, social_media_name & followers_list for checking
           Output : Followers present or not Present
        """
        if social_media == "instagram":
            img = cv2.imread(img_path)
            text_result = self.fetch_text(img)
            print(text_result)
            acc_holder_name = self.get_acc_holder_name_text(text_result)
            print(acc_holder_name)
            followers_list = text_result.split("<")[1].split()
            print(self.check_followers(followers_list, check_followers_list))

if __name__ == "__main__":
    ocr_obj = OCR()

    img_path = "Data/test_s2.jpg"
    check_followers_list = ['harshu_kitty_lover_20', 'ganeshkondawar88']
    social_media_name = "instagram"

    ocr_obj.instagram_handler(img_path,social_media_name,check_followers_list)
    