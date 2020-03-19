#!/usr/bin/env python3

from selenium import webdriver
import requests
import time
browser = webdriver.Firefox()

browser.get('https://anichart.net/Spring-2020')
time.sleep(25)

elem = browser.find_element_by_xpath("""//div[@class='card-list']//div[1]//a[1]//div[2]""")
# elem.send_keys('anichart')
elem.click()

#FUNCOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO con el rel PATH del xpath
#//body[@class='site-theme-default']/div[@id='app']/div[@class='main-content']/div[@class='chart-view']/div/section[@class='section loaded']/div[@class='card-list']/div[1]/div[1]/div[2]/div[1]/div[1]
# time.sleep(5)

# video = browser.find_element_by_css_selector('h3.LC20lb DKV0Md')
