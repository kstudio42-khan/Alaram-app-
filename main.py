import time
import os
import random

def vibrate():
    os.system("termux-vibrate -d 1000")

def notify():
    os.system("termux-notification --title 'ALARM' --content 'WAKE UP NOW!'")

def math_challenge():
    a = random.randint(10, 50)
    b = random.randint(10, 50)
    return a, b, a + b

def alarm():
    while True:
        vibrate()
        notify()

        a, b, ans = math_challenge()
        print(f"Solve to stop alarm: {a} + {b} = ?")

        try:
            user = int(input("> "))
            if user == ans:
                print("✅ Alarm stopped")
                break
        except:
            pass

        time.sleep(1)

print("⏰ Alarm will start in 5 seconds...")
time.sleep(5)
alarm()
