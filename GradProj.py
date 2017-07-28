# Student: Krizia Houston Buck
# Faculty: Dr. Emre Celebi
# University of Central Arkansas
# Summer 2017
# Graduate Project
# GradProj.py (main file)

# PIL for manipulating images
import PIL
from PIL import Image
# time for stopwatch capability
import time
# Online K-Means python file
import OKM



# Read Image #
def readImage(userIn):
   # print('in readImage')

    # Images
    pic1 = "Bikes.JPG"
    pic2 = "Birds.jpg"
    pic3 = "Boats.JPG"
    pic4 = "Girl.JPG"
    pic5 = "Hats.JPG"
    pic6 = "Lena.JPG"
    pic7 = "Mandrill.JPG"
    pic8 = "Peppers.JPG"



##### User selects image to use
    if (userIn == 1):
        picture = pic1
    elif (userIn == 2):
        picture = pic2
    elif (userIn == 3):
        picture = pic3
    elif (userIn == 4):
        picture = pic4
    elif (userIn == 5):
        picture = pic5
    elif (userIn == 6):
        picture = pic6
    elif (userIn == 7):
        picture = pic7
    elif (userIn == 8):
        picture = pic8
    else:
        picture = pic1

    im = Image.open(picture)
    # im.show()


    return(im)
# end of readImage #



# Manipulate Images - learn to use PIL #
def maniImage(im):
    print (im.format, im.size, im.mode)

    # Rotate an image
    im.rotate(45).show()

    # multiply each pixel by a constant
    out = im.point(lambda i: i * 2)
    out.show()

    # Split and merge bands (rgb)
    r, g, b = im.split()
    # r.show()
    # g.show()
    # b.show()

    # proves that each pixel color is tallied separately as r, g, and b not as an rgb combo
    # hist = im.histogram()
    # print(sum(hist))
    # rHist = r.histogram()
    # print("R: ")
    # print(rHist)
    # gHist = g.histogram()
    # print("G: ")
    # print(gHist)
    # bHist = b.histogram()
    # print("B: ")
    # print(bHist)
    # imM1 = Image.merge("RGB", (r, b, g))
    # imM2 = Image.merge("RGB", (g, b, r))
    # imM3 = Image.merge("RGB", (g, r, b))
    # imM4 = Image.merge("RGB", (b, g, r))
    # imM5 = Image.merge("RGB", (b, r, g))
    # imM1.show()
    # imM2.show()
    # imM3.show()
    # imM4.show()
    # imM5.show()



    # get pixel values as (r,g,b) at indices
    data = list(im.getdata())
    print('Get Data: ')
    print(data)



    # TESTING THESE IDEAS for individual pixel manipulation
    rpix = r.getpixel((0,5))
    print("r pixel: " + str(rpix))
    p = im.getpixel((0,5))
    print("p pixel: " + str(p))
    rint = int(rpix)


    # HOW TO CHANGE PIXELS
    rint = 200
    test = im.load()
    for x in range(0,750):
        for y in range(0,1334):
            test[x,y] = (rint, rint, rint)
    im.show()


    # return manipulated image
    return(im)
# end of maniImage #



# All Scenarios Run with only User Input Once #
def allScenarios(output):
    c = 1 # iteration count
    times = [] # elapsed time list

##### User selects image
    image = input('Select which image to use (1-8):  ')
    # read in image
    im = readImage(image)


    # Cluster Number
    K = 8
    for k in range(0, 6):
        q = im.quantize(K)
        q.show()
        f = "PILquantizer_" + str(image) + "_" + str(K) + ".PNG"
        q.save(f)

        # [1] Linear Initialization, [2] Random Initialization, [3] Most Common Color Initialization, or [4] Maximin Initialization
        for init in range(2,5): # SKIP LINEAR
            # for output image name
            if (init == 1):
                INIT = "LI"
            elif (init == 2):
                INIT = "RI"
            elif (init == 3):
                INIT = "MCCI"
            else:
                INIT = "MI"

            # Presentation Style of [1] Cyclic/Linear or [2] Random
            for PS in range(1,3):
                # for output image name
                if (PS == 1):
                    pres = "LPS"
                else:
                    pres = "RPS"

                # Learning Rate of [1] 1/(1+t) or [2] sqrt(1/(1+t)) or [3] normal
                for LR in range(1,4):
                    # for output image name
                    if (LR == 1):
                        lr = "LR1"
                    elif (LR == 2):
                        lr = "LR2"
                    else:
                        lr = "LR3"

                    # make sure pix is from original image each run
                    im = readImage(image)
                    pix = im.load()

    ## Online K - Means ##
                    print("\n#### Running Algorithm ####")
                    times = run(output, image, K, im, pix, init, PS, LR, times, c, INIT, pres, lr)
                    c += 1
        # end all for loops
        K = K * 2
        # end cluster number for loop
    # end all for loops

    # Get final results.txt and output to terminal
    results(times, output)
