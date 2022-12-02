# PHD_FYP
A web app for The Pot Hole Detection on images and open CV and TensorFlow.

The web app would include a way to upload the image that the user took of the pothole at certain location and our model would predict if there exist any pothole  and then updates the database. So, that whenever Other person logs into the webpage, he will be notified that there is a pothole day by showing the marker over the location that the picture was taken.


By using this markers on the location one could easily find out that the road that they are taking Contains a pothole, so They can slow down the vehicle or if they really want to avoid such potholes and don't, Make any damage to the vehicle, They could take another path which has the less potholes. 

Government bodies can use this app to locate the potholes that there exist in the roads and try to fix it. Or any citizens near the locations could try to fix it by covering it is something that it would make it gone. **Thus making the world a better place.**

## Testing custom images

extract [the zip file](https://1drv.ms/u/s!AhCzSwMWU4mgjWGoSiiHpkaqP8YB?e=vfD9JB) into ` training_demo\` folder & then run

```
pip install -r requirements
python model_runnner.py
```

paste the image path when prompted

image will be saved in ` Dataset\Result ` folder

## Demo

Result for an image
### Image 

![Original](https://github.com/Mahanth-Maha/PHD_FYP/blob/main/Dataset/train/potholes/img00000.JPEG)

### Result

![detected](https://github.com/Mahanth-Maha/PHD_FYP/blob/main/Dataset/Result/res_img00000.JPEG)
