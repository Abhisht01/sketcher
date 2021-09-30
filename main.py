import cv2
image = cv2.imread("symbols.png")
grey_f = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
invert = cv2.bitwise_not(grey_f)
blur = cv2.GaussianBlur(invert,(21,21),0)
inverted_blur = cv2.bitwise_not(blur)

sketch_f = cv2.divide(grey_f,inverted_blur,scale=300.0)
cv2.imwrite("output1.png",sketch_f)