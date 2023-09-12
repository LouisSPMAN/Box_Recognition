import os
import shutil
import random


def split_dataset_to_label_and_images(src_dataset_path, des_dataset_path, train_path, val_path, test_path):
    """
    Split dataset to labels and images

    Args:
        dataset_path(str):the location of the dataset
        train_path(str):the location of the training set
        val_path(str):the location of the valuation set
        test_path(str):the location of the test set

    """

    # 定义训练集中图片和标签的子文件夹名称
    train_img_folder = "img"
    train_label_folder = "label"
    # 定义验证集中图片和标签的子文件夹名称
    val_img_folder = "img"
    val_label_folder = "label"
    # 定义测试集中图片和标签的子文件夹名称
    test_img_folder = "img"
    test_label_folder = "label"

    # 创建训练集的文件夹，如果已经存在则跳过
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(os.path.join(train_path, train_img_folder), exist_ok=True)
    os.makedirs(os.path.join(train_path, train_label_folder), exist_ok=True)

    # 创建验证集的文件夹，如果已经存在则跳过
    os.makedirs(val_path, exist_ok=True)
    os.makedirs(os.path.join(val_path, val_img_folder), exist_ok=True)
    os.makedirs(os.path.join(val_path, val_label_folder), exist_ok=True)

    # 创建测试集的文件夹，如果已经存在则跳过
    os.makedirs(val_path, exist_ok=True)
    os.makedirs(os.path.join(test_path, test_img_folder), exist_ok=True)
    os.makedirs(os.path.join(test_path, test_label_folder), exist_ok=True)

    # 获取数据集中所有的图片和标签文件名
    img_files = [f for f in os.listdir(src_dataset_path) if f.endswith(".jpg") or f.endswith(".png")]
    label_files = [f for f in os.listdir(src_dataset_path) if f.endswith(".txt")]

    # 随机打乱图片和标签文件名的顺序，保证它们一一对应
    random.seed(42)  # 设置随机数种子，保证每次运行结果一致
    random.shuffle(img_files)
    random.shuffle(label_files)

    # 定义训练集、验证集、测试集的比例
    train_ratio = 0.8
    valid_ratio = 0.1
    test_ratio = 0.1

    # 计算训练集、验证集、测试集的数量
    total_num = len(img_files)  # 总的图片和标签数量
    train_num = int(total_num * train_ratio)  # 训练集数量
    valid_num = int(total_num * valid_ratio)  # 验证集数量
    test_num = total_num - train_num - valid_num  # 测试集数量

    # 将图片和标签文件按比例分配到训练集、验证集、测试集中
    for i in range(total_num):
        if i < train_num:  # 前 train_num 个分配到训练集
            shutil.copy(os.path.join(src_dataset_path, img_files[i]),
                        os.path.join(train_path, train_img_folder, img_files[i]))
            shutil.copy(os.path.join(src_dataset_path, label_files[i]),
                        os.path.join(train_path, train_label_folder, label_files[i]))
        elif i < train_num + valid_num:  # 接下来 valid_num 个分配到验证集
            shutil.copy(os.path.join(src_dataset_path, img_files[i]),
                        os.path.join(val_path, val_img_folder, img_files[i]))
            shutil.copy(os.path.join(src_dataset_path, label_files[i]),
                        os.path.join(val_path, val_label_folder, label_files[i]))
        else:  # 剩下的分配到测试集
            shutil.copy(os.path.join(src_dataset_path, img_files[i]),
                        os.path.join(test_path, test_img_folder, img_files[i]))
            shutil.copy(os.path.join(src_dataset_path, label_files[i]),
                        os.path.join(test_path, test_label_folder, label_files[i]))

    # 打印完成的信息
    print("数据集分配完成！")

src_dataset_path = 'D:/ImageRecognition/dataset/downloaded_images'
dataset_path = 'D:/ImageRecognition/bottle_chair_table_keyboard_laptop_person'
train_path = 'D:/ImageRecognition/bottle_chair_table_keyboard_laptop_person/train'
val_path = 'D:/ImageRecognition/bottle_chair_table_keyboard_laptop_person/val'
test_path = 'D:/ImageRecognition/bottle_chair_table_keyboard_laptop_person/test'

_classes = os.listdir(path=src_dataset_path)
for _class in _classes:
    split_dataset_to_label_and_images(os.path.join(src_dataset_path, _class), dataset_path, train_path,
                                      val_path, test_path)

