# Cricket-field-Object-Detection
The code demonstrates the process of training a YOLOv8 object detection model on a custom cricket dataset.
It begins by importing necessary libraries and defining the dataset path, followed by creating a data.yaml file that specifies the paths to training, validation, and test images, the number of classes, and their names.
The YOLO model is then initialized using pre-trained weights, and the training process is executed for 50 epochs with a specified input image size and batch size. After training, the model is evaluated on the validation set, and inference is performed on a specific image to detect objects.
Finally, the trained model is exported in ONNX format for compatibility with other frameworks. This code effectively encapsulates the workflow for training, evaluating, and deploying a YOLOv8 model on a custom dataset.

![Prdeicted image 2](https://github.com/user-attachments/assets/579e0720-8037-4e49-b7aa-2aaa1d4a277f)

