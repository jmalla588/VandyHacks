# GuardBot

## **Convolutional Neural Networks**, **Video Livestreaming**, and **Image Modeling/Processing**....and a **GroupMe Bot?**

### How could these _possibly_ fit together? Let us explain.

This project has quite a few bits and pieces that work together to form the basics of a security system - or more simply, a simple notifier for any visitors you may have at your front door. Better yet, you don't need any new software to get the notifications, as our product integrates directly with a GroupMe group in order to send notifications to a relevant group of people.


### Step 1: Video Livestream

Our project begins with the collection of our data - which in this case is a *live feed from a computer's webcam*. We were able to use OpenCV in order to capture a direct stream of the input data received by a laptop's camera, and then used *a sample website created by Flask* in order to send this livestream to the cloud. A service called ngrok allowed us to easily host this video livestream and make it accessible to other devices.

#### Relevant files, services, & credits (thanks for providing us with stuff!):
camera.py, main.py, index.html, ngrok, python3, random people on stack overflow


### Step 2: Amazon EC2 and Convolutional Neural Network

Once our video stream was on the internet and available, we used an Amazon EC2 GPU instance for access to CUDA and CUDNN framework. Like actually, that stuff is reeeeal nifty. We used our EC2 instance in conjunction with Google's *deep learning framework known as TensorFlow*, to quickly *process frames from our video stream (capable of 60 fps using NVIDIA's CUDNN) and detect the various objects present in said frames*. We created a python script to parse the stream with OpenCV and then these frames were sent through the pre-trained Inception model.

#### Relevant files, services, & credits (thanks for providing us with stuff!):
TensorFlow (GoogLeNet), Amazon EC2 AWS instance, python3, random people on stack overflow


### Step 3: GroupMe Bot?

We wanted to provide our users with a simple yet elegant way to stay updated on their visitors, whether they be wanted or unwanted. Therefore, we decided to use the publicly available *GroovyAPI for Python3* to create a GroupMe Bot. This bot is capable of informing a group of users that a person is approaching the camera. GroupMe provided an elegant solution for this, as we are easily able to notify relevant individuals in any given scenario.

#### Relevant files, services, & credits (thanks for providing us with stuff!):
Dude who made the Groupy API, Python3, Conor Joplin (thanks man)


## So after all that....where does this leave us?

We made a camera that does a bunch of super fancy stuff to figure out when a person is present and can notify people using GroupMe. Ta-da! Sidenote: It's still being worked on.
