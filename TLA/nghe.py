import speech_recognition
from gtts import gTTS
import os
from datetime import date, datetime
from playsound import playsound 
bot_brain= "" #Ban đầu chưa học gì nên não chưa có thông tin
bot_ear = speech_recognition.Recognizer()#Siri nghe
with speech_recognition.Microphone() as mic:
    print("\nSiri: I'm listening")
    #audio = bot_ear.listen(mic)
    audio = bot_ear.listen(mic) #Siri nghe trong vòng 3 giây sau đó tắt Mic, tránh treo máy do bật Mic lien tục
    print("\nSiri: ....")
try:
    you = bot_ear.recognize_google(audio,language='vi-VN')# nó sẽ lấy giọng của chị Google
    print("\nYou: "+you)   
except:
    bot_brain ="Tôi không hiểu bạn nói gì."
    print("\nSiri: "+you)

if "Thái Khôi" in you:
	bot_brain="Một thằng chó ăn cức, bê đê chúa, bóng ngầm Trà Vinh"
	print (bot_brain)
elif  "ngày" in you:
	today = date.today()
	bot_brain = today.strftime("hôm nay là tháng %B ngày %d, năm %Y")
	print(bot_brain)
elif "giờ" in you:
	now =datetime.now()
	bot_brain = now.strftime("%H giờ %M phút %S giây")
	print(bot_brain)
now =datetime.now()
bot_brain = now.strftime("%H giờ %M phút %S giây")
print(bot_brain)
tts = gTTS(str(bot_brain),tld='com.vn',lang='vi')
tts.save("hello.mp3")
playsound("hello.mp3")
