#This is a sample file.
import easygui as eg
import sys
from PIL import Image


title = "Embolism or nah?"
selMsg = "Select an Image"
quitMsg = "Go Fuck Yourself"
procMsg = "Perform Pre-Processing"
analyzeMsg = "Analyze Selected Image"

msg = "Welcome to the Pulmonary Embolism Finder!"
choices = [selMsg, quitMsg]
first = True; addButton = True;
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

    # Ooen main program window
    main = eg.buttonbox(msg, title, image=image, choices=choices)


    # If image selection is required.
    if main == selMsg:
        filename = eg.fileopenbox(msg = "Embolize", title = "Find Image File", default='*', filetypes=filetypes)
        # TODO: insert code here to do things with filename, as it contains the actual jpeg file.

        # Converts selected file so it can be displayed on image selection.
        Image.open(filename).convert('RGB').save('372151.jpg')


    # If the user wants to perform image processing
    elif main == procMsg:

    # If the user wants to analyze an image
    elif

    # If
    elif main == quitMsg:
        sys.exit(0)

    first = False;



# # while 1:
# title = "Embolism or Nah?"
# eg.msgbox("Click the button below to select an image.", title)
#
#
#
# msg ="What is your favorite flavor?"
# title = "Ice Cream Survey"
# choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
# choice = eg.choicebox(msg, title, choices)
#
# # note that we convert choice to string, in case
# # the user cancelled the choice, and we got None.
# eg.msgbox("You chose: " + str(choice), "Survey Result")
#
# msg = "Do you want to continue?"
# title = "Please Confirm"
# if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
#     pass  # user chose Continue
# else:
#     sys.exit(0)           # user chose Cancel