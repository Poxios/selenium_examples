import selenium.webdriver as webdriver
import time
import winsound as ws
import random

# Initializing Browser
driver = webdriver.Chrome()
i = 1
j = 1


def beepsound():  # Define BeepSound Function
    freq = 1000
    dur = 1000
    ws.Beep(freq, dur)


# Beep Test
beepsound()


while i < 10:  # Main Running
    try:
        driver.get('Your URL')
        mask = driver.find_element_by_partial_link_text("Your TEXT")

        # If found
        while j < 10:
            beepsound()
            print("Found")
            time.sleep(1)

    # If failed
    except Exception as e:
        now = time.gmtime(time.time())
        print("Not Found", now.tm_hour, now.tm_min, now.tm_sec)
        time.sleep(random.randrange(600, 900))
