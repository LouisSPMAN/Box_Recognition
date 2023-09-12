from ultralytics import YOLO
import cv2
import pandas as pd

model = YOLO("../train/training_files/runs/detect/train/weights/epoch185.pt")

# 获取摄像头内容
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 使用模型进行目标检测,并返回相应数据
    results_list = model.predict(source=frame)

    # 获取每个结果对象并进行处理
    for results in results_list:
        if results.boxes is not None:
            xyxy_boxes = results.boxes.xyxy
            conf_scores = results.boxes.conf
            cls_ids = results.boxes.cls

            # boxes = np.array([box[0], box[1], box[2] - box[0], box[3] - box[1]])
            for box, conf, cls_id in zip(xyxy_boxes, conf_scores, cls_ids):
                x1, y1, x2, y2 = map(int, box)
                cls_id = int(cls_id)
                label = model.names[cls_id]
                confidence = f"{conf:.2f}"
                confidence = confidence * 5

                print(label)
                print(xyxy_boxes)

                img_box = xyxy_boxes.tolist()

                df = pd.DataFrame({'x_centre': [img_box[0][0]], 'y_centre': [img_box[0][1]], 'width': [img_box[0][2]],
                                   'height': [img_box[0][3]]})
                df.to_csv('example.csv', index=False)

                # 颜色
                rectangle_color = (0, 255, 0)
                label_color = (0, 0, 255)

                # 在图像上绘制矩形框和标签
                cv2.rectangle(frame, (x1, y1), (x2, y2), rectangle_color, 2)
                cv2.putText(frame, f"{label} {confidence}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_color,
                            2)

        # 显示图像
        cv2.imshow('YOLOv8 Real-time Detection', frame)

    # 如果按下 'q' 键，则中断循环
    if cv2.waitKey(1) == ord('q'):
        break

# 释放视频文件和输出视频
cap.release()
cv2.destroyAllWindows()
