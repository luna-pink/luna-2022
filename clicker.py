import mouse
from time import sleep

# if "G" is pressed then mouse.click()
while True:
    if mouse.is_pressed(button="left"):
        mouse.click()
        print("Clicked")
        sleep(0.05)
        mouse.click()
        print("Clicked 1")
        sleep(0.05)
        mouse.click()
        print("Clicked 2")
        sleep(0.05)
        mouse.click()
        print("Clicked 3")
    else:
        print("Not clicked")
    sleep(0.01)