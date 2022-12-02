#  Set-ExecutionPolicy RemoteSigned
# Set-ExecutionPolicy Unrestricted 

Write-Host "---- SETTING UP YOUR PHY_FYP ----"
Write-Host "[+] STARTING UP "
Write-Host "[!] Make sure you have a Good internet Connection."

$phd_fyp = split-path -parent $MyInvocation.MyCommand.Definition
mkdir PHD_FYP
# cd PHD_FYP
Write-Host "DIR"
Write-Host $phd_fyp 
$main_dir = "$phd_fyp\PHD_FYP"
Write-Host $main_dir
cd $main_dir
conda create --name phd_fyp2 python=3.9 ipykernel tensorflow
conda activate phd_fyp2
pip install --ignore-installed --upgrade tensorflow==2.5.0
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

Write-Host "[+] installing dependencies"
pip install absl-py==1.3.0 apache-beam==2.43.0 asttokens  astunparse==1.6.3 avro-python3==1.10.2 backcall  Bottleneck  cachetools==5.2.0 certifi  charset-normalizer==2.1.1 cloudpickle==2.2.0 colorama  contextlib2==21.6.0 contourpy==1.0.6 crcmod==1.7 cycler==0.11.0 Cython==0.29.32 debugpy  decorator  dill==0.3.1.1 dm-tree==0.1.7 docopt==0.6.2 entrypoints  etils==0.9.0 executing  fastavro==1.7.0 fasteners==0.18 flatbuffers==22.11.23 fonttools==4.38.0 gast==0.4.0 gin-config==0.5.0 google-api-core==2.10.2 google-api-python-client==2.66.0 google-auth==2.14.1 google-auth-httplib2==0.1.0 google-auth-oauthlib==0.4.6 google-pasta==0.2.0 googleapis-common-protos==1.57.0 grpcio==1.34.1 h5py==3.1.0 hdfs==2.7.0 httplib2==0.20.4 idna==3.4 immutabledict==2.2.3 importlib-metadata==5.1.0 importlib-resources==5.10.0 ipykernel  ipython  jedi  joblib==1.2.0 jupyter_client  jupyter_core  kaggle==1.5.12 keras==2.10.0 keras-nightly==2.5.0.dev2021032900 Keras-Preprocessing==1.1.2 kiwisolver==1.4.4 labelImg==1.8.6 libclang==14.0.6 lvis==0.5.3 lxml==4.9.1 Markdown==3.4.1 MarkupSafe==2.1.1 matplotlib==3.6.2 matplotlib-inline  mkl-fft==1.3.1 mkl-random  mkl-service==2.4.0 nest-asyncio  numexpr  numpy  oauth2client==4.1.3 oauthlib==3.2.2 object-detection  objsize==0.5.2 opencv-python==4.6.0.66 opencv-python-headless==4.6.0.66 opt-einsum==3.3.0 orjson==3.8.2 packaging  pandas  parso  pickleshare  Pillow==9.3.0 portalocker==2.6.0 promise==2.3 prompt-toolkit  proto-plus==1.22.1 protobuf==3.19.6 pure-eval  py-cpuinfo==9.0.0 pyarrow==9.0.0 pyasn1==0.4.8 pyasn1-modules==0.2.8 pycocotools  pydot==1.4.2 Pygments  pymongo==3.13.0 pyparsing  PyQt5==5.15.7 PyQt5-Qt5==5.15.2 PyQt5-sip==12.11.0 python-dateutil  python-slugify==7.0.0 pytz  pywin32==302 PyYAML==5.4.1 pyzmq  regex==2022.10.31 requests==2.28.1 requests-oauthlib==1.3.1 rsa==4.9 sacrebleu==2.2.0 scikit-learn==1.1.3 scipy==1.9.3 sentencepiece==0.1.97 seqeval==1.2.2 six  stack-data  tabulate==0.9.0 tensorboard==2.10.1 tensorboard-data-server==0.6.1 tensorboard-plugin-wit==1.8.1 tensorflow==2.10.1 tensorflow-addons==0.18.0 tensorflow-datasets==4.7.0 tensorflow-estimator==2.10.0 tensorflow-hub==0.12.0 tensorflow-io==0.28.0 tensorflow-io-gcs-filesystem==0.28.0 tensorflow-metadata==1.11.0 tensorflow-model-optimization==0.7.3 tensorflow-text==2.10.0 termcolor==1.1.0 text-unidecode==1.3 tf-models-official==2.10.1 tf-slim==1.1.0 threadpoolctl==3.1.0 toml==0.10.2 tornado  tqdm==4.64.1 traitlets  typeguard==2.13.3 typing-extensions==3.7.4.3 uritemplate==4.1.1 urllib3==1.26.13 wcwidth  Werkzeug==2.2.2 wincertstore==0.2 wrapt==1.12.1 zipp==3.11.0 zstandard==0.19.0
Write-Host "[+] installed all dependencies"

