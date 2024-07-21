# Cricket-field-Object-Detection
The code is designed to train a YOLOv8 object detection model on a custom dataset of cricket images.
"data_yaml" dictionary
  train: The path to the training images.
  val: The path to the validation images.
  test: The path to the test images.
  nc: The number of classes in the dataset (3 in this case: ball, bat, pitch).
  names: The names of the classes.
  The yaml.dump() function is used to save the data_yaml dictionary to a file named data.yaml in the dataset_path directory.
