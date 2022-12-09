import setup 

import os
from flask import Flask, app, request, render_template, send_from_directory

from main import PHD_FYP_WEB_APP_API 
from phd_api import PHD_API

print("\n\n\nHang on tight \n\nLoading prereq....\n\n\n")
web_app = PHD_FYP_WEB_APP_API()
phd_run = PHD_API()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


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
    return render_template('maps.html')

@app.route('/result', methods=["GET", "POST"])
def nres():
    
    if request.method == "POST":
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads', f.filename)
        f.save(filepath)
        nresult = "NULL"
        print(f'{filepath=},{f.filename=},{basepath=}')
        detect_status = 0
        image_output_path, detect_Scores, detect_status = phd_run.run_phd_and_save_img(input_image_path=filepath)
        print(f'{image_output_path=}, {detect_Scores=}, {detect_status=}')
        if detect_status == 0:
            nresult = "No potholes detected"
        elif detect_status == 1:
            nresult = "Pothole detected"
        else:
            nresult = "Potholes detected"
        loc_status = web_app.get_img_data(filepath)
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
            
        return render_template('pred_res.html', prediction=nresult,res_desc = phd_desc,loc_desc=loc_desc,map_desc=map_desc)

if __name__ == "__main__":
    app.run(debug=False, port=8080)
