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

    # ** CALL COUNTCOLOR FOR TESTING
    colorCount(k, im, pix)


    # iterate through pixels to form clusters
    while (end < 5):
        print("while")
        end += 1

    # return to main
    out = 0
    return(out)
# end of kmeans #



# Check Termination Criteria to see if met #
def term():
    print("in term")
# end of term #



# Randomizer for Initialization and Presentation Style #
def rando():
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
    print("in colorCount")


# end of colorCount #







#### HELPFUL INFO FOR PILLOW ####

# http://pillow.readthedocs.io/en/3.0.x/reference/PixelAccess.html