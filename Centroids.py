# Student: Krizia Houston Buck
# Faculty: Dr. Emre Celebi
# University of Central Arkansas
# Summer 2017
# Graduate Project
# OKM.py (Online K-Means file)

# PIL for manipulating images
import PIL
from PIL import Image

# ******* maybe try making a Color class with RGB then use inheritance for Centroids and Pixels (have a location too)

class Centroids(object):

    centroids = []
    r = 0.0
    g = 0.0
    b = 0.0

    def __init__(self, cents):
        super(Centroids, self).__init__()
        self.centroids = cents


    # update centroid and the list
    def insertCRGB(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        c = (self.r, self.g, self.b)
        self.centroids.append(c)
        return(c)

    def insertCTUP(self, tup):
        self.r = tup[0]
        self.g = tup[1]
        self.b = tup[2]
        c = (self.r, self.g, self.b)
        self.centroids.append(c)
# end of Centroids class #
