# coding=utf-8

import cv2
import face_recognition

# 打开摄像头
capture = cv2.VideoCapture(0)

print(type(capture))
print(capture.read())

# 2.读取图片
filename = 'dataset/bruce.jpeg'
image = cv2.imread(filename)
know_encodings = face_recognition.face_encodings(image)

# 获取摄像头的实时画面
while True:
    # 5.读取当前摄像头一帧的画面 true false
    ret, image = capture.read()
    # print(ret)

    unknown_encodings = face_recognition.face_encodings(image)
    print(unknown_encodings)
    faces = face_recognition.face_locations(image)

    # 8.标记人脸
    for (top, right, bottom, left) in faces:
        # 1.原始图片 2.左上角坐标 3.右下角坐标 4.颜色值 5.线宽
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    if unknown_encodings.__len__() > 0:
        resultList = face_recognition.compare_faces(know_encodings, unknown_encodings[0])
        for result in resultList:
            if result:
                cv2.putText(image, "bruce", (faces[0][3], faces[0][0]), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0))

    # 显示镜头捕捉到的图像
    cv2.imshow('Jim', image)

    # 暂停窗口
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 11.释放资源
capture.release()

# 12.销毁窗口
cv2.destroyAllWindows()
