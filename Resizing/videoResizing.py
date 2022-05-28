import cv2 as cv

cam = cv.VideoCapture("dog.mp4")  # All videos,photos and codes are in same directory.
def rescaleFrame(cam):  # We define a function because we cant use all operations for each frame.
    return cv.resize(cam,(500,500),interpolation=cv.INTER_AREA)
while True:
    isTrue, frame = cam.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow("Video", frame_resized)


    if cv.waitKey(10) & 0xFF == ord('q'):   # If you decrease waitKey parameter video speed increase.
        break

cam.release()
cv.destroyAllWindows()
