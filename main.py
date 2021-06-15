import time
#import plyer
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drink Water now",
            message = "drink 2.7 litres",
            app_icon = "icon.ico",
            timeout = 5
            )
        time.sleep(60)
        
        
    


