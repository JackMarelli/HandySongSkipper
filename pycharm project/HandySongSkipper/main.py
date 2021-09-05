import cv2
import mediapipe as mp
import time
import win32api

import HandTrackingModule as htm

PLAY_PAUSE_BUTTON = 0xB3

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
detector = htm.handDetector()

# restituisce True se le 4 dita lunghe sono aperte, se anche una sola è chiusa False
def findOpenHand(varLmList):
    open = False
    if len(varLmList) != 0:
        open = True
        if varLmList[8][2] > varLmList[6][2]:
            open = False
        if varLmList[12][2] > varLmList[10][2]:
            open = False
        if varLmList[16][2] > varLmList[14][2]:
            open = False
        if varLmList[20][2] > varLmList[18][2]:
            open = False
    return open

def playPause():
    hwcode = win32api.MapVirtualKey(PLAY_PAUSE_BUTTON, 0)
    win32api.keybd_event(PLAY_PAUSE_BUTTON, hwcode)

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=False)

    print(findOpenHand(lmList))
    if findOpenHand(lmList):
        playPause()
        time.sleep(2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
