import cv2
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import threading

from handLmModel import handDetector

vidObj = cv2.VideoCapture(0)
vidObj.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vidObj.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

handlmsObj = handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVolume = volRange[0]
maxVolume = volRange[1]

minBrightness = 0
maxBrightness = 100


def setVolume(dist):
    vol = np.interp(int(dist), [25, 95], [minVolume, maxVolume])
    volume.SetMasterVolumeLevel(vol, None)


def setBrightness(dist):
    brightness = np.interp(int(dist), [10, 100], [minBrightness, maxBrightness])
    sbc.set_brightness(int(brightness))


while True:
    _, frame = vidObj.read()
    frame = cv2.flip(frame, 1)
    frame = handlmsObj.findHands(frame)
    lndmrks = handlmsObj.findPosition(frame, draw=False)
    if lndmrks:
        # print(lndmrks[4],lndmrks[8])

        xr1, yr1 = lndmrks[1][4][1], lndmrks[1][4][2]
        xr2, yr2 = lndmrks[1][8][1], lndmrks[1][8][2]
        dist = math.hypot(xr2 - xr1, yr2 - yr1)

        if lndmrks[0] == 'Left':
            setBrightness(dist)
        elif lndmrks[0] == 'Right':
            setVolume(dist)


            t1 = threading.Thread(target=setVolume, args=(dist,))
            


            t1.start()


    cv2.imshow("stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
