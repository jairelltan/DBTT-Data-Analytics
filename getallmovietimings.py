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
 # Returns an array of all movie screenings on the day itself. Each object consist of location, moviename, timing, href, genre, language, rating, runtime, opening
def obtain_all_movietimings():

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

                genre = driver.find_element(By.XPATH, "//div[contains(text(),'GENRE')]/following-sibling::div").text
                language = driver.find_element(By.XPATH, "//div[contains(text(),'LANGUAGE')]/following-sibling::div").text
                rating = driver.find_element(By.XPATH, "//div[contains(text(),'RATING')]/following-sibling::div").text
                runtime = driver.find_element(By.XPATH, "//div[contains(text(),'RUNTIME')]/following-sibling::div").text
                opening = driver.find_element(By.XPATH, "//div[contains(text(),'OPENING')]/following-sibling::div").text

                timing_datetime = datetime.fromisoformat(timing)

                #yes technically this can be placed above but i thought of limiting it to only one day later
                if timing_datetime.date() == current_date:
                    showtimes_list.append({
                        "location": location,
                        "movie_name": movie_name,
                        "timing": timing,
                        "href": href,
                        "genre": genre,
                        "language": language,
                        "rating": rating,
                        "runtime": runtime,
                        "opening": opening
                })

        showtimes_list.sort(key=lambda x: datetime.fromisoformat(x['timing']))
        driver.quit()
    return showtimes_list
