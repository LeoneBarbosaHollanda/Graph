import cv2
import numpy as np
import pyautogui
import time



# Carregando a imagem do template (a tela de "Game Over", por exemplo)
template = cv2.imread('MARIOF.jpg', 0)
w, h = template.shape[::-1]

# Verifica se o template foi carregado corretamente




# Aplicando a correspondência de template






time.sleep(10)  
pyautogui.keyDown('k')
pyautogui.keyUp('k')
pyautogui.keyDown('d')
while(True):
    screenshot = pyautogui.screenshot()
    gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    if len(loc[0]) > 0:
        print("Imagem encontrada na tela!")
        pyautogui.keyDown('f1')
        pyautogui.keyUp('f1')
    pass