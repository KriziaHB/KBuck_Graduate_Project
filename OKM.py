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

    # Variables to be used throughout
    width = int(im.size[0])
    length = int(im.size[1])
    print("width: " + str(width) + " -- length: " + str(length) + " -- k: " + str(k))
    centroids = []
    clustersize = []
    for i in range(0,k):
        clustersize.append(0)


# Initializations
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
    # Maximin Initialization #
    elif (initC == 4):
        print("Maximin Initialization")
        centroids = maximin(k, pix, width, length)


    print("* Original Centroids *")
    for i in centroids:
        i.printRGB()
    previous_centroids = copy.deepcopy(centroids)
# end Initializations


    # Membership data for going through OKM
# DO NOT NEED previous_membership when using number of iterations as sole convergence type
    previous_membership = []
    membership = []
    for i in range(0,length*width): # initialize previous membership with original data and fake centroid
        membership.append(0)
        previous_membership.append(0)


## **  K-MEANS HERE via two different Presentation Styles ** ##
    # Random Presentation Style - OKM runs from a different method entirely
    if (psC == 2):
        pix = randoP(k, pix, width, length, centroids, previous_centroids, membership, previous_membership, clustersize, LR)
    # Linear Presentation Style - OKM runs here
    else:
        pix = linearP(k, pix, width, length, centroids, previous_centroids, membership, previous_membership, clustersize, LR)
## ** end of K-MEANS ** ##


    # Use cluster data to make new image
    pix = newImage(k, pix, centroids, membership, width, length)


    # return to main with final image
    return(im)
# end of kmeans #


##################### Not Using, Set number of iterations instead to keep all versions to equal number of runs
# Check Termination Criteria to see if met #
def term(k, oldCent, newCent):
    print("--in term")

    # termination value (if small, then convergence is reached)
    sum = 0.0

    # go through all centroids comparing them to what they used to be using Euclidean distance
    for i in range(0,k):
        old = oldCent[i]
        updated = newCent[i]
        r = (old.r - updated.r) * (old.r - updated.r)
        g = (old.g - updated.g) * (old.g - updated.g)
        b = (old.b - updated.b) * (old.b - updated.b)
        euclidean = math.sqrt(r + g + b) # REMOVE SQRT
        sum += euclidean

    t = float(sum / k)
    print("t: " + str(t))

    return(t)
# end of term #



# Linear Initialization #
def linearI(k, pix, width, length):
    print("--in linearI")

    # Count, jump, coordinate, and corrector variables
    c = 0
    jumpW = int(width / k) #- 1
    jumpL = int(length / k ) #- 1
    x, y, correction = 0, 0, 0
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
            # print(str(x) + "  ___  " + str(y))
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

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        rgb = (r, g, b)
        c = ColorPixel(rgb)
      #  r = (r1, r2, r3)
        # print(r)

        # if current random color is not a centroid, add it, or else repeat until unique
        if c not in centroids:
            centroids.append(c)
            count += 1


    return(centroids)
# end of randoI #



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



# Maximin Initialization #
def maximin(k, pix, width, length):
    print("--in maximin")
    centroids = []
    # List for all pixels for counting
    pixList = []
    # List for all centroid indices for use with matrix
    centroidIndices = []


    # narrow down to only colors in the image
    for y in range(0, length):
        for x in range(0, width):
            p = pix[x,y]
            element = (p[0], p[1], p[2])
            pixList.append(element)

    # first centroid
    cen1 = Counter(pixList).most_common(1) # list
    cen1toRGB = cen1[0] # tuple with color count
    c = cen1toRGB[0] # tuple of RGB
    pixel = ColorPixel(c)
    centroids.append(pixel)

    # remove duplicate colors
    colors = list(set(pixList))
    centroidIndices.append(colors.index(c)) # index of first centroid in color list
    colorLen = len(colors)
    print("Number of colors present: " + str(colorLen))



    # set up and find distances to build up distance matrix
    matrix = [[0] * colorLen for l in range(colorLen)]
    for x in range(0,colorLen):
        i = colors[x]
        for y in range(0,colorLen):
            if (x == y):
                break
            j = colors[y]
            r = (i[0]- j[0]) * (i[0]- j[0])
            g = (i[1] - j[1]) * (i[1] - j[1])
            b = (i[2] - j[2]) * (i[2] - j[2])
            dist = r + g + b # REMOVED SQRT
            matrix[x][y] = dist
           # matrix[y][x] = dist

    total = 0
    # all remaining centroids
    while (total < k-1):
        i = 0
        dist = []
        distIndex = []  # y index for found minimum distance to a centroid


        # use distance matrix to calculate best new centroid to append
        for y in range(0,colorLen):
            while (i < len(centroids)):
                minDist =  195075 # minimum distance from centroid (start with 255^2 + 255^2 + 255^2)
                x = centroidIndices[i]
                # make sure not already a centroid
                if (y not in centroidIndices):
                    # swap minimum distance if it is less than to this centroid
                    if (minDist > matrix[x][y]):
                        minDist = matrix[x][y]
                        index = y
                # repeat
                i += 1
            # end inner while loop

            # add to distances list for check on minimum along with parallel of its index
            dist.append(minDist)
            distIndex.append(index)
            i = 0
        # end for loop

        # color furthest away becomes a centroid
        furthest = max(dist)  # int
        location = dist.index(furthest)  # index within dist
        yVal = distIndex[location]  # index within matrix
        p = ColorPixel(colors[yVal])  # color at index changed to ColorPixel
        centroids.append(p)
        centroidIndices.append(yVal)
        #print(dist)
        #print(distIndex)
        #print(colors[yVal])

        # repeat
        total += 1
    # end of all loops

    # return the intialized k centroids
    return(centroids)
