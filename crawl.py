# -*- coding: utf-8 -*-
# License: MIT
# Based on https://ch.nicovideo.jp/drcn114514/blomaga/ar1370794

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, datetime, json, traceback, requests
import chromedriver_binary

interval = 7

userID = "*******"
until = datetime.datetime.now() + datetime.timedelta(days=1)

since = until - datetime.timedelta(days=interval)

def random_sleep():
    time.sleep(7 + random.random() * 1)

browser = webdriver.Chrome()

xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div'

count = 0

try :
    while(True) :
        all_tweets = dict()

        url = "https://twitter.com/search?q=(from%3A" + userID + ")%20since:" + since.strftime('%Y-%m-%d') + "%20until:" + until.strftime('%Y-%m-%d') + "&src=typed_query&f=live"
        browser.get(url)
        
        random_sleep()

        tweets = browser.find_elements_by_xpath(xpath)
        for tweet in tweets:
            try:
                date = tweet.find_element_by_xpath('.//div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time').get_attribute('dateTime')
                all_tweets[date] = tweet.get_attribute('innerHTML')
            except:
                pass
            
        number = len(tweets)

        if len(tweets) == 0:
            count += 1
            if count >= 10:
                print('no more tweets')
                break
        else:
            count = 0

        while(True) :
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight * 2);")
            random_sleep()
            num_old = len(all_tweets)
            
            tweets = browser.find_elements_by_xpath(xpath)
            for tweet in tweets:
                try:
                    date = tweet.find_element_by_xpath('.//div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time').get_attribute('dateTime')
                    all_tweets[date] = tweet.get_attribute('innerHTML')
                except:
                    pass
                
            if len(all_tweets) == num_old:
                break

        print('since:' + since.strftime('%Y-%m-%d') + '/until:' + until.strftime('%Y-%m-%d') + ' tweets : ' + str(number))
        for k, v in all_tweets.items():
            print(k)
            print(v)

        since = since - datetime.timedelta(days=interval)
        until = until - datetime.timedelta(days=interval)

except :
    traceback.print_exc()

browser.quit()
