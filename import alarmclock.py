import datetime
import time
import winsound # work on window

print("----Alarm Clock-----")
alarm_time = input("Enter alarm (HH:MM:SS) in 24-hour format: ")

print(f"Alarm set for {alarm_time}...")

while True:
    current_time = datatime.datatime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up! Alarm ringing...")

        #Beep sound
        for i in range(5):
            winsound.Beep(1000, 500) #(frequency, duration)
            break

time.sleep(1)