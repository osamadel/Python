import cv2
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1
img = np.zeros((512, 512, 3), np.uint8)


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img,(x,y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
        else:
            cv2.circle(img,(x,y),5, (0,0,255), -1)


def main():
    # ========== Video Camera Capture =========== #
    # cap = cv2.VideoCapture(0)
    # if not cap.isOpened():
    #     cap.open()
    # while True:
    #     ret, frame = cap.read()
    #     print "Captures? =", ret
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow("Live Stream", gray)
    #
    #     if cv2.waitKey(1) & 0xff == ord('q'):
    #         break
    # # don't forget to release the capture.
    # cap.release()
    # cv2.destroyAllWindows()

    # ========== Drawing Shapes on images =========== #
    # Creates a black image
    # im = np.zeros((512, 512, 3), np.uint8)
    #
    # # Draws a blue line from 0,0 to 511,511 with 5px thickness
    # cv2.line(im,(0,0),(511,511),(255,0,0),5)
    # # Draw a rectangle at the right-most corner
    # cv2.rectangle(im,(400,0),(511,111),(0,255, 0), 3)
    # # Draws a circle inside the rectangle
    # cv2.circle(im,(455,55), 55, (0, 0, 255), -1)
    # # Write text
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(im,"OpenCV",(10,511), font, 4, (0,255,255), 2)
    #
    # cv2.imshow("Image", im)
    # cv2.waitKey(0)

    global mode
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    while(1):
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xff == ord('m'):
            mode = not mode
        elif cv2.waitKey(20) & 0xff == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
