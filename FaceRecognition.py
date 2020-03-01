import cv2
import re
import os
import bs4

# 2.读取图片
filename = '/Users/LvSheng/Pictures/WechatIMG43.jpeg'
image = cv2.imread(filename)

# 3.加载人脸模型 级联分类器
face_model = cv2.CascadeClassifier('/Users/LvSheng/study/facemodel.xml')

# 4.对图片进行灰度处理
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# 5.检查人脸
faces = face_model.detectMultiScale(gray)

# 6.标记人脸(椭圆形、三角形、矩形)
for (x, y, w, h) in faces:
    # 1.原始图片 2.左上角坐标 3.右下角坐标 4.颜色值 5.线宽
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 7.显示图片
cv2.imshow('Jim', image)

# 8.暂停窗口
cv2.waitKey(0)

# 9.销毁窗口
cv2.destroyAllWindows()
