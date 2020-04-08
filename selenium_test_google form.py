
from selenium import webdriver
import time

'''
Python 3.7.6
Win 10
pip install selenium

Agenda
1. Download firefox browser
2. Download driver
3. Catch the span
4. Send the msg
5. Send the form
6. Close the browser
'''



if __name__ == '__main__':
    driverpath = "C:\\Users\\Kuo\\Downloads\\geckodriver.exe"
    driver = webdriver.Firefox(executable_path=driverpath)
    url = "https://forms.gle/gcK7MiuuShP9gCwV7"
    driver.get(url)
    
  
    name = driver.find_element_by_xpath("//input[@name='entry.7180544']")
    name.send_keys("1234")
    time.sleep(0.1)
    driver.find_element_by_xpath("//*[contains(text(), '繼續')]").click()
    time.sleep(0.1)
    name = driver.find_element_by_xpath("//input[@name='entry.665011496']")
    name.send_keys("5678")
    driver.find_element_by_xpath("//*[contains(text(), '提交')]").click()
    time.sleep(1)
    #close the browser
    driver.close()
