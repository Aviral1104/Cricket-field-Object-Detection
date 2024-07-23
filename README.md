# Cricket-field-Object-Detection
The code demonstrates the process of training a YOLOv8 object detection model on a custom cricket dataset.
It begins by importing necessary libraries and defining the dataset path, followed by creating a data.yaml file that specifies the paths to training, validation, and test images, the number of classes, and their names.
The YOLO model is then initialized using pre-trained weights, and the training process is executed for 50 epochs with a specified input image size and batch size. After training, the model is evaluated on the validation set, and inference is performed on a specific image to detect objects.
Finally, the trained model is exported in ONNX format for compatibility with other frameworks. This code effectively encapsulates the workflow for training, evaluating, and deploying a YOLOv8 model on a custom dataset.

![Prdeicted image 2](https://github.com/user-attachments/assets/579e0720-8037-4e49-b7aa-2aaa1d4a277f)

#YOLO-for-object-detection-in videos
When applied to video object detection, YOLO processes each frame of the video independently, treating it as a single image. The algorithm divides each frame into a grid and predicts bounding boxes and class probabilities for objects within each grid cell. YOLO's strength lies in its ability to perform detection in a single forward pass through the neural network, making it fast enough for real-time video processing. To use YOLO for video object detection, you typically load a pre-trained YOLO model, read video frames sequentially, apply the model to each frame to detect objects, draw bounding boxes and labels on the detected objects, and then either display the processed frame in real-time or write it to an output video file. This process is repeated for every frame in the video, resulting in a continuous stream of object detection throughout the entire video sequence.

https://drive.google.com/file/d/12hs2Fy9Sbx0MWycYCgU-UotIZaP0p5-c/view?usp=sharing

This is the first draft and is kind of like, how Americans would see cricket, more fine tuning is required.

Video Credit: https://www.youtube.com/@officialenglandcricket
