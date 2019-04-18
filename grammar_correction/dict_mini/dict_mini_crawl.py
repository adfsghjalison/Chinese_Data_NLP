# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

url = 'http://dict.mini.moe.edu.tw/'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

def css(i):
    return driver.find_element_by_css_selector(i)

def css2(i):
    return driver.find_elements_by_css_selector(i)

# click "字音索引"
css('a[title="字音索引"]').click()

# switch to pinyin frame
driver.switch_to.frame(1)

d1 = {}
d2 = {}
c1_n = len(css2('.bst_pin1 a'))

# get c2
def get_c2(j):
    c2 = css2('.bst_pin2 a')[j]
    c2_text = c2.text
    c2.click()

    # get characters
    c3 = [k.text for k in css2('.bst_pin3 a')]
    for k in c3:
        d2[k] = c2_text
    d1[c2_text] = c3
            
    driver.back()
    driver.switch_to.frame(1)

# get c1
def get_c1(i, start=0):
    c1 = css2('.bst_pin1 a')[i]
    c1.click()

    c2_n = len(css2('.bst_pin2 a'))
    for j in range(start, c2_n):
        get_c2(j)
        print("{}/{} : {}/{}".format(i, c1_n, j, c2_n))
    driver.back()
    driver.switch_to.frame(1)

# save files
def save():
	json.dump(d1, open('pinyin_character', 'w'))
	json.dump(d2, open('character_pinyin', 'w'))

# recover process
def recover(i, j):
    driver.back()
    driver.switch_to.frame(1)
    for k in range(i, c1_n):
        get_c1(k, j if k == i else 0)
	save()

for i in range(c1_n):
    get_c1(i)
save()
