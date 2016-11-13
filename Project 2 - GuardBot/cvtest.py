import cv2
import urllib
import numpy as np
import os

stream=urllib.urlopen('http://4bf70e32.ngrok.io/video_feed')
bytes=''
count = 0;
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        count+=1;
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('i',i)

        if count % 100 == 0:
            #save image
            cv2.imwrite("runme.jpg", i)

            #run classify on saved image
            os.system("python3 classify_image.py --image_file runme.jpg")

        if cv2.waitKey(1) == 27:
            exit(0)



# import cv2, platform
# import numpy as np
# import urllib
# import os
#
# cam2 = "http://7ac65838.ngrok.io/video_feed"
#
# stream=urllib.urlopen(cam2)
# bytes=''
#
# while True:
#     # to read mjpeg frame -
#     bytes+=stream.read(1024)
#     a = bytes.find('\xff\xd8')
#     b = bytes.find('\xff\xd9')
#     if a!=-1 and b!=-1:
#         jpg = bytes[a:b+2]
#         bytes= bytes[b+2:]
#     frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
#     # we now have frame stored in frame.
#
#     cv2.imshow('cam2',frame)
#
#     # Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()
