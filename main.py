import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam could not be opened.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("AI Hand Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()