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


# Machine Learning

## Tensorflow
TensorFlow is an open-source software library for machine learning, specifically deep learning and numeric computation. It is often used for building and training machine learning models, particularly neural networks. TensorFlow allows developers to create data flow graphs, which are structures that describe how data moves through a graph of computational operations. This makes it easy to build and train complex models with many layers, and it also allows for efficient training on large datasets using parallel processing. TensorFlow has become one of the most popular tools for machine learning and deep learning, and is widely used in both industry and academia.
## Object Detection API
An object detection API is a type of software that can be used to identify objects within images or videos. These APIs typically use machine learning algorithms to identify and locate objects within the image or video, and can be used for a wide variety of applications, such as security and surveillance, image recognition, and autonomous vehicles. Object detection APIs can be used by developers to build applications that can automatically detect and identify objects within images or videos, making it possible to perform tasks such as tracking objects in a video feed or identifying objects in a photograph.
## why python programming
Python is popular in machine learning for several reasons. First, it is a high-level, general-purpose programming language, which means that it is easy to read and write, and it can be used for a wide variety of tasks, including building machine learning models. Second, Python has a large and active community of users, which means that there is a wealth of support and resources available for those learning to use the language, as well as a large number of libraries and frameworks that can be leveraged to build machine learning models more easily. Finally, Python has many powerful libraries and frameworks specifically designed for machine learning, such as TensorFlow, PyTorch, and scikit-learn, which make it a good choice for those looking to get started with machine learning.

## Testing custom images

extract [the zip file](https://1drv.ms/u/s!AhCzSwMWU4mgjWGoSiiHpkaqP8YB?e=vfD9JB) into ` training_demo\` folder.

install python-3.9.X 
go to the root folder of the project and run the command below (it is recommended to use a venv for testing the project)

```
pip install tensorflow=2.5.0 numpy opencv-python tensorflow-object-detection-api customtkinter
```
### Running in a loop (debugging purpose)
```
python model_runnner.py
```
paste the image path when prompted (no image is shown) , after Successfully generating output, It re-runs the program again. To exit the program Press "exit" and enter enter(Return) Key.

### Running as a product for an image (CLI)

By running this python script it opens the Input image and the output image generated in separate window.

Note : Replace the <image_path> with the actual image path while running the Script.
```
python Main_CLI.py <image_path>
```

### Running as a product for an image (GUI)

Select the image form the drop down and click Run.

```
python Main_GUI.py
```

### THe Results

the Resulting image will be saved in ` Dataset\Result ` folder

## Demo

Result for an image
### Image 

![Original](https://github.com/Mahanth-Maha/PHD_FYP/blob/main/Dataset/train/potholes/img00000.JPEG)

### Result

![detected](https://github.com/Mahanth-Maha/PHD_FYP/blob/main/Dataset/Result/res_img00000.JPEG)
