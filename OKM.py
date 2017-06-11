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



    #! Linear Initialiation
    if (initC == 1):
        print("Linear Init")
        centroids = linearI(k, pix, width, length)
    #! Random Initialization
    elif (initC == 2):
        print("Random Init")
        centroids = randoI(k)
    #! Most Common Colors Initialization
    elif (initC == 3):
        print("Most Common Color Init")
        centroids = colorCount(k, pix, width, length)


    print("* Original Centroids *")
    print(centroids)


    # Membership data for going through OKM
    prevmembership = []
    membership = []
    for x in range(0,width): # initialize previous membership with original data and fake centroid
        for y in range(0,length):
            m1 = x
            m2 = y
            m3 = -1
            m4 = (m1, m2, m3)
            prevmembership.append(m4)

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



# Linear Initialization #
def linearI(k, pix, width, length):
    print("--in linearI")

    centroids = []
    c = 0
    jumpW = int(width / k) - 1
    jumpL = int(length / k ) - 1
    x,y, correction = 0, 0, 0

    # go through making centroids a diagonal line top left to bottom right
    while (c < k):
        l = pix[x,y]

        if l in centroids: # centroid exists, increment to test new value
            c = c
            correction += 1
            x += 1
            y += 1
        else: # add new centroid, set up next x/y, and reset correction
            centroids.append(l)
            print(str(x) + "  " + str(y))
            c += 1
            x += (jumpW - correction)
            y += (jumpL - correction)
            correction = 0


    return(centroids)
# end of linearI #



# Randomizer for Initialization #
def randoI(k):
    print("--in randoI")

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
def randoP(k, pix, width, length):
    print("--in randoP")


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



# Find Greatest Occurring Colors #
def colorCount(k, pix, width, length):
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