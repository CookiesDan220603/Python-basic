import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear= speech_recognition.Recognizer()
robot_brain =""

while True:
	with speech_recognition.Microphone() as mic:
		print ("Robot : I'm listening...")
		audio =robot_ear.listen(mic)
	print ("Robot:...")
	try :
		you = robot_ear.recognize_google(audio)
	except :
		you ="..."
	print ("You : "+you)

	if "hello" in you :
		robot_brain = "Hello Cookies Dan"
	elif "time" in you:
		now =datetime.now()
		robot_brain = now.strftime("%H hour %M minutes %S seconds")
	elif  "date" in you:
			today = date.today()
			robot_brain = today.strftime("Today is %B %d, %Y")
	elif "President of Vietnam" in you:
		robot_brain = "Pham Minh Chinh"
	elif "call" in you:
		robot_brain = "Your name is Huy, your nickname is Cookies"	
	elif "bye" in you:
		robot_brain = "Bye Cookies Dan"
		print ("Robot : "+robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else :
		robot_brain ="I don't understand, pls tell me again"
	print ("Robot : "+robot_brain)

	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()