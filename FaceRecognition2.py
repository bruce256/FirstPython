import cv2
import face_recognition

# 2.读取图片
filename = 'dataset/lvsheng1.jpeg'
image = cv2.imread(filename)

encodings = face_recognition.face_encodings(image)[0]
print(encodings)

image2 = cv2.imread('dataset/lvsheng1.jpeg')
encodings2 = face_recognition.face_encodings(image2)[0]

result = face_recognition.compare_faces([encodings], encodings2)

print(result)

faces = face_recognition.face_locations(image)

# 6.标记人脸(椭圆形、三角形、矩形)
for (top, right, bottom, left) in faces:
    # 1.原始图片 2.左上角坐标 3.右下角坐标 4.颜色值 5.线宽
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)


# 7.显示图片
cv2.imshow('Jim', image)

# 8.暂停窗口
cv2.waitKey(0)

# 9.销毁窗口
cv2.destroyAllWindows()
