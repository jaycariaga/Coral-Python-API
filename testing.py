
#object detection starts here:
#
#
#


import argparse
import platform
import subprocess
from edgetpu.detection.engine import DetectionEngine
import re
from edgetpu.classification.engine import ClassificationEngine
from PIL import Image
from PIL import ImageDraw
import json


output_dict = {} #declares json

# Function to read labels from text files.
def ReadLabelFile(file_path):
  with open(file_path, 'r', encoding="utf-8") as f:
    lines = f.readlines()
  ret = {}
  for line in lines:
    pair = line.strip().split(maxsplit=1)
    ret[int(pair[0])] = pair[1].strip()
  return ret


def main():
  parser = argparse.ArgumentParser()
  #parser.add_argument(
  #    '--model', help='Path of the detection model.')
  #parser.add_argument(
  #    '--label', help='Path of the labels file.')
  parser.add_argument(
      '--input', help='File path of the input image.', required=True)
  parser.add_argument(
      '--output', help='File path of the output image.')
  
  parser.add_argument('--threshold', help='Detection threshold', type=float, required=True)
  args = parser.parse_args()

  #model and label are created in script below:
  newmodel = '/home/igolgi/Downloads/edgetpu_files/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite'
  uselabel = '/home/igolgi/Downloads/edgetpu_files/coco_labels.txt'
  
  if not args.output:
    output_name = 'object_detection_result.jpg'
  else:
    output_name = args.output

  # Initialize engine.
  engine = DetectionEngine(newmodel)
  labels = ReadLabelFile(uselabel) if uselabel else None

  # Open image.
  output_dict["input"] = args.input
  output_dict["results"] = {}

  img = Image.open(args.input)
  draw = ImageDraw.Draw(img)

  # Run inference.
  ans = engine.DetectWithImage(img, threshold=args.threshold, keep_aspect_ratio=True,
                               relative_coord=False, top_k=100)

  output_dict["results"]["confidence"] = []
  output_dict["results"]["labels"] = [] 
  output_dict["results"]["left"] = [] 
  output_dict["results"]["bottom"] = [] 
  output_dict["results"]["top"] = [] 
  output_dict["results"]["right"] = [] 
  output_dict["results"]["num_contour_points"] = 4 

  totallabels = 0

  # Display result.
  if ans:
    for obj in ans:
      print ('-----------------------------------------')
      if labels:
        print(labels[obj.label_id])
      print ('score = ', obj.score)

      output_dict["results"]["labels"].append(labels[obj.label_id])
      output_dict["results"]["confidence"].append(float(obj.score)*100)
      
      totallabels += 1

      box = obj.bounding_box.flatten().tolist()

      output_dict["results"]["left"].append(box[0])
      output_dict["results"]["top"].append(box[1])
      output_dict["results"]["right"].append(box[2])
      output_dict["results"]["bottom"].append(box[3])

      print ('box = ', box)
      # Draw a rectangle.
      draw.rectangle(box, outline='red')
    img.save(output_name)
    
    output_dict["results"]["num_labels_detected"] = str(totallabels)
    print(output_dict)

    if platform.machine() == 'x86_64':
      # For gLinux, simply show the image.
      img.show()
    elif platform.machine() == 'armv7l':
      # For Raspberry Pi, you need to install 'feh' to display image.
      subprocess.Popen(['feh', output_name])
    else:
      print ('Please check ', output_name)
  else:
    print ('No object detected!')

if __name__ == '__main__':
  main()







