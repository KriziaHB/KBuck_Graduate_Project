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
import math
from ColorPixel import ColorPixel # ColorPixel.py
import copy




# Online K-Means, call functions from here #
def kmeans(k, im, pix, initC, psC, LR):
    print("--in kmeans")
    end = 0
    t = 1.0

    width = int(im.size[0])
    length = int(im.size[1])
    print("width: " + str(width) + " -- length: " + str(length))
    centroids = []


    #! Linear Initialization
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
    for i in centroids:
        i.printRGB()
    previousCentroids = copy.deepcopy(centroids)


    # Membership data for going through OKM
    previous_membership = []
    membership = []
    for i in range(0,length*width): # initialize previous membership with original data and fake centroid
        membership.append(0)
        previous_membership.append(0)

    # Extra list for Random Presentation Style to keep track of if the pixel has been used
    if (psC == 2):
        presentation = []
        for i in range(0,length*width):
            presentation.append(0)



        ## **  K-MEANS HERE  ** ##
    # iterate through pixels to form clusters
    t = 100.0
    while (t > 5.0 and end < 10):
        print("while: " + str(end))

        # Check through all points each while iteration
        for y in range(0, length):
            for x in range(0, width):
                #! Presentation Style
                if (psC == 1): # Linear
                    pixel = ColorPixel(pix[x,y])
                else: # Random
                    pi = randoP(k, pix, width, length, presentation)
                    # claim RGB
                    piToRGB = (pi[0], pi[1], pi[2])
                    pixel = ColorPixel(piToRGB)
                    # update that this pixel was seen
                    presentation[(pi[4]*width) + pi[3]] = 1
                # find the index of nearest centroid to current pixel and update membership
                m = knn(k, pixel, centroids)
                index = (y*width) + x
                membership[index] = m
                # update the nearest center
                centroids[m] = centroids[m].upC(pixel, LR)
        # end of for loops

        end += 1
        # check for convergence of centroids
        T = term(k, previousCentroids, centroids)
        if (previous_membership == membership):
        #if (t == T or set(previous_membership) == set(membership)):
            break
        else:
            t = copy.deepcopy(T)

        # Reset old centroids
        previousCentroids = copy.deepcopy(centroids)
        # Reset old membership
        previous_membership = copyOver(membership) ##Untested!!!!!!!!!!!

        # Extra list for Random Presentation Style to keep track of if the pixel has been used
        if (psC == 2):
            for i in range(0, length * width):
                presentation[i] = 0
    # end of while loop
## ** end of K-MEANS ** ##

    # Use cluster data to make new image
    pix = newImage(k, pix, centroids, membership, width, length)
    print("Iterations: " + str(end))

    # return to main with final image
    return(im)
# end of kmeans #


##################### UNTESTED
# Check Termination Criteria to see if met #
def term(k, oldCent, newCent):
    print("--in term")

    # termination value (if small, then convergence is reached)
    sum = 0.0

    # go through all centroids comparing them to what they used to be using Euclidean distance
    for i in range(0,k):
        old = oldCent[i]
        updated = newCent[i]
        r = pow((old.r - updated.r),2)
        g = pow((old.g - updated.g),2)
        b = pow((old.b - updated.b),2)
        euclidean = math.sqrt(r + g + b)
        sum += euclidean

    t = float(sum / k)
    print("t: " + str(t))

    return(t)
# end of term #



# Linear Initialization #
def linearI(k, pix, width, length):
    print("--in linearI")


    c = 0
    jumpW = int(width / k) - 1
    jumpL = int(length / k ) - 1
    x,y, correction = 0, 0, 0
    centroids = []

    # go through making centroids a diagonal line top left to bottom right
    while (c < k):
        l = pix[x,y]

        if l in centroids: # centroid exists, increment to test new value
            correction += 1
            x += 1
            y += 1
        else: # add new centroid, set up next x/y, and reset correction
            cent = ColorPixel(l)
            centroids.append(cent)
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
        rgb = (r1, r2, r3)
        c = ColorPixel(rgb)
      #  r = (r1, r2, r3)
        # print(r)

        # if current random color is not a centroid, add it, or else repeat until unique
        if c in centroids:
            count = count
        else:
            centroids.append(c)
            count += 1

    return(centroids)
