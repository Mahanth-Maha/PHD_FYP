from PIL import Image
import numpy as np
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import label_map_util
import time
import cv2
import tensorflow as tf
import os

# import warnings
# import pathlib
# import argparse
# import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
# warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# PROVIDE PATH TO IMAGE DIRECTORY
# IMAGE_PATHS = '/content/training_demo/images/train/image1.jpg'
# IMAGE_PATHS = 'C:/Maha/dev/Temp/PHD_FYP_TEMP/TensorFlow/workspace/training_demo/images/test/37.JPEG'

# PROVIDE PATH TO MODEL DIRECTORY
# PATH_TO_MODEL_DIR = '/content/training_demo/exported_models/my_model'
PATH_TO_MODEL_DIR = './training_demo/exported-models/my_model'

# PROVIDE PATH TO LABEL MAP
# PATH_TO_LABELS = '/content/training_demo/annotations/label_map.pbtxt'
PATH_TO_LABELS = './training_demo/annotations/label_map.pbtxt'

# PROVIDE THE MINIMUM CONFIDENCE THRESHOLD
MIN_CONF_THRESH = float(0.60)

# LOAD THE MODEL
PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR + "/saved_model"

print('''
██████╗  ██████╗ ████████╗██╗  ██╗ ██████╗ ██╗     ███████╗    ██████╗ ███████╗████████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗    
██╔══██╗██╔═══██╗╚══██╔══╝██║  ██║██╔═══██╗██║     ██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║    
██████╔╝██║   ██║   ██║   ███████║██║   ██║██║     █████╗      ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║    
██╔═══╝ ██║   ██║   ██║   ██╔══██║██║   ██║██║     ██╔══╝      ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║    
██║     ╚██████╔╝   ██║   ██║  ██║╚██████╔╝███████╗███████╗    ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║    
╚═╝      ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    
                                                                                                                                           
███████╗██╗███╗   ██╗ █████╗ ██╗         ██╗   ██╗███████╗ █████╗ ██████╗     ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗   
██╔════╝██║████╗  ██║██╔══██╗██║         ╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝   
█████╗  ██║██╔██╗ ██║███████║██║          ╚████╔╝ █████╗  ███████║██████╔╝    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║      
██╔══╝  ██║██║╚██╗██║██╔══██║██║           ╚██╔╝  ██╔══╝  ██╔══██║██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║      
██║     ██║██║ ╚████║██║  ██║███████╗       ██║   ███████╗██║  ██║██║  ██║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║      
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝      

-....- -....- -....- -....-    -.-- .- .-.. .-.. .-    -- .- .... .- -. - ....    -....- -....- -....- -....- 
                                                                                                                                           
      ''')
print('Loading model...', end='')
start_time = time.time()

# LOAD SAVED MODEL AND BUILD DETECTION FUNCTION
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

# LOAD LABEL MAP DATA FOR PLOTTING
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)


def load_image_into_numpy_array(path):
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


def generate_result(IMAGE_PATHS):
    # print('Running inference for {}... '.format(IMAGE_PATHS), end='')
    image = cv2.imread(IMAGE_PATHS)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)

    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis, ...]

    # input_tensor = np.expand_dims(image_np, 0)
    detections = detect_fn(input_tensor)

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(
        np.int64)

    image_with_detections = image.copy()

    # SET MIN_SCORE_THRESH BASED ON YOU MINIMUM THRESHOLD FOR DETECTIONS
    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=0.5,
        agnostic_mode=False)

    # print('Done')
    return image_with_detections
    # # DISPLAYS OUTPUT IMAGE
    # cv2.imshow("TEST",image_with_detections)
    # cv2.waitKey(0)
    # # CLOSES WINDOW ONCE KEY IS PRESSED

    # cv2.destroyAllWindows()


# path = '/Dataset//train//potholes//'
# list_files = []
# for root, dirs, files in os.walk(path):
#     for file in files:
#         list_files.append(os.path.join(root, file))
# path = 'C://Maha//dev//Github//PHD_FYP//Dataset//train//normal//'
# for root, dirs, files in os.walk(path):
#     for file in files:
#         list_files.append(os.path.join(root, file))
# path = 'C://Maha//dev//Temp//PHD_FYP_TEMP//TensorFlow//workspace//training_demo//images//test//'
# for root, dirs, files in os.walk(path):
#     for file in files:
#         list_files.append(os.path.join(root, file))

# images_test_ = [l for l in list_files if l.endswith('.JPEG')]


PATH_2_SAVE_ANNOTED_PIC = './Dataset/Result/res_' + str(int(time.time())) + '_'

# for img_name in images_test_:


def main():
    while 1:
        img_name = input("\nPaste the path of input file : ")
        if img_name in ('', " ", "exit", "EXIT", "No"):
            break
        try:
            image_with_detections = generate_result(img_name)
            print(img_name)
            file_name_ = img_name.split('\\')[-1]
            isWritten = cv2.imwrite(
                PATH_2_SAVE_ANNOTED_PIC + file_name_, image_with_detections)
            if isWritten:
                print(
                    f'[+] Image is successfully saved as file at {PATH_2_SAVE_ANNOTED_PIC + file_name_}')
            else:
                print('[-] Image is not saved', isWritten)
        except Exception:
            print('[-] ERR :', img_name)
        print('[+] Re-Running : press Enter or enter exit to exit the program\n')

def run_main(img_name):
    if img_name in ('', " ", "exit", "EXIT", "No"):
        return False
    try:
        image_with_detections = generate_result(img_name)
        # print(img_name)
        file_name_ = img_name.split('\\')[-1]
        isWritten = cv2.imwrite(
            PATH_2_SAVE_ANNOTED_PIC + file_name_, image_with_detections)
        if isWritten:
            print(
                f'[+] Image is successfully saved as file at {PATH_2_SAVE_ANNOTED_PIC + file_name_}')
        else:
            print('[-] Image is not saved', isWritten)
    except Exception:
        print('[-] ERR :', img_name)
    print('[+] Press any key to EXIT\n')
    return image_with_detections

if __name__ == '__main__':
    main()
