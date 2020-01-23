import cv2
import pytesseract
img = cv2.imread("/home/avi101/Desktop/index.png")
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def perform_ocr(image,config = None):
	text = pytesseract.image_to_string(image,config = None)
	return text

print(perform_ocr(img))
cv2.imshow("Sampled", img)
cv2.waitKey(0)