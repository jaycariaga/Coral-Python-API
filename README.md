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

# Exercises (testing.py)
Trying to 



# Current Progress
Ran the image classification and object detection demos with the given information
<br> currently trying to learn how to retrain new models with its customized labels (TPU does NOT handle training according to the site; rather it handles compiling .pb file to a .tflite file)
<br> Currently using https://coral.withgoogle.com/docs/edgetpu/retrain-classification/ for help on retraining. First step is to download "Docker" (done). Now attempting to develop a model that utilizes recognizing flowers.

