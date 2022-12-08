from GPSPhoto import gpsphoto


def GetLocFromImage(filepath):
    try:
        LocA = gpsphoto.getGPSData(filepath)
        Cord = LocA['Latitude'] , LocA['Longitude']
        # print( f"\n{LocA['Latitude']},{LocA['Longitude']}")
        return Cord
    except Exception:
        return False

def main(filepath):
    return GetLocFromImage(filepath)


if __name__ == '__main__':
    img_path__ = "C:/Maha/Temp/IMG_5892.JPEG"
    new_img_path__ = "C:/Maha/Temp/FullSizeRender.jpg"
    No_exif_data_img_path__ = "C:/Maha/Temp/IMG20191124112930.jpg"
    No_exif_data_img_path__2 = "C:/Maha/Temp/IMG20221112195235.jpg"
    print(main(img_path__))
    print(main(new_img_path__))
    print(main(No_exif_data_img_path__))
    print(main(No_exif_data_img_path__2))
    
    nod = "C:/Maha/Temp/IMG20221111091405.jpg" 
    print(main(nod))
    