

from PIL import Image
import numpy as np


def CalculateCo_occurrence(image):

   image_array = image
   flattened_image = image_array.flatten()


   # Initialize CoOccurence with zeroes
   rows= 256
   cols = 256
   cooccurrence = [[0 for j in range(cols)] for i in range(rows)]
   num_rows = len(image_array)
   num_cols = len(image_array[0])


   # Fill values of CoOccurence
   for i in range(num_rows-1):
      for j in range(num_cols):
         cooccurrence[image_array[i][j]][image_array[i+1][j]]+=1

   return cooccurrence



def CalculateContrast(CoOccurence):
   c1=0
   c2=0
   # Caculate contrast

   for i in range(len(CoOccurence)):
      for j in range(len(CoOccurence[0])):
            c1+=CoOccurence[i][j]*abs(i-j)
            c2+=abs(i-j)
   return c1/c2

def Gray_scaleTransformation(image,x1,y1,x2,y2):
   # Apply transformation according to values

   for i in range(len(image)):
      for j in range(len(image[0])):
         if(image[i][j]<x1):
            image[i][j] *= y1/x1
         elif(image[i][j]<x2):
            image[i][j] = ((image[i][j]-x1)*((y2-y1)/(x2-x1)))+y1
         else:
            image[i][j] = ((image[i][j]-x2)*((255-y2)/(255-x2)))+y2
   result = Image.fromarray(image)
   result.show()
   return result
#Calculate the histogram 
def CalculateHistogram(image):
  #initialize a 1D array of size 256 pixels (0 up to 255)
  histogram=np.zeros(256) 
  #for each color value you encounter in the image increment its value
  # in the histogram array
  for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
      histogram [image[i][j]]+=1
  return histogram

#Calculate the histogram 
def CalculateCumulativeHistogram(histogram):
  #initialize a 1D array of the same size as the histogram array
  comm_histogram=np.zeros_like(histogram)
  #first color has the same frequency and commulative frequency
  comm_histogram[0]=histogram[0]
  #for each other color add its frequency to the commulative frequency 
  #of the previous color
  for i in range(1,histogram.size):
    comm_histogram[i]=comm_histogram[i-1]+histogram[i]
  return comm_histogram


# Given a certain percentage get the color intensities at
# which the percentage is fulfilled at both ends of the cumulative histogram

def GetColorAtPersentage(comm_histogram,percentage):
  #initialize two variable for the two color intensities left and right
  intensity_left,intensity_right=0,0
  #loop on the commhistogram from the left side to find the color intensity 
  #that fulfills the percentage from the left
  for i in range(0,comm_histogram.size):
    if(comm_histogram[i]/comm_histogram[255]>=percentage):
      intensity_left=i
      break
  #loop on the commhistogram from the right side to find the color intensity 
  #that fulfills the percentage from the right
  for i in range(comm_histogram.size-1,0,-1):
    if(comm_histogram[i]/comm_histogram[255]<=1-percentage):
      intensity_right=i
      break
  return intensity_left,intensity_right



image = Image.open("image2.png").convert('L') #to open the uploaded image and use it
image_as_array=np.asarray(image) #convert the image object into np 2d array
#calculate the histogram of the image
histogram=CalculateHistogram(image_as_array) 
print(histogram)
#check if the sum of the frequencies in the histogram is equal to # of pixels
print(np.sum(histogram)==image_as_array.size)
#calculate the commulative histogram of the image
comm_histogram=CalculateCumulativeHistogram(histogram)
print(comm_histogram)
#check if the commulative frequency at 255 is equal to # of pixels
print(comm_histogram[255]==image_as_array.size)
#calculate the two color intensies at 5% 
intensity_left,intensity_right=GetColorAtPersentage(comm_histogram,0.05)
print(intensity_left,intensity_right)
#check if the commulative frequency of the two intensities fulfill the percentage
print(comm_histogram[intensity_left]/image_as_array.size,comm_histogram[intensity_right]/image_as_array.size)

# Press the green button in the gutter to run the script.
