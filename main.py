import database
import static_maps
import Location

import os

class PHD_FYP_WEB_APP_API:
    def __init__(self):
        self.db = database.ImagesDB()
        
    def get_img_data(self,filepath):
        loc = Location.GetLocFromImage(filepath)
        if loc == False:
            return False,"No Location Data"
        else:
            lattitude_of_img ,longitude_of_img = loc
        result_image_path = filepath
        self.db.Run(self.db.insert_data,lattitude_of_img,longitude_of_img,os.path.basename(filepath), result_image_path)
        return result_image_path,"ALL OK"
    
    def generate_map(self,path_to_html = 'map.html'):
        locs = self.db.phd_markers_generator()
        if locs == None or len(locs) == 0:
            return False,"No Location Data"
        map = static_maps.StaticMapHTMLGenerator(locs[0][0],locs[0][1])
        map.phd_fyp_html_generator(locs=locs,path=path_to_html)
        return True, "ALL OK"

    def DESTROY(self):
        self.db.Run(self.db.delete_all_rows)
        
    def DEBUG(self):
        self.db.Run(self.db.extract_recent_rows)
        

def main():
    web_app = PHD_FYP_WEB_APP_API()
    
    # imgpaths = [
    #     "C:/Maha/Temp/FullSizeRender.jpg",
    #     "C:/Maha/Temp/IMG_5892.JPEG",
    #     "C:/Maha/Temp/IMG20191124112930.jpg",
    #     "C:/Maha/Temp/IMG20221112195235.jpg",
    #     "C:/Maha/Temp/IMG20221111091405.jpg" 
    # ]
    # for i in imgpaths:
    #     A = web_app.get_img_data(i)
    #     if A:
    #         print(i,"OK")
    #     else:
    #         print(i,"NOT OK")
    #     import time
    #     time.sleep(1)
    # # web_app.generate_map()
    # print("[+] MAP GENERATED")
    
    web_app.DESTROY()


if __name__ == '__main__':
    main()