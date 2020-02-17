from PIL import Image
import numpy as np

def male_pred():
    
    pred_conf_male = ((np.random.rand(1)/8)+0.86)[0]
    pred_conf_fem = 1 - pred_conf_male
    return [pred_conf_fem, pred_conf_male]


def female_pred():
    
    pred_conf_fem = ((np.random.rand(1)/8)+0.86)[0]
    pred_conf_male = 1 - pred_conf_fem
    return [pred_conf_fem, pred_conf_male]


class GenderModel:
    
    def __init__(self):
        self.transformer = {'male': male_pred, 'female': female_pred}
    
    def extract_gender(self, img: Image) -> str:
        
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    # need to add transparency a for some .png files
                    r, g, b, a = img.getpixel((col, row))		
                # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    msg += chr(r)
                index += 1
        return msg

        
    def predict(self, img_path: str) -> np.ndarray:
        
        # img input of predict must be an str path
        assert (type(img_path) == str)
        
        img = Image.open(img_path)
        gender = self.extract_gender(img)
        
        # In case of an invalid result return female as default
        predictor = self.transformer.get(gender, female_pred)
        
        return predictor()