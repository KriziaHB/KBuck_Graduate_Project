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
import time




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
    start = time.time()
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
    end = time.time()
    elapsed = end - start
    print("Initialization Time: " + str(elapsed))


    print("* Original Centroids *")
    for i in centroids:
        i.printRGB()
# end Initializations


    # Membership data for going through OKM
    membership = []
    for i in range(0,length*width):
        membership.append(0)


## **  K-MEANS HERE via two different Presentation Styles ** ##
    start = time.time()
    # end value for how many times it iterates through pixel set
    t = 20
    # number to add to skips in order to not test so many pixels
    reduction = 1
    # Random Presentation Style - OKM runs from a different method entirely
    if (psC == 2):
        p = randoP(k, pix, width, length, centroids, membership, clustersize, LR, t, reduction)
    # Linear Presentation Style - OKM runs here
    else:
        p = linearP(k, pix, width, length, centroids, membership, clustersize, LR, t, reduction)
    end = time.time()
    elapsed = end - start
    print("K-Means Time: " + str(elapsed))
## ** end of K-MEANS ** ##

    # pix info is first part of what was returned, SSE/MSE/MAE is second part of what was returned
    pix = p[0]
    out = (im, p[1])
    # return to main with final image
    return(out)
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
    # removing duplicates did not speed up the algorithm
   # colors = []


    # narrow down to only colors in the image
    for y in range(0, length):
        for x in range(0, width):
            p = pix[x,y]
            element = (p[0], p[1], p[2])
            pixList.append(element)
     #       colors.append(element)

    # first centroid
    # print(Counter(pixList).most_common())
    cen1 = Counter(pixList).most_common(1) # list
#    cen1 = Counter(colors).most_common(1)
    cen1toRGB = cen1[0] # tuple with color count
    c = cen1toRGB[0] # tuple of RGB
    centroids.append(c)

    # remove duplicate colors
    colors = list(set(pixList))
    colorLen = len(colors)
    print("Number of colors present: " + str(colorLen))



    total = 0
    distances = []  # all minimum distances from y values to a centroid
    closestCentroids = [] # keep track of the closest Centroid in order to avoid calculating each again

    # all remaining centroids
    while (total < k-1):


        # most centroids
        if (len(centroids) > 1):
            # newest centroid next
            # go through all y to each centroid including the newest one
            for y in range(0, colorLen):
                if (colors[y] not in centroids):
                    # x is the closest centroid to y
                    x = closestCentroids[y]
                    minDist = tupDistance(centroids[x], colors[y])
                    # distance to the newest centroid
                    d = tupDistance(centroids[xVal], colors[y])
                    # replace minimum distance if it is less than to this centroid
                    if (minDist > d):
                        minDist = d
                        closestCen = xVal
                    else:
                        closestCen = x
                # add to distances list for check on minimum
                distances[y] = minDist
                closestCentroids[y] = closestCen
        # end if
        else: # get second centroid
            distances = []

            # newest centroid next
            # go through all y to each centroid including the newest one
            for y in range(0,colorLen):
                # distance to the original centroid
                d = tupDistance(centroids[0], colors[y])


                # add to distances list for check on maximum
                distances.append(d)
                closestCentroids.append(0)
        # end else


        # color furthest away becomes a centroid
        furthestDistance = max(distances)  # maximum of minimum distances from centroid to color
        locationInDistances = distances.index(furthestDistance)  # index within dist of maximum distance
        centroids.append(colors[locationInDistances])
        xVal = len(centroids) - 1


        # repeat
        total += 1
    # end of all loops

    # convert to ColorPixel
    CPcentroids = []
    for i in range(0, k):
        CPcentroids.append(ColorPixel(centroids[i]))

    # return the initialized k centroids
    return(CPcentroids)
# end of maximin #



# distance between two point tuples #
def tupDistance(a, b):
    R = (a[0] - b[0]) * (a[0] - b[0])
    G = (a[1] - b[1]) * (a[1] - b[1])
    B = (a[2] - b[2]) * (a[2] - b[2])
    c = R + G + B  # REMOVED SQRT

    return(c)
