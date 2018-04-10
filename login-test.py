#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:01:52 2018

@author: alex
"""

import mechanize
import re
import time

from selenium import webdriver

browser = webdriver.Firefox()
 
#mechanize can not work correctly
def login():
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.open("https://www.linkedin.com/")
        browser.select_form(class_="login-form")
        #browser.select_form(name="login-form")
        
        browser["session_key"] = "13225859033"
        browser["session_password"] = "wj16830223"
        response = browser.submit()
        
        print response.read()
        
#selenium can work        
def selelogin(url):
    
    
       
        browser.get(url)
        
        loginInput = browser.find_element_by_name('session_key')
        loginInput.send_keys('13225859033')
        passwd = browser.find_element_by_name('session_password')
        passwd.send_keys('wj16830223')
        
        btn = browser.find_element_by_id('login-submit')
        btn.click()
        #networks()
        time.sleep(3)
        
        # can not work effectively
        #networkicon = browser.find_element_by_class_name('nav-item__icon')
        #networkicon = browser.find_element_by_id('mynetwork-nav-item')
        #networkicon = browser.find_element_by_class_name('nav-item__link nav-item__link--underline')
        
        networkicon = browser.find_element_by_link_text('My Network')
        networkicon.click()
        
        time.sleep(3)
        seeall = browser.find_element_by_link_text('See all')
        #eeall = browser.find_element_by_id('ember2962')
        seeall.click()
        
        time.sleep(3)
        
        connects = browser.find_element_by_class_name('ember-view')
        print(connects.text)
        #for i in connects:
         #   print(i)
        
        
        

def networks():
    browser.get('http://www.linkedin.com/feed/')
    networkicon = browser.find_element_by_class_name('nav-item__link nav-item__link--underline js-nav-item-link active')
    networkicon.click()
    
    
def close():
    browser.close()
    
                
        
        
        

if __name__ == '__main__':
    myurl ='https://www.linkedin.com/'
    #newspider(myurl)
    selelogin(myurl)
    #fetchfriend(myurl)
