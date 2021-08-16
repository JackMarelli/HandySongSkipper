import mediapipe as mp
import cv2
import win32api
import time

PLAY_PAUSE_KEY = 0xB3

capture = cv2.VideoCapture(0)
mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands()
currentTime = 0;
previousTime = 0;

while True:
    #capture image & process
    success, img = capture.read()
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbImg)

    #draw landmarks & connections
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    #call general play-pause button if something is detected and wait 2s
    if results.multi_hand_landmarks:
        win32api.keybd_event(PLAY_PAUSE_KEY, win32api.MapVirtualKey(PLAY_PAUSE_KEY, 0))
        time.sleep(2)

    #draw fps
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    cv2.putText(img,"FPS: " + str(int(fps)),(10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)

    #show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)


