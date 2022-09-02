import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver') 
driver.get("http://localhost:8116")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.XPATH, "//*[@id='login']/div[2]/div[2]/input")
elemento2.clear()
elemento2.send_keys("password")

driver.find_element(By.XPATH, "//*[@id='login']/div[3]/div/input").click()
# redirecciono otra ves a la web, porque redirecciona luego del login a localhost:80
driver.get("http://localhost:8116")
time.sleep(1)

elemento3 = driver.find_element(By.XPATH, "//*[@id='CreateTicketInQueue']/div[1]/input")
elemento3.click()
time.sleep(1)

elemento4 = driver.find_element(By.XPATH, "//*[@id='TitleBox--_Ticket_Create_html--messagedetails----Q3JlYXRlIGEgbmV3IHRpY2tldCBpbiBHZW5lcmFs---0']/div/div/div[4]/div[2]/input")
elemento4.send_keys("Selenium RT")

elemento5 = driver.find_element(By.XPATH, "//*[@id='SubmitTicket']/div[2]/input")
elemento5.click()

driver.close()