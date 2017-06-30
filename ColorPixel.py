# Student: Krizia Houston Buck
# Faculty: Dr. Emre Celebi
# University of Central Arkansas
# Summer 2017
# Graduate Project
# ColorPixel.py (Color Class file)

import math

# ******* maybe try making a Color class with RGB then use inheritance for Centroids and Pixels (have a location too)

class ColorPixel(object):



    def __init__(self, c):
        super(ColorPixel, self).__init__()
        if (type(c) == tuple):
            self.r = c[0]
            self.g = c[1]
            self.b = c[2]
        else:
            self.r = c.r
            self.g = c.g
            self.b = c.b


    # update centroid and the list
    def insertRGB(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        c = (self.r, self.g, self.b)
        return(c)

    def insertTUP(self, tup):
        self.r = tup[0]
        self.g = tup[1]
        self.b = tup[2]
        c = (self.r, self.g, self.b)
        return(c)

    def r(self):
        return(self.r)

    def g(self):
        return(self.g)

    def b(self):
        return(self.b)

    def printRGB(self):
        print('(' + str(self.r) + ', ' + str(self.g) + ', ' + str(self.b) + ') ')

    # Update the Nearest Center (centroid) #
    def upC(self, pixel, LR, t):
        # print("--in upC")


        # Learning Rate of (1/(1+t))
        if (LR == 1):
            self.r = float(((1 / (1 + t)) * pixel.r) + (1 - ((1 / (1 + t)) * self.r)))
            self.g = float(((1 / (1 + t)) * pixel.g) + (1 - ((1 / (1 + t)) * self.g)))
            self.b = float(((1 / (1 + t)) * pixel.b) + (1 - ((1 / (1 + t)) * self.b)))
        # Learning Rate of sqrt(1/(1+t))
##!! Gives back white image
        elif (LR == 2):
            self.r = (math.sqrt(1 / (1 + t)) * pixel.r) + ((1 - math.sqrt(1 / (1 + t))) * self.r)
            self.g = (math.sqrt(1 / (1 + t)) * pixel.g) + ((1 - math.sqrt(1 / (1 + t))) * self.g)
            self.b = (math.sqrt(1 / (1 + t)) * pixel.b) + ((1 - math.sqrt(1 / (1 + t))) * self.b)
        # Average of both points for LR
        else:
            self.r = float((pixel.r + self.r) / 2)
            self.g = float((pixel.g + self.g) / 2)
            self.b = float((pixel.b + self.b) / 2)


        return (self)
    # end of ColorPixel class #
