import cv2
import numpy as np
from PIL import Image
from pytesseract import *
import sys
sys.path.append('../')
import logger_hander

class OCR_instagram:
    def __init__(self):
        """
            initialize loggers
        """
        self.logger = logger_hander.set_logger()

    def fetch_croped_img(self, img, crop_points, width, height):
        """
            get cropped img
        """
        try:
            overlapping_area_pts = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv2.getPerspectiveTransform(crop_points, overlapping_area_pts)
            imgOut = cv2.warpPerspective(img, matrix, (width, height))
            return imgOut

        except Exception as e:
            self.logger.exception("Something went Wrong while cropping input image {}".format(e))

    def get_acc_holder_name_text(self, cropped_img):
        """
            get Account holder name in text format
        """
        try:
            result_acc_holder_name = pytesseract.image_to_string(cropped_img)
            return result_acc_holder_name
        except Exception as e:
            self.logger.exception("Something went Wrong while fetching Account Holder Name {}".format(e))
            
    def get_acc_followers_name_text(self, cropped_img):
        """
            get Account Followers name's list in text format
        """
        try:
            result_text = pytesseract.image_to_string(cropped_img)
            followers_list = result_text.replace("\n \n", "\n")
            followers_list = followers_list.replace("\n\n\n", "\n").replace("\n\n", "\n")
            # print(repr(followers_list), "*************")
            final_follower_list = followers_list.splitlines()
            return final_follower_list[::2]
        except Exception as e:
            self.logger.exception("Something went Wrong while getting Account Followers name's list in text format {}".format(e))

    def get_cropping_points_input_img(self, img_path):
        """
            get input img cropping points of Account holder name & Followers list names
        """
        try:
            img = cv2.imread(img_path)
            height, width, _ = img.shape
            acc_holder_width, acc_holder_height = 550, 200
            acc_follower_width, acc_follower_height = 290, 600
            if (height < 2500) and (height > 2180):
                img = cv2.resize(img, (500, 760))
                followers_crop_pints = np.float32([[102, 110], [299, 110], [105, 682], [296, 682]])
                acc_holder_crop_pints = np.float32([[69,36],[382,37],[70,70],[381,67]])
            else:
                img = cv2.resize(img, (500, 750))
                followers_crop_pints = np.float32([[100, 110], [299, 110], [105, 688], [296, 688]])
                acc_holder_crop_pints = np.float32([[69,36],[382,37],[70,70],[381,67]])
            return img, followers_crop_pints, acc_holder_crop_pints, acc_holder_width, acc_holder_height, acc_follower_width, acc_follower_height
        except Exception as e:
            self.logger.exception("Something went Wrong while getting input img cropping points of Account holder name & Followers list names {}".format(e))

    def check_followers(self, followers_list, check_list):
        """
            Check list of followers present or not from result list
        """
        try:
            result_list = []
            for check_list_item in check_list:
                if check_list_item in followers_list:
                    result_list.append(True)
                else:
                    result_list.append(False)
            return result_list
        except Exception as e:
            self.logger.exception("Something went Wrong while Checking list of followers present or not from result list {}".format(e))


    def instagram_handler(self, img_path, check_followers_list):
        """
           Instagram OCR handler
           input : img_path & followers_list for checking
           Output : Followers present or not Present
        """
        try:
            img, followers_crop_pints, acc_holder_crop_pints, acc_holder_width, acc_holder_height, acc_follower_width, acc_follower_height = self.get_cropping_points_input_img(img_path)
            # get cropped img for account holder
            acc_holder_imgOut = self.fetch_croped_img(img, acc_holder_crop_pints, acc_holder_width, acc_holder_height)
            # get Account Holder Name
            result_acc_holder_name = self.get_acc_holder_name_text(acc_holder_imgOut)

            # get cropped img for account follower list
            acc_follower_imgOut = self.fetch_croped_img(img, followers_crop_pints, acc_follower_width, acc_follower_height)
            # get Account Followers List
            final_follower_list = self.get_acc_followers_name_text(acc_follower_imgOut)

            # show extracted result
            print("\n Account Holder Name :", result_acc_holder_name)
            print("\n Account Holder Follower List :", final_follower_list)

            result = self.check_followers(final_follower_list, check_followers_list)
            if all(bool(x) == True for x in result):
                print("\n ******************\n All Followers Present \n ******************\n")
            else:
                print(result,"\n ******************\n Followers not Present\n ******************\n")

            # # show cropped img
            # cv2.imshow("Account follower Name", acc_follower_imgOut)
            # cv2.imshow("Account Holder Name", acc_holder_imgOut)
            # if cv2.waitKey(0) & 0xFF == ord('q'):
            #     cv2.destroyAllWindows()
        except Exception as e:
            self.logger.exception("Something went Wrong in Instagram OCR handler {}".format(e))

# if __name__ == "__main__":
#     ocr_insta_obj = OCR_instagram()
# 
#     img_path = "Data/test_s3.jpg"
#     check_followers_list = ['rohan_a_patil', 'moolyadhiraj']
#     social_media_name = "instagram"
# 
#     ocr_insta_obj.instagram_handler(img_path,social_media_name,check_followers_list)




