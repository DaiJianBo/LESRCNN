# coding: utf-8
from PIL import Image
import os
import os.path
import numpy as np
import cv2
# 指明被遍历的文件夹
rootdir = "train"
# rootdir = "DIV2K_train_HR"
# rootdir=r'C:\Users\阿波\Desktop\val'
# https://blog.csdn.net/qq_40801168/article/details/83691774
#用Python批量裁剪图片

for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        img = Image.open(currentPath)
        #
        # print(img.format, img.size, img.mode)
        image=cv2.imread(currentPath)
        # h, w, c = image.shape
        h=image.shape[0]
        w=image.shape[1]
        # img.show()
        box1 = (int(0.5*w)-256, int(0.5*h)-256, int(0.5*w)+256, int(0.5*h)+256)  # 设置左、上、右、下的像素
        image1 = img.crop(box1)  # 图像裁剪
        # image1=img[int(0.15*h):int(0.85*h),int(0.15*w):int(0.85*w),:]

        image1.save(r"D:\改数据格式" + '\\'+ filename)  # 存储裁剪得到的图像