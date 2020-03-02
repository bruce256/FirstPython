# coding=utf-8
import requests, cv2

# 打开摄像头
capture = cv2.VideoCapture(0)

print(type(capture))
print(capture.read())

# 导入模型
face_model = cv2.CascadeClassifier('/Users/LvSheng/study/facemodel.xml')

# 获取摄像头的实时画面
while True:
    # 5.读取当前摄像头一帧的画面 true false
    ret, image = capture.read()
    print(ret)
    # 6.图片灰度处理
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # 7.人脸检测
    faces = face_model.detectMultiScale(gray, 1.1, 3, 0, (100, 100))

    # 8.标记人脸
    for (x, y, w, h) in faces:
        # 1.原始图片 2.左上角坐标 3.右下角坐标 4.颜色值 5.线宽
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
        # 9.显示图片
        cv2.imshow('image', image)

    # 暂停窗口
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 11.释放资源
capture.release()

# 12.销毁窗口
cv2.destroyAllWindows()
