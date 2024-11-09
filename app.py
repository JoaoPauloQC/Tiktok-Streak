import pyautogui
import time

#lista de users
user1 = ''
user2 = ''
user3 = ''
user_list = [
    
    user1,
    user2,
    user3

]
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

for user in user_list:

    print('to buscando')

    pyautogui.click(user)
    time.sleep(4)
    pyautogui.click('imgs/test2.png')
    pyautogui.write('bot de sequência')
    pyautogui.press('enter')

    time.sleep(3)
