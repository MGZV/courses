import pyttsx3
import time


s = pyttsx3.init()
data = "Время вышло, нужен отдых"
data1 = "Пора садится за учёбу"

s.say(data)
time.sleep(2400)
s.say(data1)