# end of tupDistance #



# OKM with Random Points for Presentation Style #
def randoP(k, pix, width, length, centroids, membership, clustersize, LR, term, reduction):
    print("--in randoP")

    # will be 0 when an unused pixel is found
    cont = 1
    end = 0
    max = (width * length) - 1
    endingcount = term / reduction

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
        if (end == (max * endingcount)):
            cont = 0
        elif (end == (max * 10)):
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



    # for all pixels, assign a final membership without updating centroids
    for y in range(0, length):
        for x in range(0, width):
            pixel = ColorPixel(pix[x, y])
            m = knn(k, pixel, centroids)
            index = (y * width) + x
            membership[index] = m

    # find the SSE
    s = sse(k, pix, membership, centroids, length, width)

    # Use cluster data to make new image
    p = newImage(k, pix, centroids, membership, width, length)

    # output with sse and new pix data
    out = (p, s)
    return(out)
# end of randoP #



# OKM with Linear Points for Presentation Style #
def linearP(k, pix, width, length, centroids, membership, clustersize, LR, term, reduction):
    # iterate through pixels to form clusters
    end = 0

    while (end < term):
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

        ######### skip columns and rows to reduce the number of pixels checked and used #########
                x += reduction
            y += reduction
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


    # for all pixels, assign a final membership without updating centroids
    for y in range(0, length):
        for x in range(0, width):
            pixel = ColorPixel(pix[x,y])
            m = knn(k, pixel, centroids)
            index = (y * width) + x
            membership[index] = m

    print("Iterations: " + str(end))


    # find the SSE
    s = sse(k, pix, membership, centroids, length, width)

    # Use cluster data to make new image
    p = newImage(k, pix, centroids, membership, width, length)

    # output with sse and new pix data
    out = (p, s)
    return (out)
# end of linearP #



# K Nearest Neighbor - find nearest centroid to current pixel #
def knn(k, pixel, centroids):
    #print("--in knn")

    # to keep track of minimum in order to capture the closest centroid
    distances = []
    min = 255 * 255 * 255
    index = 0

    # find distance from current pixel to each centroid and select the closest one
    for i in range(0,k):
        cent = centroids[i]
        distR = pixel.r - cent.r
        distG = pixel.g - cent.g
        distB = pixel.b - cent.b

        d = (distR * distR) + (distG * distG) + (distB * distB) # removed sqrt
   #     distances.append(d)
  ## Keeping track of min is slightly faster
        if (d < min):
            min = d
            index = i

#    centroidIndex = distances.index(min(distances))

 #   return(centroidIndex)
    return(index)
# end of knn #



# Create New Image to be Printed as Output #
def newImage(k, pix, centroids, membership, width, length):
    print("--in newImage")
    print("* Final Centroids *")
    for i in range(0,k):
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



# Sum of Square Error, Mean Squared Error, and Mean Absolute Error #
def sse(k, pix, membership, centroids, length, width):
    s = 0
    m = 0

    # round centroids to ints for quantization
    for i in range(0,k):
        a = centroids[i]
        centroids[i] = ColorPixel((int(a.r), int(a.g), int(a.b)))

    # calculate SSE by adding up all distances (each point to its cluster centroid)
    for y in range(0,length):
        for x in range(0,width):
            # compensating for flattened membership list
            # selecting current pixel membership cluster
            cluster = membership[(y * width) + x ]
            # find distance between the two
            b = (centroids[cluster].r, centroids[cluster].g, centroids[cluster].b)
            d2 = tupDistance(pix[x, y], b)
            # square the distance
            s += (d2 * d2)
            # add the absolute distance
            m += math.fabs(d2)


    # mean squared error
    mse = s / (length * width)
    # mean absolute error
    mae = m / (length * width)

    # Tuple to return
    out = (s, mse, mae)

    print("SSE: " + str(s))
    print("MSE: " + str(mse))
    print("MAE: " + str(mae))
    return(out)
# end of sse #



## end of OKM.py ##






#### HELPFUL INFO FOR PILLOW ####

# http://pillow.readthedocs.io/en/3.0.x/reference/PixelAccess.html