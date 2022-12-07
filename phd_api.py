from PIL import Image
import numpy as np
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import label_map_util
import time
import cv2
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


class PHD_API:
    def __init__(self) -> None:    
        self.PATH_TO_MODEL_DIR = './training_demo/exported-models/my_model'
        self.PATH_TO_LABELS = './training_demo/annotations/label_map.pbtxt'
        self.MIN_CONF_THRESH = float(0.60)
        self.PATH_TO_SAVED_MODEL = self.PATH_TO_MODEL_DIR + "/saved_model"
        self.category_index = label_map_util.create_category_index_from_labelmap(self.PATH_TO_LABELS,use_display_name=True)
        self.detect_fn = tf.saved_model.load(self.PATH_TO_SAVED_MODEL)
        

    def load_image_into_numpy_array(self, path):
        """Load an image from file into a numpy array.
        Puts image into numpy array to feed into tensorflow graph.
        Note that by convention we put it into a numpy array with shape
        (height, width, channels), where channels=3 for RGB.
        Args:
        path: the file path to the image
        Returns:
        uint8 numpy array with shape (img_height, img_width, 3)
        """
        return np.array(Image.open(path))


    def generate_result(self, IMAGE_PATH):
        image = cv2.imread(IMAGE_PATH)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_expanded = np.expand_dims(image_rgb, axis=0)
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis, ...]
        detections = self.detect_fn(input_tensor)
        print(detections)
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
        detections['num_detections'] = num_detections
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
        image_with_detections = image.copy()
        
        viz_utils.visualize_boxes_and_labels_on_image_array(
            image_with_detections,
            detections['detection_boxes'],
            detections['detection_classes'],
            detections['detection_scores'],
            self.category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=200,
            min_score_thresh=0.5,
            agnostic_mode=False)
        
        detections_scores_all = detections['detection_scores'].tolist()
        min_threshold_of_scores = 0.5
        result = [i for i in detections_scores_all if i > min_threshold_of_scores ]
        num_of_detections = len(result)
        return image_with_detections,result,num_of_detections
    
    def save_result(self,original_image,image_with_detections):
        self.PATH_2_SAVE_ANNOTED_PIC = './Dataset/Result/res_' + str(int(time.time())) + '_'
        try:
            file_name_ = original_image.split('\\')[-1]
            isWritten = cv2.imwrite(
                self.PATH_2_SAVE_ANNOTED_PIC + file_name_, image_with_detections)
            if isWritten:
                print(
                    f'[+] Image is successfully saved as file at {self.PATH_2_SAVE_ANNOTED_PIC + file_name_}')
            else:
                print('[-] Image is not saved', isWritten)
        except Exception:
            print('[-] ERR :', original_image)
        print('[+] Re-Running : press Enter or enter exit to exit the program\n')
        return self.PATH_2_SAVE_ANNOTED_PIC + file_name_
        
    def run_phd(self,input_image_path):
        """
        Object Detection on image given as input and finds pothole

        Args:
            input_image_path (str)

        Returns:
            outputs 3 tuple of image in cv2, Scores of Results , Dectect Status: Detect Status  -> 0 => No Detection , Number => number of detections found
        """
        return self.generate_result(input_image_path)
        
    def run_phd_and_save_img(self,input_image_path):
        """
        Pothole Detection on image given as input and finds pothole

        Args:
            input_image_path (str)

        Returns:
            outputs 3 tuple of resultant image path, Scores of Results , Dectect Status: Detect Status  -> 0 => No Detection , Number => number of detections found
        """
        img_w_d , Score , num_det = self.generate_result(input_image_path) 
        return self.save_result(original_image = input_image_path,image_with_detections = img_w_d) , Score , num_det
        
# def main():
#     while 1:
#         img_name = input("\nPaste the path of input file : ")
#         if img_name in ('', " ", "exit", "EXIT", "No"):
#             break
#         try:
#             image_with_detections = generate_result(img_name)
#             print(img_name)
#             file_name_ = img_name.split('\\')[-1]
#             isWritten = cv2.imwrite(
#                 PATH_2_SAVE_ANNOTED_PIC + file_name_, image_with_detections)
#             if isWritten:
#                 print(
#                     f'[+] Image is successfully saved as file at {PATH_2_SAVE_ANNOTED_PIC + file_name_}')
#             else:
#                 print('[-] Image is not saved', isWritten)
#         except Exception:
#             print('[-] ERR :', img_name)
#         print('[+] Re-Running : press Enter or enter exit to exit the program\n')

def main():
    Main_model = PHD_API()
    img_name = input("\nPaste the path of input file : ")
    print(Main_model.run_phd_and_save_img(img_name))

if __name__ == '__main__':
    main()
