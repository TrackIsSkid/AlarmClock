
# import required module
import schedule 
import playsound
import time 
from playsound import playsound


Path = input ('Input The path to the sound (ex: C:\\Path\\To\\The\\Song\\song.wav(if an error then put two \\ like in the ex): ')
Time = input (' What time do you wanna wake up:')
print('alarm set till ' + Time )

def sound():
    playsound(Path)

schedule.every().day.at(Time).do(sound)
while True:
    schedule.run_pending()
    time.sleep(1)
