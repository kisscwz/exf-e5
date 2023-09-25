#仅用于保持活跃
import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, sec)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("时间到！专注时间结束。")

if __name__ == "__main__":
    minutes = int(input(120))
    focus_timer(minutes)
