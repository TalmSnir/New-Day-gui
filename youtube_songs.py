from selenium import webdriver
import time
from random import choice


artist_list = ['Jeff Buckley', 'Harry Styles', 'Foo Fighters']
# !expend the list of artist


def open_youtube():
    driver = webdriver.Chrome('.\chromedriver')
    driver.get('https://www.youtube.com/')
    driver.maximize_window()
    return driver


def chose_artist(driver):
    chosen_artist = choice(artist_list)
    search_box = driver.find_element_by_id('search')
    search_box.send_keys(chosen_artist)

    search_btn = driver.find_element_by_id('search-icon-legacy')
    search_btn.click()
    time.sleep(1)
    return chosen_artist


def song_picker(chosen_artist, driver):
    video_titles = driver.find_elements_by_partial_link_text(chosen_artist)
# ? how to get only the titles for the songs and not the youtube channel name
# ? maybe using youtube API

    chosen_video_btn = choice(video_titles)
    chosen_video_btn.click()
    time.sleep(240)
    driver.quit()


def play_song():
    driver = open_youtube()
    chosen_artist = chose_artist(driver)
    song_picker(chosen_artist, driver)