mkdir TensorFlow
cd .\TensorFlow\
git clone https://github.com/tensorflow/models.git
cd .\models\
cd .\research\
Get-ChildItem object_detection/protos/*.proto | foreach {protoc "object_detection/protos/$($_.Name)" --python_out=.}
pip install cython
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
cp object_detection/packages/tf2/setup.py .
python -m pip install --use-feature=2020-resolver .
conda install -c anaconda ipykernel
python -m ipykernel install --user --name phd_fyp --display-name "PHD_FYP_Kernel"
cd ../../
ls
mkdir workspace
cd .\workspace\
mkdir training_demo
cd .\training_demo\
mkdir annotations
mkdir exported-models/
mkdir images
mkdir models
mkdir pre-trained-models
cd .\images\
mkdir test
mkdir train
cd ..
tree
pip install labelImg
labelImg
conda install pandas
cd ../../
mkdir scripts
cd .\scripts\
mkdir preprocessing
cd .\preprocessing\

conda install numpy<1.23.0
conda install pandas
pip install protobuf==3.19.6

# Start-BitsTransfer -Source "https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/_downloads/d0e545609c5f7f49f39abc7b6a38cec3/partition_dataset.py" -Destination "." 
Start-BitsTransfer -Source "https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/_downloads/da4babe668a8afb093cc7776d7e630f3/generate_tfrecord.py" -Destination "."

cd ../../../
# Create train data:
python generate_tfrecord.py -x "$main_dir/TensorFlow/workspace/training_demo/images/train" -l "$main_dir/TensorFlow/workspace/training_demo/annotations/label_map.pbtxt" -o "$main_dir/TensorFlow/workspace/training_demo/annotations/train.record"
# Create test data:
python generate_tfrecord.py -x "$main_dir/TensorFlow/workspace/training_demo/images/test" -l "$main_dir/TensorFlow/workspace/training_demo/annotations/label_map.pbtxt" -o "$main_dir/TensorFlow/workspace/training_demo/annotations/test.record"

cd .\TensorFlow\
cd .\workspace\
cd .\training_demo\
cd .\annotations\

New-Item "label_map.pbtxt" -ItemType File -Value "item {"
Add-Content "label_map.pbtxt" "id: 1"
Add-Content "label_map.pbtxt" "    name: 'pothole'"
Add-Content "label_map.pbtxt" "}"

cd $main_dir


cd .\TensorFlow\workspace\training_demo\models\
mkdir my_ssd_resnet50_v1_fpn

cd $main_dir
cp TensorFlow/models/research/object_detection/model_main_tf2.py .\TensorFlow\workspace\training_demo\
cp TensorFlow/models/research/object_detection/exporter_main_v2.py .\TensorFlow\workspace\training_demo\

cd .\TensorFlow\workspace\training_demo\
python model_main_tf2.py --model_dir=models/my_ssd_resnet50_v1_fpn --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config

python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path .\models\my_ssd_resnet50_v1_fpn\pipeline.config --trained_checkpoint_dir .\models\my_ssd_resnet50_v1_fpn\ --output_directory .\exported-models\my_model
