from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# Obtain all links from each of the movies from the cathay main page
# Accepts no parameters
# Returns a list of all links to each movie page individually.
def getallmovies():

    #havent tested if relative path works, yall use ur own path bah
    cService = webdriver.ChromeService(executable_path=r'C:\Users\jai\Desktop\DBTT\DBTT\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=cService)

    driver.get('https://www.cathaycineplexes.com.sg/')

    movie_containers = driver.find_elements(By.CSS_SELECTOR, ".movie-container")

    movies_list = []

    for movie in movie_containers:

        movie_link = movie.find_element(By.TAG_NAME, "a").get_attribute("href")
        movies_list.append(movie_link)

    driver.quit()
    return movies_list
