## Name - Fahia Tabassum
## Your x500

import copy
# Part 1: Inversion
#==========================================
# Purpose:
#   Inverts the colors of an image
# Input Parameter(s):
#   A 3D matrix (list of lists of lists) representing an .bmp image
#   Each element of the matrix represents one row of pixels in the image
#   Each element of a row represents a single pixel in the image
#   Each pixel is represented by a list of three numbers between 0 and 255
#   in the order [blue, green, red]
# Return Value:
#   A 3D matrix of the same dimensions, with all colors inverted
#   (that is, for every value x in the input matrix, the output matrix
#   should have 255-x in that spot).
#==========================================
def invert(img_matrix):
    y = 0
    n = len(img_matrix)
    for y in range(n):
        for x in range(len(img_matrix[y])):
            for z in range(3):
                img_matrix[y][x][z] = 255 - img_matrix[y][x][z]

    print("Not Yet Implemented")
    return img_matrix
    

# Part 2: Grayscale
#==========================================
# Purpose:
#   Converts an image to grayscale
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, where each pixel has all components
#   (red, green, blue) set to the average of the three components in the
#   original pixel, rounded down if necessary
#==========================================
def grayscale(img_matrix):
    n = len(img_matrix)
    for y in range(n):
        for x in range(len(img_matrix[y])):
            a = int((img_matrix[y][x][0]+img_matrix[y][x][1]+img_matrix[y][x][2])/3)
            img_matrix[y][x][0] = a
            img_matrix[y][x][1] = a
            img_matrix[y][x][2] = a
    print("Not Yet Implemented")       
    return img_matrix

    
# Part 3: Rotate 180 degrees
#==========================================
# Purpose:
#   Rotates an image 180 degrees (equivalent to flipping on both axes)
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, rotated 180 degrees.  This means
#   that a pixel at location (x,y) in the original matrix should end up
#   at location (width-x-1,height-y-1) in the output matrix, assuming that
#   we start counting at 0.
#==========================================
def rotate(img_matrix):
    
    new_matrix = copy.deepcopy(img_matrix)
    height = len(img_matrix)
    width = len (img_matrix[0])
    for y in range(len(img_matrix)):
        for x in range(len(img_matrix[y])):
            for z in range(3):
                img_matrix[y][x][z] = new_matrix[height-y-1][width-x-1][z]
    print("Not Yet Implemented")           
    return img_matrix
    


# Part 4: Edge detection
#==========================================
# Purpose:
#   Applies the following edge detection filter to an image:
#       -1 -1 -1
#       -1  8 -1
#       -1 -1 -1
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, with the edge detection filter
#   applied to it (see homework instructions for details).
#==========================================
def edge_detect(img_matrix):
    
    new_matrix = copy.deepcopy(img_matrix)
    for y in range(len(img_matrix)):
        for x in range(len(img_matrix[y])):
            for z in range(3):
                if x ==0 or x == len(img_matrix[y])-1 or y==0 or y == len(img_matrix)-1:
                    new_val = 0
                    img_matrix[y][x][z] = new_val
                else:
                    newval =8*new_matrix[y][x][z]-new_matrix[y-1][x-1][z]-new_matrix[y][x-1][z]-new_matrix[y+1][x-1][z]-new_matrix[y-1][x][z]-new_matrix[y+1][x][z]-new_matrix[y-1][x+1][z]-new_matrix[y][x+1][z]-new_matrix[y+1][x+1][z]
                    if newval>255:
                        newval = 255
                    elif newval < 0:
                        newval = 0
                    img_matrix[y][x][z] = newval                    

    print("Not Yet Implemented")
    return img_matrix

    

# DO NOT EDIT ANYTHING BELOW THIS LINE

# Helper function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Compute the integer represented by a sequence of bytes
# Input Parameter(s):
#   A list of bytes (integers between 0 and 255), in big-endian order
# Return Value:
#   Integer value that the bytes represent
#==========================================
def big_end_to_int(ls):
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

# .bmp conversion function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Turns a .bmp file into a matrix of pixel values, performs an operation
#   on it, and then converts it back into a new .bmp file
# Input Parameter(s):
#   fname, a string representing a file name in the current directory
#   operation, a string representing the operation to be performed on the
#   image.  This can be one of 4 options: 'invert', 'grayscale', 'rotate',
#   or 'edge_detect'.
# Return Value:
#   None
#==========================================

def transform_image(fname,operation):
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [blue,green,red].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i],data[i+1],data[i+2]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()
    new_matrix = matrix

    #Perform operation on the pixel matrix
    if operation == 'invert':
        new_matrix = invert(matrix)
    elif operation == 'grayscale':
        new_matrix = grayscale(matrix)
    elif operation == 'edge_detect':
        new_matrix = edge_detect(matrix)
    elif operation == 'rotate':
        new_matrix = rotate(matrix)
    else:
        return

    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i],data[i+1],data[i+2] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()

