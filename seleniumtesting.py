from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("file:///Users/giladouzan/Downloads/tip_calc%202/index.html")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="musicQual").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = "9"
assert expected == actual
# if expected == actual:
#     print("All good")
# else:
#     print("You have ruined the tip")

sleep(1000)