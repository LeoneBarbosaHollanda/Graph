import cv2
import numpy as np
import pyautogui
import time
import networkx




template = cv2.imread('DEAD.png', 0)
template2 = cv2.imread('TIME.png', 0)
aux=0

w, h = template.shape[::-1]



time.sleep(5)  
pyautogui.keyDown('k')
pyautogui.keyUp('k')
pyautogui.keyDown('d')
time.sleep(1)
while(True):
    
    screenshot = pyautogui.screenshot()
    gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(gray, template2, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    loc2 = np.where(res2 >= threshold)

    if len(loc[0]) > 0:

        print("Imagem encontrada na tela!")
        pyautogui.keyDown('f1')
        pyautogui.keyUp('f1')
    if len(loc2[0]) > 0 and aux == 0:
        print("Imagem2 encontrada na tela!")
        pyautogui.keyDown('shift')
        pyautogui.keyDown('f1')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('f1')
        aux=1
    pass