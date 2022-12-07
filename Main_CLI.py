import sys
from PIL import Image
import cv2
if __name__ == '__main__':
    # check if the user provided a file path as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        exit()
    else:
        import model_runner
        # open the image and display it
        image_path = sys.argv[1]
        image = Image.open(image_path)
        image.show()
        img_out = model_runner.run_main(image_path)
        # DISPLAYS OUTPUT IMAGE
        cv2.imshow("TEST",img_out)
        cv2.waitKey(0)
        # CLOSES WINDOW ONCE KEY IS PRESSED


