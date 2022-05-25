import cv2
cap = cv2.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    if isTrue:
        cv2.imshow("Secret Cam", frame)
    else:
        print("Reading Error!")
    if cv2.waitKey(5) & 0xFF == ord("q"):   # If you decrease waitKey parameter video speed increase.
        break

cap.release()
cv2.destroyAllWindows()

