from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
                title="*** Take Rest ***",
                message = "Rest is vital for better mental health",
                timeout = 5)

        time.sleep("time period in seconds")
