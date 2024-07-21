from ultralytics import YOLO
import yaml

dataset_path = r'/content/drive/MyDrive/cricket.v1i.yolov8'

data_yaml = {
    'train': f'{dataset_path}/train/images',
    'val': f'{dataset_path}/valid/images',
    'test': f'{dataset_path}/test/images',
    'nc': 3,
    'names': ['ball', 'bat', 'pitch']
}

with open(f'{dataset_path}/data.yaml', 'w') as file:
    yaml.dump(data_yaml, file)

model = YOLO('/content/yolov8n.pt') 

results = model.train(
    data=f'{dataset_path}/data.yaml',
    epochs=50,
    imgsz=640,
    batch=16,
    name='cricket_model'
)

results = model.val()

results = model('/content/drive/MyDrive/cricket.v1i.yolov8/images.jpeg')

model.export(format='onnx')
