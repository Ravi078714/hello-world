from PIL import Image
import numpy as np
from numpy.core.defchararray import asarray
im = Image.open("/Users/ravikumar/Downloads/Unknown.jpeg")
# print(im.mode)


if(im.size):   
    print("Image succesfully Loaded")
    print("Image size:",im.size)   


# image_sequence = im.getdata()
# image_array = np.array(image_sequence)

pixel_matrix = asarray(im)
print(type(pixel_matrix))
# print(pixel_matrix)
for i in range(len(pixel_matrix)):
    pixel_brightness = [[0 for i in range(len(pixel_matrix[i]))] for j in range(len(pixel_matrix))]

for i in range(len(pixel_matrix)):
    for j in range(len(pixel_matrix[i])):
        # pixel_brightness[i][j] = (int(pixel_matrix[i][j][0]) + int(pixel_matrix[i][j][1]) + int(pixel_matrix[i][j][2]))//3
        pixel_brightness[i][j] = 0.21*int(pixel_matrix[i][j][0]) + 0.72*int(pixel_matrix[i][j][1]) + 0.07*int(pixel_matrix[i][j][2])

# print(len(pixel_brightness))

cha = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# char_repr = [0]*len(pixel_brightness)
for i in range(len(pixel_matrix)):
    char_repr = [[0 for i in range(len(pixel_matrix[i]))] for j in range(len(pixel_matrix))]

for i in range(len(pixel_matrix)):
    for j in range(len(pixel_matrix[i])):
        char_repr[i][j] = (cha[int(pixel_brightness[i][j]/3.93):int(pixel_brightness[i][j]/3.93 +1)])*3

for i in range(len(char_repr)):
    print(*char_repr[i],sep='')

Inversion = input("Do you want to invert the black and white? Y/N: ")

if(Inversion=="Y" or Inversion=="y"):
    for i in range(len(pixel_matrix)):
        for j in range(len(pixel_matrix[i])):
            pixel_brightness[i][j] = 255 - (int(pixel_matrix[i][j][0]) + int(pixel_matrix[i][j][1]) + int(pixel_matrix[i][j][2]))//3

    for i in range(len(pixel_matrix)):
        for j in range(len(pixel_matrix[i])):
            char_repr[i][j] = (cha[int(pixel_brightness[i][j]/3.93):int(pixel_brightness[i][j]/3.93 +1)])*3 

    for i in range(len(char_repr)):
        print(*char_repr[i],sep='')   
else:
    print("Thanks for Using The code :D")    