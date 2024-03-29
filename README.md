# Coral-Python-API

# Starting by developing Python API demos 
<br>To setup on the USB accelerator, refer to: https://coral.withgoogle.com/docs/accelerator/get-started/
<br>For running the demos, refer to https://coral.withgoogle.com/docs/edgetpu/api-intro/
<br>Two important API's to use: Image Classification and Object Detection
<br>Third API in demos: Imprinting (carries out retraining for "low shot" classes)
<br><br>After installation, the edgetpu files that run the demos and beyond should be located in 
/usr/local/lib/python3.X/dist-packages/edgetpu for linux users
<br>Code for edgetpu has no permission to access thru github, HOWEVER code can be looked at via text files or just going on the "Python API" subsection of the coral site itself. It contains explanations of all of the functions used.

# Image Classification (classify_image.py)
Accesses classification engine to return a label and score of a classification of an image file

# Object Detection (object_detection.py)
Accesses Detection engine to return a list of labels found using a certain model, and a copy of the picture 
with box overlays for the detected objects.

# testing.py
Meant to use object detection on multiple image files in a directory and returning object detection outputs and an image with box overlay. Current state of this file is that it takes an input directory of jpg images, uses the coco database to classify, and returns: <b><br>A copy of the input images with box overlays and a JSON file containing the classifications.</b> 
<br><br>Quick note: JSON printing IN ORDER requires to import the collections package (already handled inside testing.py)
# RUNNING testing.py (sample from terminal)
go to testing.py directory:<br>
<b>$ python3 testing.py --model /home/igolgi/Downloads/edgetpu_files/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite  --inputdir /home/igolgi/snap/skype/common/Downloads/test_images/ --label ~/Downloads/edgetpu_files/coco_labels.txt  --outputdir ~/Downloads/Jasons-downloads/newimages --threshold 0.2 --jsonfile ~/Downloads/Jasons-downloads/newimages  </b>

# Expected inference output from testing.py (sample)
-----------------------------------------
Inference: ---- 0.18507647514343262 seconds ----

Iteration 1
car
score =  0.417969
box =  [298.42809677124023, 25.467658415436745, 350.0341033935547, 51.35906274829591]

Iteration 1
person
score =  0.210938
<p>box =  [216.38036727905273, 20.89538052678108, 275.0260353088379, 79.80286915387425] </p>
-----------------------------------------

Inference: ---- 0.025499582290649414 seconds ----

Iteration 2
.
.
.


# Information on Retraining new models
Ran the image classification and object detection demos with the given information
<br> currently trying to learn how to retrain new models with its customized labels (TPU does NOT handle training according to the site; rather it handles compiling .pb file to a .tflite file)
<br> Currently using https://coral.withgoogle.com/docs/edgetpu/retrain-classification/ for help on retraining. First step is to download "Docker" (done). Now attempting to develop a model that utilizes recognizing flowers.

