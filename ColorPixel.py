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

        # Take LR here to speed up computation
        rate = 1.0 / (1.0 + t)
        rateComp = 1.0 - rate


        # Learning Rate of (1/(1+t))
        if (LR == 1):
            self.r = (rate * pixel.r) + (rateComp * self.r)
            self.g = (rate * pixel.g) + (rateComp * self.g)
            self.b = (rate * pixel.b) + (rateComp * self.b)
        # Learning Rate of sqrt(1/(1+t))
        elif (LR == 2):
            ratesqrt = math.sqrt(rate)
            ratesqrtComp = 1.0 - ratesqrt
            self.r = (ratesqrt * pixel.r) + (ratesqrtComp * self.r)
            self.g = (ratesqrt * pixel.g) + (ratesqrtComp * self.g)
            self.b = (ratesqrt * pixel.b) + (ratesqrtComp * self.b)
        # Average of both points for LR [3]
        else:
            self.r = float((pixel.r + self.r) / 2.0)
            self.g = float((pixel.g + self.g) / 2.0)
            self.b = float((pixel.b + self.b) / 2.0)


        return (self)
    # end of ColorPixel class #
