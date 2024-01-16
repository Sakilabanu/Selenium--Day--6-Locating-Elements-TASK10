from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

chrome_service = ChromeService(r"C:\Users\sahbi\OneDrive\Desktop\PyCharm Community Edition 2023.2.5\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)

driver.get("https://www.instagram.com/guviofficial/")


from selenium.webdriver.common.by import By
import time
time.sleep(4)

textdata=driver.find_element(By.CLASS_NAME,"_ac2a").text
print(textdata)



from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

chrome_service = ChromeService(r"C:\Users\sahbi\OneDrive\Desktop\PyCharm Community Edition 2023.2.5\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)

driver.get("https://www.instagram.com/guviofficial/")


from selenium.webdriver.common.by import By
import time
time.sleep(2)

time.sleep(2)
textdata=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]').text
print(textdata)