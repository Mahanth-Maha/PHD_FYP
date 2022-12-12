# PHD_FYP
A web app for The Pot Hole Detection on images and open CV and TensorFlow.

The web app would include a way to upload the image that the user took of the pothole at certain location and our model would predict if there exist any pothole  and then updates the database. So, that whenever Other person logs into the webpage, he will be notified that there is a pothole day by showing the marker over the location that the picture was taken.

By using this markers on the location one could easily find out that the road that they are taking Contains a pothole, so They can slow down the vehicle or if they really want to avoid such potholes and don't, Make any damage to the vehicle, They could take another path which has the less potholes. 

# PotHole
Potholes are a common problem on roads and highways. These pesky depressions in the road surface can cause serious damage to vehicles and be a major inconvenience for drivers.

Potholes form when water seeps into cracks in the road surface and then freezes and expands. This expansion puts pressure on the surrounding pavement, eventually causing it to break and form a pothole. As vehicles drive over the weakened area, the pothole grows larger and deeper.

Potholes can range in size from a few inches to several feet in diameter, and they can be found on any type of road, from city streets to rural highways. They can be especially **dangerous** for bicyclists and motorcyclists, who are more vulnerable to the effects of potholes.

One of the biggest problems with potholes is that they can cause significant ***damage to vehicles***. A pothole can cause **a tire to blow out**, damage the suspension, or even ***cause an accident*** if a driver swerves to avoid it. This can be a costly inconvenience for drivers, who may have to pay for repairs or even a rental car while their own vehicle is being repaired.

To avoid damage from potholes, it is important for drivers to pay attention to the road and watch for potholes. When driving over a pothole, it is best to slow down and try to avoid it if possible. If it is not possible to avoid the pothole, drivers should try to drive over it slowly and straight, rather than at an angle.

Another way to avoid potholes is Avoiding the roads that are extensively filled with ,But unfortunately there is no app to tell wheather a pothole is in the road or not, so our app will show the All the portals that are there In that road so that one can avoid that road.

In addition to preventing potholes, regular road maintenance can also improve the overall safety and condition of the road. This can include repaving worn or damaged sections of the road, as well as regularly inspecting and repairing drainage systems to prevent water from accumulating on the road.
In which our app can again be used by the government agencies to detect The potholes that are there in a road and plan according to to fix the roads which are heavily damaged.
 
Government bodies can use this app to locate the potholes that there exist in the roads and try to fix it. Or any citizens near the locations could try to fix it by covering it is something that it would make it gone. **Thus making the world a better place.**

# Testing custom images

Please check the [project demonstration](https://youtu.be/dQw4w9WgXcQ) that I made before messing things up from Youtube

extract [the zip file](https://1drv.ms/u/s!AhCzSwMWU4mgjWGoSiiHpkaqP8YB?e=vfD9JB) into ` training_demo\` folder.

install python-3.9.X 
go to the root folder of the project and run the command below (it is recommended to use a venv for testing the project)

### Creating v-env to run project
```
conda create --name phd_fyp python==3.9.12
conda activate phd_fyp
```

### NOTE : POSSIBLE ERROR while running the app 

The tensorflow usual throws an error as tf.gfile.GFile not found or tf has no attribute named gfile.
check reslving techniques here in 
* [StackOverflow](https://stackoverflow.com/questions/55591437/attributeerror-module-tensorflow-has-no-attribute-gfile#:~:text=33-,in%202.0%2C%20tf.gfile.*%20is%20replaced%20by%20tf.io.gfile.*.,-when%20I%20get)

* [Tensorflow Issues](https://github.com/tensorflow/tensorflow/issues/31315#:~:text=i%20solved%20the%20error%20by%20replacing%20tf.gfile.fastgfile%20to%20tf.io.gfile.gfile.)

simply ,  ***Replace tf.gfile.GFile to tf.io.gfile.GFile at line number 137***

# End User Product

## Setup 
the setup file is also included with requirements.txt, but _I have wrote the script_ in such a way that it ensures all the dependencies are installed on FIRST TIME RUN , ALL AT ONCE and no more installing or configuring is required except for the mentioned above

Note : if one wants to delete entire database run `python main.py`, which deletes all the entries till now.

## Web App

make sure you are in root directory i.e, `PHD_FYP` and extracted the zip file into ` training_demo\` so that the structure will be ` training_demo\exported-models\models\` (be careful since it might be the case that it extracts ` training_demo\exported-models\exported-models\models\` if it's a windows OS)

```
python app.py
```

go to the web link it provides probably [http://127.0.0.1:8080/](http://127.0.0.1:8080/) , or better open which flask provides dynamically

### web app interface images

![]()

## Running as a product for an image (CLI)

By running this python script it opens the Input image and the output image generated in separate window.

Note : Replace the <image_path> with the actual image path while running the Script.
```
python Main_CLI.py <image_path>
```


### CLI app interface images

![]()


## Running as a product for an image (GUI)

Select the image form the drop down and click Run.

```
python Main_GUI.py
```

### GUI app interface images

![]()

## Build our custom app

Yes, you can integrate pothole detection system into any custom app which is already written as an API in the file named as [phd_api.py](https://github.com/Mahanth-Maha/PHD_FYP/blob/main/phd_api.py).

just import as
```
import phd_api

#create object
phd_run = PHD_API() 

filepath = 'test.jpg'

# use the model
# saves output in /Dataset/Result folder
phd_run.run_phd_and_save_img(input_image_path=filepath)

# alternatively use this to not save result
phd_run.run_phd(input_image_path=filepath)
```


### The Results

the Resulting image will be saved in ` Dataset\Result ` folder

## Demo

Result for an image
### Image 

![Original](https://github.com/Mahanth-Maha/PHD_FYP/blob/main/Dataset/train/potholes/img00000.JPEG)

### Result

![detected](https://github.com/Mahanth-Maha/PHD_FYP/blob/main/Dataset/Result/res_img00000.JPEG)
