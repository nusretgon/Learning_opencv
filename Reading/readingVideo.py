import cv2 as cv

cam = cv.VideoCapture("dog.mp4")  # All videos,photos and codes are in same directory.
while True:
    isTrue, frame = cam.read()
    cv.imshow("Video", frame)


    if cv.waitKey(10) & 0xFF == ord('q'):   # If you decrease waitKey parameter video speed increase.
        break

cam.release()
cv.destroyAllWindows()


