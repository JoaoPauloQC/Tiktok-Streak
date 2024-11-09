import pyautogui
import time



# entrar no tiktok

pyautogui.press('winleft')
pyautogui.write('tiktok')
pyautogui.press('enter')
time.sleep(6)
pyautogui.press('f11')
pyautogui.click('imgs/tiktokmsg.png')
time.sleep(5)


#streak
time.sleep(5)
print('to buscando')

pyautogui.click('')
time.sleep(8)
pyautogui.click('imgs/send2.png')
pyautogui.write('bot de sequência')
pyautogui.press('enter')

time.sleep(5)
