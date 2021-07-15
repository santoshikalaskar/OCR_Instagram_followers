from OCR_instagram import OCR_instagram
from OCR_facebook import OCR_facebook
from OCR_linkedin import OCR_linkedin
import sys
sys.path.append('../')
import logger_hander

class OCR_main_controller:
    def __init__(self):
        """
            initialize variables
        """
        pass
    
    def social_media_handler(self, img_path,social_media_name,check_followers_list):
        """
           Social Media handler
           input : img_path, social_media_name & followers_list for checking
           Output : Followers present or not Present
        """
        try:
            if social_media_name.lower() == "instagram":
                ocr_insta_obj.instagram_handler( img_path,check_followers_list)

            elif social_media_name.lower() == "facebook":
                ocr_fb_obj.facebook_handler( img_path,check_followers_list)

            elif social_media_name.lower() == "linkedin":
                ocr_linkedin_obj.linkedin_handler( img_path,check_followers_list)
        
        except Exception as e:
            logger.exception("Something went Wrong {}".format(e))
    
if __name__ == "__main__":
    ocr_obj = OCR_main_controller()
    logger = logger_hander.set_logger()
    ocr_insta_obj = OCR_instagram()
    ocr_fb_obj = OCR_facebook()
    ocr_linkedin_obj = OCR_linkedin()

    img_path = "../Data/test_s3.jpg"
    check_followers_list = ['soni_codes', 'swap_369']
    social_media_name = "instagram"

    ocr_obj.social_media_handler(img_path,social_media_name,check_followers_list)
