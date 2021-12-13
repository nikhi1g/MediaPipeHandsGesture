import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
import pyautogui as py
from threading import Thread
from pynput.keyboard import Key, Controller, Listener#UNNECESSARY?




py.FAILSAFE = False#danger?

x = 50
y = 50
click = False
def mouse_movement():
    confcount = 0
    while True:
        x1 = 1440 -x
        py.moveTo(int(x1), int(y))
        if click:
            confcount += 1
            if confcount > 2:
                py.click()
                confcount = 0



Thread(target=mouse_movement).start()


cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
            # leftHand = results.multi_hand_landmarks[1]
            if results.multi_handedness[0].classification[0].label == "Left":  # actually right hand since it's flipped
                hand = results.multi_hand_landmarks[0]
                for id, lm in enumerate(hand.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 0:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpalmbottomx = cx
                        rightpalmbottomy = cy
                    if id == 1:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightthumbbasex = cx
                        rightthumbbasey = cy
                    if id == 2:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightthumbbaseDownx = cx
                        rightthumbbaseDowny = cy
                    if id == 3:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightthumbBaseUpx = cx
                        rightthumbBaseUpy = cy
                    if id == 4:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        # print(id, cx, cy)
                        rightthumbx = cx
                        rightthumby = cy
                        x = cx
                        y = cy
                    if id == 5:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpointerBasex = cx
                        rightpointerBasey = cy
                    if id == 6:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpointerDownx = cx
                        rightpointerDowny = cy
                    if id == 7:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpointerUpx = cx
                        rightpointerUpy = cy
                    if id == 8:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpointerx = cx
                        rightpointery = cy
                    if id == 9:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightmiddleBasex = cx
                        rightmiddleBasey = cy
                    if id == 10:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightmiddleDownx = cx
                        rightmiddleDowny = cy
                    if id == 11:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightmiddleUpx = cx
                        rightmiddleUpy = cy
                    if id == 12:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightmiddlex = cx
                        rightmiddley = cy
                    if id == 13:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightringBasex = cx
                        rightringBasey = cy
                    if id == 14:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightringDownx = cx
                        rightringDowny = cy
                    if id == 15:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightringUpx = cx
                        rightringUpy = cy
                    if id == 16:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightringx = cx
                        rightringy = cy
                    if id == 17:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpinkyBasex = cx
                        rightpinkyBasey = cy
                    if id == 18:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpinkyDownx = cx
                        rightpinkyDowny = cy
                    if id == 19:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpinkyUpx = cx
                        rightpinkyUpy = cy
                    if id == 20:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        rightpinkyx = cx
                        rightpinkyy = cy

            if results.multi_handedness[0].classification[0].label == "Right":  # actually left hand since it's flipped
                hand = results.multi_hand_landmarks[0]
                for id, lm in enumerate(hand.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 0:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpalmbottomx = cx
                        leftpalmbottomy = cy
                    if id == 1:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftthumbbasex = cx
                        leftthumbbasey = cy
                    if id == 2:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftthumbbaseDownx = cx
                        leftthumbbaseDowny = cy
                    if id == 3:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftthumbBaseUpx = cx
                        leftthumbBaseUpy = cy
                    if id == 4:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        # print(id, cx, cy)
                        leftthumbx = cx
                        leftthumby = cy
                    if id == 5:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpointerBasex = cx
                        leftpointerBasey = cy
                    if id == 6:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpointerDownx = cx
                        leftpointerDowny = cy
                    if id == 7:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpointerUpx = cx
                        leftpointerUpy = cy
                    if id == 8:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpointerx = cx
                        leftpointery = cy
                    if id == 9:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftmiddleBasex = cx
                        leftmiddleBasey = cy
                    if id == 10:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftmiddleDownx = cx
                        leftmiddleDowny = cy
                    if id == 11:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftmiddleUpx = cx
                        leftmiddleUpy = cy
                    if id == 12:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftmiddlex = cx
                        leftmiddley = cy
                    if id == 13:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftringBasex = cx
                        leftringBasey = cy
                    if id == 14:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftringDownx = cx
                        leftringDowny = cy
                    if id == 15:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftringUpx = cx
                        leftringUpy = cy
                    if id == 16:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftringx = cx
                        leftringy = cy
                    if id == 17:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpinkyBasex = cx
                        leftpinkyBasey = cy
                    if id == 18:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpinkyDownx = cx
                        leftpinkyDowny = cy
                    if id == 19:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpinkyUpx = cx
                        leftpinkyUpy = cy
                    if id == 20:
                        cv2.circle(image, (cx, cy), 11, (225, 0, 0), cv2.FILLED)
                        leftpinkyx = cx
                        leftpinkyy = cy



            try:
                rightthumbslope = (rightthumby - rightthumbbaseDowny) / (rightthumbx - rightthumbbaseDownx)
                # print(int(rightthumbslope))
                # THUMBSUP
                if rightthumby < rightthumbBaseUpy < rightthumbbaseDowny < rightthumbbasey < rightpalmbottomy:  # handthumbsup, but no fist
                    if rightpointerx < rightpointerDownx:  # look downwards, each finger curled
                        if rightmiddlex < rightmiddleDownx:
                            if rightringx < rightringDownx:
                                if rightpinkyx < rightpinkyDownx:
                                    if rightthumby < rightpointerx:
                                        if int(rightthumbslope) <= -1:
                                            print('Thumbs up')
                                            click = False
                # THUMBSUPWITHFINGERSPLAYED
                if rightthumby < rightthumbBaseUpy < rightthumbbaseDowny < rightthumbbasey < rightpalmbottomy:  # handthumbsup, but no fist
                    if rightpointerx > rightpointerDownx:  # look downwards, each finger curled
                        if rightmiddlex > rightmiddleDownx:
                            if rightringx > rightringDownx:
                                if rightpinkyx > rightpinkyDownx:
                                    print('Thumbs up with fingers splayed')
                                    click = True
                # THUMBSDOWN
                if rightthumby > rightthumbBaseUpy > rightthumbbaseDowny > rightthumbbasey > rightpalmbottomy:  # handthumbsup, but no fist
                    if rightpointerx < rightpointerDownx:  # look downwards, each finger curled
                        if rightmiddlex < rightmiddleDownx:
                            if rightringx < rightringDownx:
                                if rightpinkyx < rightpinkyDownx:
                                    print('Thumbs Down')
                # THUMBSDOWNWITHFINGERSPLAYED
                if rightthumby > rightthumbBaseUpy > rightthumbbaseDowny > rightthumbbasey > rightpalmbottomy:  # handthumbsup, but no fist
                    if rightpointerx > rightpointerDownx:  # look downwards, each finger curled
                        if rightmiddlex > rightmiddleDownx:
                            if rightringx > rightringDownx:
                                if rightpinkyx > rightpinkyDownx:
                                    print('Thumbs Down with fingers splayed')
                # THUMBSPOINTINGINWARDWITHFISTCURLEDANDFINGERSSPLAYED
                if rightthumbx > rightthumbBaseUpx > rightthumbbaseDownx > rightthumbbasex > rightpalmbottomx:
                    if rightpointery < rightpointerDowny:  # look downwards, each finger curled
                        if rightmiddley < rightmiddleDowny:
                            if rightringy < rightringDowny:
                                if rightpinkyy < rightpinkyDowny:
                                    if int(rightthumbslope) == 0:
                                        print('Thumbs Level with fingers splayed')
                # THUMBSPOINTINGINWARDWITHFISTCURLED
                if rightthumbx > rightthumbBaseUpx > rightthumbbaseDownx > rightthumbbasex > rightpalmbottomx:
                    if rightpointery > rightpointerDowny:  # look downwards, each finger curled
                        if rightmiddley > rightmiddleDowny:
                            if rightringy > rightringDowny:
                                if rightpinkyy > rightpinkyDowny:
                                    if rightmiddley < rightpalmbottomy:
                                        if rightthumby > rightmiddley:
                                            if int(rightthumbslope) == 0:
                                                print('Thumbs Level')




            except Exception as e:
                # print(e)
                pass

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
