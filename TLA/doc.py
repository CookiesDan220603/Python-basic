import os
from gtts import gTTS
from playsound import playsound 
tts = gTTS('Xin chào các bạn',tld='com.vn',lang='vi')
tts.save("hello.mp3")
playsound("hello.mp3")



