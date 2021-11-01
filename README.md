# Face-Detector

Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. 
OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. 


In this project , we can detect faces in videos. As you know videos are basically made up of frames, which are still images.
So we perform the face detection for each frame in a video . we use an infinite loop to loop through each frame in the video. We use video.read() to read each frame.
The detection works only on grayscale images. So it is important to convert the color image to grayscale.faces contains a list of coordinates for the rectangular
regions where faces were found . We use these coordinates to draw the rectangles in our image.
