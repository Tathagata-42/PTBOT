from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api , win32con

#X: 486 Y:  771 RGB: (  1,  36,  86)  
#X: 615 Y:  771 RGB: (  1,  36,  86)  
#X: 722 Y:  771 RGB: (  1,  36,  86)  
#X: 848 Y:  771 RGB: (  1,  36,  86)  

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)#pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(486,771)[0] == 0:
        click(486,771)
    if pyautogui.pixel(615,771)[0] == 0:
        click(615,771)
    if pyautogui.pixel(722,771)[0] == 0:
        click(722,400)
    if pyautogui.pixel(48,771)[0] == 0:
        click(848,400)
