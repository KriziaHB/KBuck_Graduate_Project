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



# Online K-Means, call functions from here #
def kmeans(k, im, pix, initC, psC, LR):
    print("in kmeans")
    end = 0


##****** COME BACK
    # Linear Initialiation
    if (initC == 1):
        print("Linear Init")
    # Random Initialization
    elif (initC == 2):
        print("Random Init")
        rando(k, im, pix)
    # Most Common Colors Initialization
    elif (initC == 3):
        print("Most Common Color Init")
        centroids = colorCount(k, im, pix)
# ** CALL COUNTCOLOR FOR TESTING


    print(centroids)



## ** FIGURE OUT K-MEANS HERE

    # iterate through pixels to form clusters
    while (end < 2):
        print("while")
        end += 1

    # return to main
    # out = should be equal to whatever results from completed iterations, for now testing with out from colorCount
    return(im)
# end of kmeans #



# Check Termination Criteria to see if met #
def term():
    print("in term")
# end of term #



# Randomizer for Initialization and Presentation Style #
def rando(k, im, pix):
    print("in rando")
# end of rando #



# K Nearest Neighbor - find nearest centroid to current pixel #
def knn():
    print("in knn")
# end of knn #



# Update the Nearest Center (centroid) #
def upC():
    print("in upC")
# end of upC #



# Find Greatest Occurring Colors # ***** using for testing ******
def colorCount(k, im, pix):
    print("in colorCount - k = " + str(k))


    # print(Counter(r).most_common(k))
  #  rpix = r.getpixel((0,5))

    # HOW TO CHANGE PIXELS
    # rint = 200
    # test = im.load()
    # for x in range(0,750):
    #     for y in range(0,1334):
    #         test[x,y] = (rint, rint, rint)
    # im.show()

    # List for all pixels for counting
    pixList = []

    for x in range(0,750):
        for y in range(0,1334):
            pixList.append(pix[x,y])
    print(pixList)
    print(len(pixList))
    cen = Counter(pixList).most_common(k)
    print(cen)

    centroids = []
    for element in cen:
        centroids.append(element[0])
    print(centroids)
    print(type(centroids)) #list
    print(type(centroids[2])) #tuple
    c = centroids[2]
    print(c[0])
    print(c[1])
    print(c[2])
    print(type(c[2])) #int


    return(centroids)
# end of colorCount #


## end of OKM.py ##




#### HELPFUL INFO FOR PILLOW ####

# http://pillow.readthedocs.io/en/3.0.x/reference/PixelAccess.html