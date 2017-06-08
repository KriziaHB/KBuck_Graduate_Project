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
        out = colorCount(k, im, pix)
# ** CALL COUNTCOLOR FOR TESTING






## ** FIGURE OUT K-MEANS HERE

    # iterate through pixels to form clusters
    while (end < 2):
        print("while")
        end += 1

    # return to main
    # out = should be equal to whatever results from completed iterations, for now testing with out from colorCount
    return(out)
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

    # proves that each pixel color is tallied separately as r, g, and b not as an rgb combo
    hist = im.histogram()
    print(sum(hist))

    # experiment with splitting for counting
    r, g, b = im.split()
    rHist = r.histogram()
    print("R: ")
    print(rHist)
    gHist = g.histogram()
    print("G: ")
    print(gHist)
    bHist = b.histogram()
    print("B: ")
    print(bHist)
    #print(Counter(r).most_common(k))







    # built in PIL quantization (use for comparison)
    out = im.quantize(k)
    out.show()
    return(out)
# end of colorCount #


## end of OKM.py ##




#### HELPFUL INFO FOR PILLOW ####

# http://pillow.readthedocs.io/en/3.0.x/reference/PixelAccess.html