from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
#最大化窗口
driver.maximize_window()
driver.get('http://mail.163.com/')
sleep(2)
#切换到表单
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys('huangyajiao1995')
driver.find_element_by_name("password").send_keys('huang19951223')
driver.find_element_by_id("dologin").click()

