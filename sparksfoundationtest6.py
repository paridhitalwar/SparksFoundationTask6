from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
  

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.thesparksfoundationsingapore.org/')
print ("Opened Sparks Foundation")
sleep(2)
  
Policies_and_Code = driver.find_element_by_xpath('//a[normalize-space()="Policies and Code"]') #Element 1
Policies_and_Code.click()
sleep(1)
Policies = driver.find_element_by_xpath('//a[normalize-space()="Policies"]') #Element 2
Policies.click()
sleep(2)
driver.find_element_by_xpath('//a[normalize-space()="Programs"]').click() #Element 3
sleep(1)
driver.find_element_by_xpath('//ul[@class="dropdown-menu"]//a[normalize-space()="Student Mentorship Program"]').click() #Element 4
sleep(1)
driver.find_element_by_xpath('//a[normalize-space()="Programs"]').click() #Element 5
sleep(1)
driver.find_element_by_xpath('//ul[@class="dropdown-menu"]//a[normalize-space()="Student Scholarship Program"]').click() #Element 6
sleep(1)
driver.find_element_by_xpath('//a[normalize-space()="LINKS"]').click() #Element 7
sleep(1)
driver.find_element_by_xpath('//a[normalize-space()="Salient Features"]').click() #Element 8
sleep(1) 
driver.find_element_by_xpath('//a[normalize-space()="Contact Us"]').click() #Element 9
sleep(1)
driver.find_element_by_xpath('//a[normalize-space()="About Us"]').click() #Element 10
sleep(7)
driver.quit()
