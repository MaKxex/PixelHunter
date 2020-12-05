import time
import os, sys
try:
    import pyautogui
except Exception as e:
    print(e)
    os.system('pip install pyautogui')
    sys.exit("Restart the script.")

n = input("Сколько раз вывести координаты?")
i = 0
time.sleep(2)
while i < int(n):
    print(str(i) + str(pyautogui.position()))
    time.sleep(2)
    i +=1
