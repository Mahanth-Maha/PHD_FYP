import setup 
print("Welcome...")
import os
# import shutil
from PIL import Image

from flask import Flask, app, redirect, request, render_template, send_from_directory

from main import PHD_FYP_WEB_APP_API 
from phd_api import PHD_API

print("\n\n\nHang on tight \n\nLoading prereq....\n\n\n")
web_app = PHD_FYP_WEB_APP_API()
phd_run = PHD_API()
# web_app = None
# phd_run = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locerror')
def locerror():
    return render_template('locerror.html')

@app.route('/index')
def inde1():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/pred_res')
def pred_res():
    return render_template('pred_res.html')

@app.route('/maps')
def maps():
    maps_html = False
    with open('templates/maps.html') as f:
        maps_html = f.read()
    if maps_html in ("", " ", None,) :
        return redirect('/locerror')
    return render_template('maps.html')

@app.route('/result', methods=["GET", "POST"])
def nres():
    NoFIleErr = False
    NoPotHolesErr = False
    if request.method == "POST":
        try:
            uploaded_img_to_show = 'static/temp/original_img.JPEG'
            resulted_img_to_show = 'static/temp/result_img.JPEG'
            f = request.files['image']
            basepath = os.path.dirname(__file__)
            filepath = os.path.join(basepath, 'uploads', f.filename)
            f.save(filepath)
            nresult = "NULL"
            print(f'{filepath=}\n,{f.filename=}\n,{basepath=}')
            detect_status = 0
            image_output_path, detect_Scores, detect_status = phd_run.run_phd_and_save_img(input_image_path=filepath)
            print(f'{image_output_path=}\n, {detect_Scores=}\n, {detect_status=}\n')
            NoPotHolesErr = False
            if detect_status == 0:
                nresult = "No potholes detected"
                NoPotHolesErr = True
                loc_status = (False,"No Location Data")
            elif detect_status == 1:
                nresult = "Pothole detected"
                with Image.open(filepath) as img:
                    img.save(uploaded_img_to_show , format='JPEG')
                with Image.open(image_output_path) as img:
                    img.save(resulted_img_to_show , format='JPEG')
                loc_status = web_app.get_img_data(filepath)
            else:
                nresult = "Potholes detected"
                with Image.open(filepath) as img:
                    img.save(uploaded_img_to_show , format='JPEG')
                with Image.open(image_output_path) as img:
                    img.save(resulted_img_to_show , format='JPEG')
                loc_status = web_app.get_img_data(filepath)
            # Open the image file
            # COPYING
            # shutil.copyfile(filepath, uploaded_img_to_show)
            # shutil.copyfile(image_output_path, resulted_img_to_show)
        
            loc_Err_msg = ''
            map_Err_msg = ''
            if loc_status[0] == False:
                loc_Err_msg = loc_status[1]
            map_staus = web_app.generate_map('templates/maps.html')
            if map_staus[0] == False:
                map_Err_msg = loc_status[1]
            if detect_status !=0 : 
                phd_desc = f"Number of Potholes = {detect_status}\n"
            else :
                phd_desc = f"No Potholes detected \n"
            if loc_Err_msg:
                loc_desc = "Location Data Missing Since : " + loc_Err_msg +'\n'
            else:
                loc_desc = "Location Data : Avaliable"+ '\n'
            if map_Err_msg:
                map_desc = "Map data Missing Since :" + map_Err_msg +'\n'
            else:
                map_desc = "Map Status : Avaliable "+ '\nMAP GENERATED\n'
        except Exception as e:
            nresult = False
            map_desc = False
            phd_desc = False
            loc_desc = False
            NoFIleErr = "Please select a valid location"
        return render_template('pred_res_img.html', prediction=nresult,res_desc = phd_desc,loc_desc=loc_desc,map_desc=map_desc,NoFIleErr = NoFIleErr,NoPotHolesErr = NoPotHolesErr)



if __name__ == "__main__":
    app.run(debug=False, port=8080)
    # app.run(debug=False,host= '192.168.0.160', port=8080)
    # app.run(debug=False,host= '192.168.0.122', port=4444)
