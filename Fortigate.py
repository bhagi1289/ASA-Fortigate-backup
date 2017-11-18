from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from datetime import datetime
import time
import os

now = datetime.now()
backup_time = now.strftime("%Y-%m-%d")
directory = os.getcwd()+"\\Customer_"+backup_time
print directory
if not os.path.exists(directory):
	os.makedirs(directory)

host = "proxy.com"# Enter your custome proxy here
port = "8080"
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", host)
profile.set_preference("network.proxy.http_port", port)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.useDownloadDir", True )
profile.set_preference("browser.download.dir", directory)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/octet-stream')


driver = webdriver.Firefox(firefox_profile=profile)
driver.implicitly_wait(30)
driver.get("")#Give URL here 

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("secretkey")

username.send_keys("")#username
password.send_keys("")#password
driver.find_element_by_id("login_button").click()
time.sleep(2)

#------------------ LOGIN TIME WINDOWS HANDLING--------------------------------------------

#remind =driver.find_elements_by_xpath("//*[contains(text(), 'Remind me later')]")
#print(dir(remind))
#remind[0].click()
login = driver.find_elements_by_xpath("//*[contains(text(), 'Login Read-Write')]")
login[0].click()
fortimanager= driver.find_elements_by_xpath("//*[contains(text(), 'Yes')]")
fortimanager[0].click() 

#--------------------------------------------------------------------------------------------	

time.sleep(3)
driver.switch_to.frame(driver.find_element_by_name("embedded-iframe"))
backup = driver.find_elements_by_xpath("//*[contains(text(), '[Backup]')]")
backup[0].click()
driver.switch_to.default_content()
#time.sleep(3)
ok = driver.find_elements_by_xpath("//*[contains(text(), 'OK')]")
ok[0].click()
time.sleep(3)
driver.quit()	