# end of maximin #



# OKM with Random Points for Presentation Style #
def randoP(k, pix, width, length, centroids, previous_centroids, membership, previous_membership, clustersize, LR):
    print("--in randoP")

    # will be 0 when an unused pixel is found
    cont = 1
    end = 0
    max = (width * length) - 1

    while (cont == 1):

        # Find random number to generate pixel location
        random = randint(0, max)
        mod = divmod(random, width)
        pixel = ColorPixel(pix[mod[1], mod[0]])

        # find the index of nearest centroid to current pixel and update membership
        m = knn(k, pixel, centroids)

        # update the size of the current cluster and new cluster
        if (membership[random] != m):
            clustersize[m] += 1
            if (clustersize[membership[random]] > 0):
                clustersize[membership[random]] -= 1
        membership[random] = m

        # update the nearest center
        centroids[m] = centroids[m].upC(pixel, LR, clustersize[m])

        # End the algorithm after 50 full runs
        if (end == (max * 10)):
            print("Ten runs")
        elif(end == (max * 20)):
            print("Twenty runs")
        elif (end == (max * 30)):
            print("Thirty runs")
        elif (end == (max * 40)):
            print("Forty runs")
        elif (end == (max*50)):
            print("Fifty runs")
            cont = 0
        end += 1
    # end of while


    return(pix)
# end of randoP #



# OKM with Linear Points for Presentation Style #
def linearP(k, pix, width, length, centroids, previous_centroids, membership, previous_membership, clustersize, LR):
    # iterate through pixels to form clusters
    end = 0
    # t = 100.0
    while (end < 50):  # !! if you change end value here, then also change in randoP
        if ((end % 10) == 0):
            print("while: " + str(end))

        # Check through all points each while iteration
        for y in range(0, length):
            for x in range(0, width):
                # Linear Presentation Style
                pixel = ColorPixel(pix[x, y])

                # find the index of nearest centroid to current pixel and update membership
                m = knn(k, pixel, centroids)
                index = (y * width) + x

                # update the size of the current cluster
                if (membership[index] != m):
                    clustersize[m] += 1
                    if (clustersize[membership[index]] > 0):
                        clustersize[membership[index]] -= 1
                membership[index] = m

                # update the nearest center
                centroids[m] = centroids[m].upC(pixel, LR, clustersize[m])
        # end of for loops
        end += 1

        # # check for convergence of centroids
        # T = term(k, previous_centroids, centroids)
        # if (previous_membership == membership):
        #     # if (t == T or set(previous_membership) == set(membership)):
        #     break
        # else:
        #     t = copy.deepcopy(T)
        #
        # # Reset old centroids
        # previous_centroids = copy.deepcopy(centroids)
        # # Reset old membership
        # previous_membership = copyOver(membership)
    # end of while loop

    print("Iterations: " + str(end))
    return(pix)
# end of linearP #



# K Nearest Neighbor - find nearest centroid to current pixel #
def knn(k, pixel, centroids):
    #print("--in knn")

    distances = []

    # find distance from current pixel to each centroid and select the closest one
    for i in range(0,k):
        cent = centroids[i]
        distR = pixel.r - cent.r
        distG = pixel.g - cent.g
        distB = pixel.b - cent.b

        d = (distR * distR) + (distG * distG) + (distB * distB) # removed sqrt
        distances.append(d)
  ####!! COME BACK CHECK IF KEEPING TRACK OF MIN IS FASTER, remove some variables to simplify

    centroidIndex = distances.index(min(distances))

    return(centroidIndex)
# end of knn #



# Create New Image to be Printed as Output #
def newImage(k, pix, centroids, membership, width, length):
    print("--in newImage")
    print("* Final Centroids *")

    # round centroids to ints for quantization
    for i in range(0,k):
        a = centroids[i]
        centroids[i] = ColorPixel((int(a.r), int(a.g), int(a.b)))
        centroids[i].printRGB()


    # replace pixels with their cluster's centroid
    for y in range(0,length):
        for x in range(0,width):
            # compensating for flattened membership list
            # selecting current pixel membership cluster
            cluster = membership[(y * width) + x ]
            # replace original color with centroid color value not in ColorPixel form
            pix[x, y] = (centroids[cluster].r, centroids[cluster].g, centroids[cluster].b)

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