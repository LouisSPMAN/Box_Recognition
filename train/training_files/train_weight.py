from multiprocessing import freeze_support
from ultralytics import YOLO

if __name__ == '__main__':
    freeze_support()

    model = YOLO('yolov8n.yaml')
    model = YOLO('yolov8n.pt')
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')

    results = model.train(data='D:/Box_Recognition/Box/data.yaml', resume=True, pretrained=True, save_period=5,
                          epochs=200)

    results = model.val()  # automatically evaluate the data

    success = model.export(format='onnx')
