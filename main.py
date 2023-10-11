

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


# Press the green button in the gutter to run the script.
