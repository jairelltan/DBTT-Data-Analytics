from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from getallmovies import getallmovies

 # Obtain all links to each of the available movies timings for each movie.
 # Accepts no parameters
 # Returns a list of all links to each movie timings for all movies for that day itself. Ideally sorted by chronological order
def obtain_all_moviedates():

    movielist = getallmovies()
    print(movielist)
    showtimes_list = []
    current_date = datetime.now().date()


    for movie in movielist:

        cService = webdriver.ChromeService(executable_path=r'C:\Users\jai\Desktop\DBTT\DBTT\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=cService)

        driver.get(movie)

        links = driver.find_elements(By.CSS_SELECTOR, "a[onclick^='saveShowtimeToLocalStorage']")
        
        for link in links:
            onclick_data = link.get_attribute('onclick')
            
            if "saveShowtimeToLocalStorage" in onclick_data:
                start = onclick_data.find("(") + 1
                end = onclick_data.rfind(")")
                params = onclick_data[start:end].split(", ")
            
                location = params[0].strip("'")  
                movie_name = params[1].strip("'")  
                timing = params[2].strip("'")  
                href = link.get_attribute("href")  

                timing_datetime = datetime.fromisoformat(timing)
                if timing_datetime.date() == current_date:
                    showtimes_list.append({
                        "location": location,
                        "movie_name": movie_name,
                        "timing": timing,
                        "href": href
                })

        showtimes_list.sort(key=lambda x: datetime.fromisoformat(x['timing']))
        driver.quit()
    return showtimes_list

print(obtain_all_moviedates())