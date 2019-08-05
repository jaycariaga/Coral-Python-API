
#object detection starts here:
#
#
#
import timeit
import time
import glob
import argparse
import platform
import subprocess
from edgetpu.detection.engine import DetectionEngine
import re
from edgetpu.classification.engine import ClassificationEngine
from PIL import Image
from PIL import ImageDraw
import json
import collections


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

def getanswer(engine, img, argsthreshold):
  return engine.DetectWithImage(img, threshold=argsthreshold, keep_aspect_ratio=True, relative_coord=False, top_k=100)


def main():

  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--model', help='Path of the detection model.')
  parser.add_argument( '--inputdir', help = "location of the input directory", required = True)
  parser.add_argument( '--outputdir', help = "location of the output directory", required = True)
  parser.add_argument(
      '--label', help='Path of the labels file.')
  parser.add_argument(
      '--input', help='File path of the input image.', )
  parser.add_argument(
      '--output', help='File path of the output image.')
  
  parser.add_argument('--threshold', help='Detection threshold', type=float, required=True)
  args = parser.parse_args()

  filenames = glob.glob(args.inputdir + '*.jpg')
  #print (filenames) to check for successful image response
  filenames.sort() #array of images created in order

  #model and label are created in script below:
  #newmodel = '/home/igolgi/Downloads/edgetpu_files/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite'
  #uselabel = '/home/igolgi/Downloads/edgetpu_files/coco_labels.txt'
  
  if not args.outputdir:
    outputdir = '/home/Downloads/testingoutput'
  else:
    outputdir = args.outputdir

  # Initialize engine.
  engine = DetectionEngine(args.model)
  labels = ReadLabelFile(args.label) if args.label else None

  # Open image.
#?start for loop through directory of images here...?
#
#
#
  output_dict = {}
  for x in range(10):
    output_dict[str(x)] = {}
    output_dict[str(x)]["results"] = {}	
    output_dict[str(x)]["input"] = filenames[x]
    img = Image.open(filenames[x])

  #output_dict["input"] = args.input

  #img = Image.open(args.input)
    draw = ImageDraw.Draw(img)

  # Run inference. (needs timer here)
    #ans = engine.DetectWithImage(img, threshold=args.threshold, keep_aspect_ratio=True, relative_coord=False, top_k=100)
    #time = timeit.timeit(lambda: getanswer(engine, img, args.threshold)) #'from main() import engine, img, args.threshold')
    print ('-----------------------------------------')
    times = time.time()
    ans = getanswer(engine, img, args.threshold)
    print ("Inference: ---- %s seconds ----" % (time.time() - times))
    

    output_dict[str(x)]["results"]["confidence"] = []
    output_dict[str(x)]["results"]["labels"] = [] 
    output_dict[str(x)]["results"]["left"] = [] 
    output_dict[str(x)]["results"]["bottom"] = [] 
    output_dict[str(x)]["results"]["top"] = [] 
    output_dict[str(x)]["results"]["right"] = [] 
    output_dict[str(x)]["results"]["num_contour_points"] = 4 

    totallabels = 0

  # Display result.
    if ans:
      for obj in ans:

        print ('\nIteration ' + str(x+1))
        if labels:
          print(labels[obj.label_id])
        print ('score = ', obj.score)

        output_dict[str(x)]["results"]["labels"].append(labels[obj.label_id])
        output_dict[str(x)]["results"]["confidence"].append(float(obj.score)*100)
      
        totallabels += 1

        box = obj.bounding_box.flatten().tolist()

        output_dict[str(x)]["results"]["left"].append(box[0])
        output_dict[str(x)]["results"]["top"].append(box[1])
        output_dict[str(x)]["results"]["right"].append(box[2])
        output_dict[str(x)]["results"]["bottom"].append(box[3])

        print ('box = ', box)

      # Draw a rectangle.
        draw.rectangle(box, outline='red')
      #saves into output folder
        img.save(outputdir+ '/test_' + str(x) + '.jpg')    
        output_dict[str(x)]["results"]["num_labels_detected"] = str(totallabels)

      #print(output_dict)

      #if platform.machine() == 'x86_64':
      # For gLinux, simply show the image.
      #  img.show()
      #elif platform.machine() == 'armv7l':
      # For Raspberry Pi, you need to install 'feh' to display image.
      #  subprocess.Popen(['feh', output_name])
      #else:
      #  print ('Please check ', output_name)
    else:
      print ('No object detected!')
  print ('-----------------------------------------')
  print ('JSON output:')
  #below handles the JSON print outputs
  #line below prints out the JSON NOT IN ORDER 
  #print(output_dict)
  #below prints it in order inside a JSON but is now a collections object
  orderoutput = collections.OrderedDict(sorted(output_dict.items()))
  print(orderoutput)
  #this one prints in order, however within separate JSON's
  #for x in sorted(output_dict):
  #  print(output_dict[str(x)])

if __name__ == '__main__':
  main()








