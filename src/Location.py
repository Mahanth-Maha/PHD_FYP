from GPSPhoto import gpsphoto

def GetLocFromImage(filepath):
    LocA = gpsphoto.getGPSData(filepath)
    Cord = LocA['Latitude'] , LocA['Longitude']
    print( f"\n{LocA['Latitude']},{LocA['Longitude']}")
    return Cord

def main(filepath):
    GetLocFromImage(filepath)

if __name__ == '__main__':
    while(1):
        path_ = input("paste File loc :")
        if path_ == "":
            break
        main(path_)