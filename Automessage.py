# WE are writting short python code to automate the chat
# we will write the code which will send same msg 1000 times or more
#python code
import pyautogui as dk
import time

message = "I Love You" #you can write any message here
count = 1
time.sleep(1)

for i in range(10): #you can write any no here -this will repeat msg upto that no
     dk.typewrite(message + " " + str(count))
     dk.press('Enter')
     count = count + 1

property.press('Enter')
#now run the code and open the chat box where you want to send and press enter there
