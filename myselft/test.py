from datetime import date, datetime

robot_brain = ""
while True :
	you = input ()
	if "hello" in you :
		robot_brain = "Hello Cookies Dan"
	elif "time" in you:
		now =datetime.now()
		robot_brain = now.strftime("%H hour %M minutes %S seconds")
	elif  "date" in you:
			today = date.today()
			robot_brain = today.strftime("Today is %B %d, %Y")
	elif "president of Viet Nam" in you:
		robot_brain = "Pham Minh Chinh"
	elif "call" in you:
		robot_brain = "Your name is Huy, your nickname is Cookies"
	elif "bye" in you:
		robot_brain ="Goodbye, Have a nice day to you"
		print (robot_brain)
		break
	else :
		robot_brain = "I don't understand, pls tell me again"
	print ("Robot : "+robot_brain)
	