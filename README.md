# Face-Detector

Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. 
OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. 


In this project , we can detect faces in videos. As you know videos are basically made up of frames, which are still images.
So we perform the face detection for each frame in a video . we use an infinite loop to loop through each frame in the video. We use video.read() to read each frame.
The detection works only on grayscale images. So it is important to convert the color image to grayscale.faces contains a list of coordinates for the rectangular
regions where faces were found . We use these coordinates to draw the rectangles in our image.

# Contributing

If you have a suggestion that would make this project better in any way , please fork the repo and create a pull request.
You can also simply open an issue with the tag "feature-request". Any and all contributions you make are greatly appreciated . 
Don't forget to give the project a star⭐⭐! Thanks again!

Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

Every PR will be reviewed before merging.
