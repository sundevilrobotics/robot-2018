from Class.ShapeIdentifier import ShapeIdentifier
import imutils
import cv2

cap = cv2.VideoCapture(0)

while (1):

    # Take each frame
    _, frame = cap.read()
    sd = ShapeIdentifier()

    resized = imutils.resize(frame, width=300, height=300)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 90, 150, cv2.THRESH_BINARY)[1]

    cv2.imshow("thresh", thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # currently able to find circle, next steps would be to match
    # if circle and circle color is inRange of hsv green values.
    # also make circle drawing stay throughout program by making
    # xy of shape a global var outside of the while
    # update that var every x amount of frames to stay on course

    for c in cnts:
        shape = sd.detect(c)
        M = cv2.moments(c)
        if M["m00"] == 0:
            break

        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        c = c.astype("float")
        c = c.astype("int")
        cv2.drawContours(resized, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 255, 255), 2)

    cv2.imshow("res", resized)
    cv2.waitKey(10)

cv2.destroyAllWindows()
