import time
from plyer import notification

if __name__ == '__main__':
  while True:
    notification.notify(
      app_name = "EDITH",
      title = "Hydration",
      message = "There you go Yash! It's time for some Hydration",
      timeout = 3,
      app_icon = "D:\\Programming\\Python\\Projects\\HYDRATION_REMAINDER\\icon.ico"
    )
    time.sleep(2700)
