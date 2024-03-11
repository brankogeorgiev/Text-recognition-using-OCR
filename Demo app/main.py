import easyocr
import cv2
import matplotlib.pyplot as plt

image_path1 = 'C:\\Users\\baneg\\PycharmProjects\\DPNS\\OCR\\images\\stop_sign.jpg'
image_path2 = 'C:\\Users\\baneg\\PycharmProjects\\DPNS\\OCR\\images\\img2.jpg'
image_path3 = 'C:\\Users\\baneg\\PycharmProjects\\DPNS\\OCR\\images\\img3.png'

img1 = cv2.imread(image_path1)
img2 = cv2.imread(image_path2)
img3 = cv2.imread(image_path3)

reader = easyocr.Reader(['ch_tra', 'en'], gpu=False)

img = img1

text_ = reader.readtext(img)

for t in text_:
    print(t)

    bbox, text, score = t

    pt1 = tuple(map(int, bbox[0]))
    pt2 = tuple(map(int, bbox[2]))

    cv2.rectangle(img, pt1, pt2, (0, 255, 0), 3)
    cv2.putText(img, text, pt1, cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 3, cv2.LINE_AA)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()