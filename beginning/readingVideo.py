import cv2 as cv

cam = cv.VideoCapture("dog.mp4")  # All videos,photos and codes are in same directory.

while True:
    isTrue, frame = cam.read()
    if isTrue==True:
        cv.imshow("Video", frame)
    else:
        print("Okunamadı")
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()


