import time
def countdown(t):
  while t:
    mins, sec = divmod(t, 60)
    timer = '{:05d}:{:05d}'.format(mins,sec)
    time.sleep(1)
    t -= 1
    print("The time's up")
t= input("Enter the time in sec")

countdown(int(t))
