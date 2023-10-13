import cv2
img_path = "QR.png"
img = cv2.imread(img_path)
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    print(f"QRCode data:\n{data}")