# end of randoI #



# Randomizer for Presentation Style #
def randoP(k, pix, width, length, presentation):
    print("--in randoP")

    # will be 0 when an unused pixel is found
    cont = 1

    while (cont == 1):
        x = randint(0, width-1)
        y = randint(0, length-1)

        # find unused pixels for this iteration
        if (presentation[(y*width) + x] == 0):
            pixel = ColorPixel(pix[x, y])
            r = pixel.r
            g = pixel.g
            b = pixel.b
            cont = 0
            print("x: " + str(x) + " y: " + str(y))
    # end of while


    random = (r, g, b, x, y)
    return(random)
# end of randoP #



# K Nearest Neighbor - find nearest centroid to current pixel #
def knn(k, pixel, centroids):
    #print("--in knn")

    distances = []

    r = pixel.r
    g = pixel.g
    b = pixel.b

    # find distance from current pixel to each centroid and select the closest one
    for i in range(0,k):
        cent = centroids[i]
        cr = cent.r
        cg = cent.g
        cb = cent.b

        d = math.sqrt(pow((r - cr), 2) + pow((g - cg), 2) + pow((b - cb), 2))
        distances.append(d)
        if (distances[i] == 0.0):
            return(i)

    centroidIndex = distances.index(min(distances))

    return(centroidIndex)

# end of knn #



# Update the Nearest Center (centroid) #
def upC(pixel, oldCentroid, LR):
    #print("--in upC")


    r = float((pixel.r + oldCentroid.r)/2)
    g = float((pixel.g + oldCentroid.g)/2)
    b = float((pixel.b + oldCentroid.b)/2)


    # # Learning Rate of (1/(1+t))
    # if (LR == 1):
    #     r = 0
    #     g = 0
    #     b = 0
    #
    # # Learning Rate of sqrt(1/(1+t))
    # else:
    #     r = 0
    #     g = 0
    #     b = 0


    # updated centroid
    c = oldCentroid.insertRGB(r, g, b)
    print(type(c))
    return(c)
# end of upC #



# Find Greatest Occurring Colors #
def colorCount(k, pix, width, length):
    print("--in colorCount - k = " + str(k))


    # List for all pixels for counting
    pixList = []

    for y in range(0,length):
        for x in range(0,width):
            pixList.append(pix[x,y])
  #  print(pixList)
    cen = Counter(pixList).most_common(k)
    print(cen)

    # After count is complete, only keep the pixel data (not the number of times it appears)
    centroids = []
    for element in cen:
        centroids.append(ColorPixel(element[0]))
    # centroids is a list of tuples containing ints
    # replace individual centroids by assigning a new tuple to that centroid index


    return(centroids)
# end of colorCount #


################ UNTESTED
# Create New Image to be Printed as Output #
def newImage(k, pix, centroids, membership, width, length):
    print("--in newImage")

    # round centroids to ints for quantization
    for i in range(0,k):
        a = centroids[i]
        r = int(a.r)
        g = int(a.g)
        b = int(a.b)
        rgb = (r, g, b)
        centroids[i] = ColorPixel(rgb)


    # replace pixels with their cluster's centroid
    for y in range(0,length):
        for x in range(0,width):
            index = (y * width) + x # compensating for flattened membership list
            cluster = membership[index] # selecting current pixel membership cluster
            R = centroids[cluster].r
            G = centroids[cluster].g
            B = centroids[cluster].b
            pix[x,y] = (R, G, B)  # replace original color with centroid color value not in ColorPixel form

    return(pix)
# end of newImage #



# Replace Membership value of pixel #
def copyOver(m):
    #print("--in copyOver")

    pm = []

    for i in m:
        pm.append(i)

    return(pm)
# end of copyOver #


## end of OKM.py ##






#### HELPFUL INFO FOR PILLOW ####

# http://pillow.readthedocs.io/en/3.0.x/reference/PixelAccess.html