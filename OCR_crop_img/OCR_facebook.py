import cv2
import numpy as np
from PIL import Image
from pytesseract import *
import sys
sys.path.append('../')
import logger_hander

class OCR_facebook:
    def __init__(self):
        """
            initialize variables
        """
        self.logger = logger_hander.set_logger()
        
    def facebook_handler(self, img_path, check_followers_list):
        """
           Facebook OCR handler
           input : img_path & followers_list for checking
           Output : Followers present or not Present
        """
        pass
    