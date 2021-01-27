# Image-Processing-based-Vehicle-Detection

## Problem Statement:
Vehicle detection and tracking play an effective and significant role in the area of traffic
surveillance system where efficient traffic management and safety is the main concern.
How our project is different from the references:
We implemented the background elimination of frames as mentioned in the references.
But we implemented a different approach for detecting objects, we used the Haar
Cascade method to detect objects in a frame and not the Convolutional Neural Networks
method.
## Description:
Haar Cascade is a machine learning object detection algorithm used to identify objects
in an image or video and based on the concept of features. It is a machine learning-based
approach where a cascade function is trained from a lot of positive and negative images.
It is then used to detect objects in other images.
## Enhancements:
1. Used Haar cascade method instead of the Convolutional Neural Networks
method for object detection.
2. Calculated the number of vehicles in each frame.
Implementations in this iteration:
1. Detection of other vehicles like bus and two-wheeler vehicles is added.
2. Created Haar cascade file from the dataset provided.
3. Tested the implementation on video dataset.
## Procedure:
1. Created a Haar cascade file for the vehicle detection from a dataset.
2. Get frames from the video and convert them into grayscale.Then we detect
objects in the grayscale image using detectMultiScale, which detects objects of
different sizes and returns a list of rectangles.
3. Then we obtain the threshold of the image using cv2.threshold.
4. We find the number of contours in the frame using the threshold.
5. We count the number of contours occurring in a frame, that will be the number of
vehicles in the frame.