# end allScenarios #



# Test Drive with no User Input #
def testDriver(output):
    c = 1 # iteration count
    times = [] # elapsed time list

    # Image selection
    for image in range(1,9):
        # read in image and save built in quantized image
        im = readImage(image)
        im.show()


        # Cluster Number
        K = 8
        for k in range(0, 6):
            q = im.quantize(K)
            q.show()
            f = "PILquantizer_" + str(image) + "_" + str(K) + ".PNG"
            q.save(f)

            # [1] Linear Initialization, [2] Random Initialization, [3] Most Common Color Initialization, or [4] Maximin Initialization
            for init in range(2,5): # CORRECTION - skip linear
                # for output image name
                if (init == 1):
                    INIT = "LI"
                elif (init == 2):
                    INIT = "RI"
                elif (init == 3):
                    INIT = "MCCI"
                else:
                    INIT = "MI"

                # Presentation Style of [1] Cyclic/Linear or [2] Random
                for PS in range(1,3):
                    # for output image name
                    if (PS == 1):
                        pres = "LPS"
                    else:
                        pres = "RPS"

                    # Learning Rate of [1] 1/(1+t) or [2] sqrt(1/(1+t)) or [3] normal
                    for LR in range(1,4):
                        # for output image name
                        if (LR == 1):
                            lr = "LR1"
                        elif (LR == 2):
                            lr = "LR2"
                        else:
                            lr = "LR3"

                        # make sure pix is from original image each run
                        im = readImage(image)
                        pix = im.load()

        ## Online K - Means ##
                        print("\n#### Running Algorithm ####")
                        times = run(output, image, K, im, pix, init, PS, LR, times, c, INIT, pres, lr)
                        c += 1
            # end all for loops
            K = K * 2
        # end cluster number for loop
    # end image selection for loop

    # Get final results.txt and output to terminal
    results(times, output)
# end testDriver #



# Run OKM, print, and save to file #
def run(output, image, K, im, pix, init, PS, LR, times, c, INIT, pres, lr):
    # time the clustering of data using stopwatch
    start = time.time()
    OUT = OKM.kmeans(K, im, pix, init, PS, LR)
    out = OUT[0]
    sse = OUT[1]
    end = time.time()
    elapsed = end - start
    times.append(elapsed)
    print("\nElapsed time in seconds: " + str(times[c - 1]))
    print("Elapsed time in minutes: " + str(elapsed / 60.0))

    # save and display the image with fewer colors
 #   out.show()
    filename = "Output" + str(image) + "_K" + str(K) + "_" + INIT + "_" + pres + "_" + lr + ".PNG"
    print(filename + " now available")
    out.save(filename)


    # Results.txt output
    output.write(str(image) + ", " + str(K) + ", " + str(init) + ", " + str(PS) + ", " + str(LR) + ", " + str(sse) + " - " + str(times[c - 1]) + " * " + filename + "\n")


    return(times)
# end of run #



# Results of the tests #
def results(times, output):
    # Final stats and close Results.txt
    s = sum(times)
    avg = s / len(times)
    print("\n#### Results ####")
    print("Average time in seconds: " + str(avg))
    avgM = avg / 60.0
    print("Average time in minutes: " + str(avgM))

    # close Results file
    output.write("\nAverage of " + str(len(times)) + " run(s) in seconds: \n")
    output.write(str(avg))
    output.write("\nAverage of " + str(len(times)) + " run(s) in minutes: \n")
    output.write(str(avgM))
    output.close()

    print("Terminating - Results.txt now available ")
# end of results #



# Call Everything from Main #
def main():
    # variables
    c = 1 # iteration count
    times = [] # elapsed time list
    print("Krizia Houston Buck - UCA Summer 2017 - Applied Computing Graduate Project - Dr. Emre Celebi - Department of Computer Science ")

    # new file called Results.txt for all user input and elapsed times
    ts = time.time()
    filename = "Results" + str(ts) + ".txt"
    output = open(filename, "w")
    output.write("Krizia Houston Buck - UCA Summer 2017 - Graduate Project - Dr. Emre Celebi \n\n")
    output.write("Time Result(s) - Image, Clusters, Initialization, Presentation Style, Learning Rate, SSE: (in seconds) \n")


