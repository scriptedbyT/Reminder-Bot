import pyautogui, time, datetime 
# import schedule

time.sleep(2) 
n = int(input("Enter any number:"))

for x in range(n): 
	
	# to display the time at which the message is sent 
	print(datetime.datetime.now()) 
	# POP UP
	pyautogui.alert("Reminder: Take medicine!")
	# Confirm
	pyautogui.confirm("Reminder: Take medicine!")
	# Prompt
	pyautogui.prompt('Reminder: Take medicine!')
	pyautogui.typewrite("Reminder: Drink Water!") 
	pyautogui.press("enter") 
	time.sleep(1) 

	print(datetime.datetime.now()) 

	pyautogui.typewrite("Reminder: Take medicine!") 
	pyautogui.press("enter") 
	time.sleep(1) 

	print(datetime.datetime.now()) 

	pyautogui.typewrite("Reminder: Take the dog for a walk!") 
	pyautogui.press("enter") 
	time.sleep(1) 

	print(datetime.datetime.now()) 

	pyautogui.typewrite("Reminder: Drink water!") 
	pyautogui.press("enter") 
	time.sleep(1) 

	print(datetime.datetime.now()) 

	pyautogui.typewrite("Reminder: Drink water!") 
	pyautogui.press("enter") 
	time.sleep(1) 

	# schedule.every(60).minutes.do(function)
