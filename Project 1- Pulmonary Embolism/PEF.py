#This is a sample file.
import easygui as eg
import sys
import PIL
from PIL import Image
import PIL.ImageOps
from PIL import ImageFilter
# import os
#import skimage
#from skimage import io
# from skimage import data
#from skimage.morphology import disk
# #from skimage.filters.rank import subtract)mean



title = "Embolism or nah?"
selMsg = "Select an Image"
quitMsg = "Quit"
procMsg = "Perform Pre-Processing"
analyzeMsg = "Analyze Selected Image"

msg = "Welcome to the Pulmonary Embolism Finder!"
choices = [selMsg, quitMsg]
first = True; addButton = True; useInverted = False;
image = "pef.gif"
filetypes = ["*.jpeg", "*.jpg", "*.png", "*.bmp"]

while 1:

    # Occurs after image selection, so new image appears in GUI
    if not first:
        # Only add Analyze and Process buttons after image selection
        if addButton:
            choices.insert(1, procMsg)
            choices.insert(2, analyzeMsg);
        Image.open('372151.jpg').convert('RGB').save('1.gif');
        image = "1.gif"
        addButton = False;

    if useInverted:
        Image.open('inverted.jpg').convert('RGB').save('1.gif');
        image = "1.gif"
        useInverted = False;

    # Ooen main program window
    main = eg.buttonbox(msg, title, image=image, choices=choices)


    # If image selection is required.
    if main == selMsg:
        filename = eg.fileopenbox(msg = "Embolize", title = "Find Image File", default='*', filetypes=filetypes)
        # TODO: insert code here to do things with filename, as it contains the actual jpeg file.

        # Converts selected file so it can be displayed on image selection.
        image = Image.open(filename).convert('RGB').save('372151.jpg')


    # If the user wants to perform image processing
    elif main == procMsg:
        #TODO
        conImage = Image.open(filename)
        inverted_image = PIL.ImageOps.invert(conImage)

        inverted_image.save('inverted.jpg')
        useInverted = True;
        print("penis")
        #Filtering bullshit
        # fn = os.path.join(skimage.data_dir, 'inverted.jpg')
        #xTestImg = io.imread(filename)
        # yTestImg = skimage.color.gray2rgb(xTestImg, alpha=None)
        # viewer = ImageViewer(yTestImg)
        # viewer.show


        pass

    # If the user wants to analyze an image
    elif main == analyzeMsg:
        #TODO
        pass

    # If the user wants to quit
    elif main == quitMsg:
        sys.exit(0)

    first = False;