##### User decides whether to do all of the cases in one or do some individual tests
    userInput = input('\nRun [1] All Scenarios on one image or go [2] Individually for testing? or [3] run the Test Driver: ')
    if (userInput == 1):
        allScenarios(output)
        # Skip option to do individual runs to preserve the information in Results.txt
        c = -2
    elif (userInput == 3):
        testDriver(output)
        c = -2


    # rerun as many times as user wants
    while (c > 0):
##### User selects image
        image = input('\nSelect which image to use (1-8):  ')
        # read in image
        im = readImage(image)
# ##### User selects whether to go to maniImage
#         userinput = input('Go into maniImage? (y/n): ')
#         if (userinput == 'y'):
#     ##      # Manipulate images (pixels)
#             imMani = maniImage(im)
#             pix = imMani.load()
#         else:
#             pix = im.load()
#      #   x, y = 2, 4; print('Pixels loaded individually for access. Example: '); print('Pixel value of [' + str(x) + ', ' + str(y) + ']'); print(pix[x,y])
        im.show()
        pix = im.load()


##### User inputs cluster number
        uIn = input('Number of clusters (k): ')
        k = int(uIn)

##### User chooses type of Initialization
        uIn1 = input('[1] Linear Initialization, [2] Random Initialization, [3] Most Common Color Initialization, or [4] Maximin: ')
        if (uIn1 == '2'):
            initChoice = 2
            INIT = "RI"
        elif (uIn1 == '3'):
            initChoice = 3
            INIT = "MCCI"
        elif (uIn1 == '4'):
            initChoice = 4
            INIT = "MI"
        else:
            initChoice = 1
            INIT = "LI"

##### User chooses type of Presentation Style
        uIn2 = input('Presentation Style of [1] Cyclic/Linear or [2] Random: ')
        if (uIn2 == '2'):
            psChoice = 2
            pres = "RPS"
        else:
            psChoice = 1
            pres = "LPS"

##### User chooses the Learning Rate
        uIn3 = input('Learning Rate of [1] 1/(1+t), [2] sqrt(1/(1+t)), or [3] normal: ')
        if (uIn3 == '1'):
            LR = 1
            lr = "LR1"
        elif (uIn3 == '2'):
            LR = 2
            lr = "LR2"
        else:
            LR = 3
            lr = "avgLR"


##### built in PIL quantization (use for comparison)
        uIN = input('Built in PIL Quantizer? (y/n): ')
        if (uIN == 'y'):
            q = im.quantize(k)
            q.show()


    ## Online K - Means ##
        print("\n#### Running Algorithm ####")
        # time the clustering of data using stopwatch
        times = run(output, image, k, im, pix, initChoice, psChoice, LR, times, c, INIT, pres, lr)

        # ask user if they want to do it all again
        uIn4 = input('Run again? (y/n): ')
        if (uIn4 == 'y'):
            c += 1
        else:
            c = 0

    if (c != -2):
        # user selected to end the program
        results(times, output)
# end of main #



# Call Main #
if __name__ == '__main__':
    main()
# end of program #



#### HELPFUL INFO ####

## http://effbot.org/imagingbook/introduction.htm
    # Split and merge bands (rgb)
    # r, g, b = im.split()
    # r.show()
    # g.show()
    # b.show()
    # imM1 = Image.merge("RGB", (r, b, g))
    # imM2 = Image.merge("RGB", (g, b, r))
    # imM3 = Image.merge("RGB", (g, r, b))
    # imM4 = Image.merge("RGB", (b, g, r))
    # imM5 = Image.merge("RGB", (b, r, g))
    # imM1.show()
    # imM2.show()
    # imM3.show()
    # imM4.show()
    # imM5.show()



    # Manipulate individual bands (RGB)  -  imout = im.point(lambda i: expression and 255)
    # split the image into individual bands  -
    # source = im.split()
    # R, G, B = 0, 1, 2
    # # select regions where red is less than 100
    # mask = source[R].point(lambda i: i < 100 and 255)
    # # process the green band
    # out = source[G].point(lambda i: i * 0.7)
    # # paste the processed band back, but only where red was < 100
    # source[G].paste(out, None, mask)
    # # build a new multiband image
    # im = Image.merge(im.mode, source)
    # im.show()
    # im.save("output.jpg")


    # getcolors
    # im.getcolors() - a list of(count, color) tuples or None
    # im.getcolors(maxcolors) - a list of(count, color) tuples or None
    # try to get (count, colors)
    # c = im.getcolors()
    # print('Get Colors: ')
    # print(c)
    # # get pixel values as (r,g,b) at indices
    # d = list(im.getdata())
    # print('Get Data: ')
    # print(d)
    # # get individual pixel
    # pix = im.load()
    # print('Pixels loaded individually for access: ')
    # x, y = 10, 20
    # print(pix[x, y])