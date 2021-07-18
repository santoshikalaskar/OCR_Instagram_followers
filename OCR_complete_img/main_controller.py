from OCR_instagram_complete_img import OCR_instagram
import sys
sys.path.append('../')
import logger_hander

class OCR_main_controller:
    def __init__(self):
        """
            initialize variables
        """
        pass

    def default(self):
        return "Incorrect Input"

    def social_media_handler(self, img_path, social_media_name, check_followers_list):
        """
           Social Media handler
           input : img_path, social_media_name & followers_list for checking
           Output : Followers present or not Present
        """
        try:
            switcher = {
                "instagram": ocr_insta_obj.instagram_handler(img_path, check_followers_list),
            #     "facebook": ,
            #     "twitter": ,
            #     "linkedin": ,
            }
            return switcher.get(social_media_name, self.default)()

        except Exception as e:
            logger.exception("Something went Wrong {}".format(e))


if __name__ == "__main__":
    try:
        ocr_obj = OCR_main_controller()
        logger = logger_hander.set_logger()
        ocr_insta_obj = OCR_instagram()

        img_path = "../Data/test2.jpg"
        check_followers_list = ['bridgelabz', 'codermacha', 'confident_coder']
        social_media_name = "Instagram"

        ocr_obj.social_media_handler(img_path, social_media_name, check_followers_list)

    except Exception as e:
        logger.exception("Something went Wrong in main controller {}".format(e))
