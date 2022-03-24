import time
from bangGood import BangGood

automation = BangGood()
automation.goToPage()
time.sleep(5)

try:
    automation.cancelPopUp()
except:
    print("No Pop up Found")

automation.sign_up_click()

time.sleep(5)
automation.input_email("helloworld18@yahoo.com")
automation.input_password("saiah22%%")
automation.submit()