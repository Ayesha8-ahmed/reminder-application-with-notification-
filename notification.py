import time
from plyer import notification

if __name__ == '__main__':
    while True:
        title = input("\nTitle of Reminder: ")
        msg = input("Message: ")
        minutes = float(input("How many minutes: "))

        seconds = minutes * 60

        notification.notify(
            title=title,
            message=msg,
            timeout=10
        )

        print("\nReminder set successfully!\n")
        time.sleep(seconds)