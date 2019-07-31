
import glob



#for x in range(100): #goes through certain number of images
filenames = glob.glob('/home/igolgi/snap/skype/common/Downloads/test_images/*.jpg')

#files = glob.glob('./*')

print(len(filenames))

filenames.sort()
print(filenames)

for x in range(101):
  print(filenames[x])
#print(filenames)
#print(files)


