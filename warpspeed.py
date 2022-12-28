from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"C:\Users\Rithesh kunchakuri\Github\chromedriver.exe")
browser.get("https://warpspeed.csivit.com/Game")

'''nextButton = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/button")
nextButton[0].click()

loginBox = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
loginBox.send_keys('rithesh.kunchakuri2020@vitstudent.ac.in')

nextButton = browser.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
nextButton[0].click()

passWordBox = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
passWordBox.send_keys('<password>')

nextButton = browser.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
nextButton[0].click()
'''
time.sleep(2)

for i in range(10000):
    stage =  browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/h1 ").text
    score =  browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[4]/h1 ").text
    if stage == "RD-01" or stage == "RD-02"  :   
        time.sleep(3)
        word = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]").get_attribute("id")
        print(word)
        python_button = browser.find_elements_by_xpath("//*[@id='userinputfield']/input")[0]
        python_button.send_keys(word)
        python_button.send_keys(Keys.ENTER)
    elif  stage == "RD-03" or stage == "RD-04" :
        time.sleep(1)
        word = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]").get_attribute("id")
        print(word)
        python_button = browser.find_elements_by_xpath("//*[@id='userinputfield']/input")[0]
        python_button.send_keys(word)
        python_button.send_keys(Keys.ENTER)
    else:
        word = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]").get_attribute("id")
        print(word)
        python_button = browser.find_elements_by_xpath("//*[@id='userinputfield']/input")[0]
        python_button.send_keys(word)
        python_button.send_keys(Keys.ENTER)




  
