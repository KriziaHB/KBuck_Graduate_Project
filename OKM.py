# Student: Krizia Houston Buck
# Faculty: Dr. Emre Celebi
# University of Central Arkansas
# Summer 2017
# Graduate Project
# OKM.py (Online K-Means file)

# PIL for manipulating images
import PIL
from PIL import Image
from collections import Counter # ** currently not in use
from random import randint



# Online K-Means, call functions from here #
def kmeans(k, im, pix, initC, psC, LR):
    print("--in kmeans")
    end = 0

    width = int(im.size[0])
    length = int(im.size[1])


##****** COME BACK to Linear
    # Linear Initialiation
    if (initC == 1):
        print("Linear Init")
    #! Random Initialization
    elif (initC == 2):
        print("Random Init")
        centroids = randoI(k)
    #! Most Common Colors Initialization
    elif (initC == 3):
        print("Most Common Color Init")
        centroids = colorCount(k, width, length, pix)


    print("* Original Centroids *")
    print(centroids)



## ** FIGURE OUT K-MEANS HERE

    # iterate through pixels to form clusters
    while (end < 2):
        print("while")
        end += 1
## **

    # return to main
    # out = should be equal to whatever results from completed iterations, for now testing with out from colorCount
    return(im)
# end of kmeans #



# Check Termination Criteria to see if met #
def term():
    print("--in term")
# end of term #



# Randomizer for Initialization #
def randoI(k):
    print("--in rando")

    count = 0
    centroids = []

    # go through until all centroid spots are filled with a unique color
    while (count < k):

        r1 = randint(0, 255)
        r2 = randint(0, 255)
        r3 = randint(0, 255)
        r = (r1, r2, r3)
        # print(r)

        # if current random color is not a centroid, add it, or else repeat until unique
        if r in centroids:
            count = count
        else:
            centroids.append(r)
            count += 1

    return(centroids)
# end of randoI #



# Randomizer for Presentation Style #
def randoP(k, width, length, pix):
    print("--in rando")


    #return(random)
# end of randoP #



# K Nearest Neighbor - find nearest centroid to current pixel #
def knn():
    print("--in knn")
# end of knn #



# Update the Nearest Center (centroid) #
def upC():
    print("--in upC")
# end of upC #



# Find Greatest Occurring Colors # ***** using for testing ******
def colorCount(k, width, length, pix):
    print("--in colorCount - k = " + str(k))


    # List for all pixels for counting
    pixList = []

    for x in range(0,width):
        for y in range(0,length):
            pixList.append(pix[x,y])
  #  print(pixList)
    cen = Counter(pixList).most_common(k)
    print(cen)

    # After count is complete, only keep the pixel data (not the number of times it appears)
    centroids = []
    for element in cen:
        centroids.append(element[0])
    # centroids is a list of tuples containing ints
    # replace individual centroids by assigning a new tuple to that centroid index


 #   print(type(centroids)) #list
 #   print(type(centroids[2])) #tuple
 #   c = centroids[0]
 #   print(type(c[2])) #int

    # c = centroids[0]
    # print(c)
    # d = (12, 12, 12)
    # centroids[0] = d
    # print(centroids)


    return(centroids)
# end of colorCount #


## end of OKM.py ##




#### HELPFUL INFO FOR PILLOW ####

# http://pillow.readthedocs.io/en/3.0.x/reference/PixelAccess.html