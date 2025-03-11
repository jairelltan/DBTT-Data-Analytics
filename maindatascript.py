from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time
import os
import csv
from datetime import datetime, timedelta
from getallmovietimings import obtain_all_movietimings

#actual calling of the script. call when necessary.
movie_timings = obtain_all_movietimings()

from datetime import datetime, timedelta

#this functions checks every 30 seconds if there is a movie screening in the next 5mins/before 5 mins. It cannot be an exact time because it means that the user needs to activate the script exactly at 00 seconds + any delays to the opening of the website can prevent the checks from happening at exactly 00 seconds. I think this is a fair trade.
def check_and_open_movie_timing():
    now = datetime.now()
    for movie in movie_timings:
        movie_timing = datetime.fromisoformat(movie['timing'])
        if abs((movie_timing - now).total_seconds()) <= 300:  
            print(f"Movie '{movie['movie_name']}' at {movie['timing']} is showing now. Opening the movie link...")
            #delete the movie from the original array. (Prevents duplicate entries)
            movie_timings.remove(movie) 
            return movie
    print('no movie as of'+ str(now))
    return None

def get_details():
    now = datetime.now()
    end_of_day = datetime(now.year, now.month, now.day, 23, 59, 59)
    current_date_str = now.strftime('%Y-%m-%d')
    csv_file = f"{current_date_str}.csv"
    file_exists = os.path.isfile(csv_file)

    if not file_exists:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Location", "Movie Name", "Timing", "Is Premium", "Href", 
                "Genre", "Language", "Rating", "Runtime", "Opening",
                "Occupied Regular", "Not Occupied Regular",
                "Occupied Couple", "Not Occupied Couple",
                "Occupied Wheelchair", "Not Occupied Wheelchair",
                "Occupied Wave", "Not Occupied Wave",
                "Total Occupied", "Total Not Occupied", "Total Seats", "Occupancy Rate"
            ])

    while True:
        # script ends ends at 12am
        if datetime.now() >= end_of_day:
            print("End of the day reached. Stopping the script.")
            break
        movie = check_and_open_movie_timing()
    
        # if a movie is found in the time interval, open it and count the stuff. you can get the other non seat data by calling movie['location'] etc.
        if movie:
            try:
                # Setup WebDriver with error handling
                cService = webdriver.ChromeService(executable_path=r'C:\Users\jai\Desktop\DBTT\DBTT\chromedriver-win64\chromedriver-win64\chromedriver.exe')
                driver = webdriver.Chrome(service=cService)

                # Try to access the movie URL
                try:
                    driver.get(movie['href'])
                except WebDriverException as e:
                    print(f"Failed to open {movie['href']} due to error: {e}")
                    driver.quit()
                    continue  # Skip to the next movie


                seats = driver.find_elements(By.CLASS_NAME, 'cell')

                occupied_regular_count = 0
                not_occupied_regular_count = 0

                occupied_couple_count = 0
                not_occupied_couple_count = 0

                occupied_wheelchair_count = 0
                not_occupied_wheelchair_count = 0

                occupied_wave_count = 0
                not_occupied_wave_count = 0

                occupied_total_count = 0
                not_occupied_total_count = 0
                total_count = 0

                is_premium = False
                occupancy_rate = 0

                # URLs for different seat types. I found out this is the easiest way to find all the seats (the status method doesnt work)
                regular_seat_url = "https://www.cathaycineplexes.com.sg/images/single-seat.png"
                regular_seat_sold_url = "https://www.cathaycineplexes.com.sg/images/single-seat-sold.png"

                couple_left_url = "https://www.cathaycineplexes.com.sg/images/couple-left.png"
                couple_right_url = "https://www.cathaycineplexes.com.sg/images/couple-right.png"
                couple_left_sold_url = "https://www.cathaycineplexes.com.sg/images/couple-left-sold.png"
                couple_right_sold_url = "https://www.cathaycineplexes.com.sg/images/couple-right-sold.png"

                wheelchair_url = "https://www.cathaycineplexes.com.sg/images/wheelchair.png"
                wheelchair_sold_url = "https://www.cathaycineplexes.com.sg/images/wheelchair-sold.png"

                #niche ones
                wave_left_url = "https://www.cathaycineplexes.com.sg/images/w-left.png"
                wave_right_url = "https://www.cathaycineplexes.com.sg/images/w-right.png"
                wave_left_sold_url = "https://www.cathaycineplexes.com.sg/images/w-left-sold.png"
                wave_right_sold_url = "https://www.cathaycineplexes.com.sg/images/w-right-sold.png"


                for seat in seats:
                    style = seat.get_attribute('style')  
                    # status = seat.get_attribute('status')  
                    
                    # Check the background image URL and status for each seat type
                    if regular_seat_url in style:
                        not_occupied_regular_count += 1
                        not_occupied_total_count += 1
                    elif regular_seat_sold_url in style:
                        occupied_regular_count += 1
                        occupied_total_count += 1

                    elif couple_left_url in style or couple_right_url in style:
                        not_occupied_couple_count += 1
                        not_occupied_total_count += 1
                    elif couple_left_sold_url in style or couple_right_sold_url in style:
                        occupied_couple_count += 1
                        occupied_total_count += 1

                    elif wheelchair_url in style:
                        not_occupied_wheelchair_count += 1
                        not_occupied_total_count += 1
                    elif wheelchair_sold_url in style:
                        occupied_wheelchair_count += 1
                        occupied_total_count += 1

                    #Niche Ones
                    elif wave_right_url in style or wave_left_url in style:
                        not_occupied_wave_count += 1
                        not_occupied_total_count += 1
                    elif wave_left_sold_url in style or wave_right_sold_url in style:
                        occupied_wave_count += 1
                        occupied_total_count += 1

                if (occupied_total_count + not_occupied_total_count) <= 30:
                    is_premium = True

                if (occupied_total_count + not_occupied_total_count) !=0:
                    occupancy_rate = round(occupied_total_count/(occupied_total_count + not_occupied_total_count),2)
                else:
                    occupancy_rate = 1

                total_count = occupied_total_count + not_occupied_total_count

                with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        movie["location"], movie["movie_name"], movie["timing"], is_premium, movie["href"],
                        movie["genre"], movie["language"], movie["rating"], movie["runtime"], movie["opening"],
                        occupied_regular_count, not_occupied_regular_count,
                        occupied_couple_count, not_occupied_couple_count,
                        occupied_wheelchair_count, not_occupied_wheelchair_count,
                        occupied_wave_count, not_occupied_wave_count,
                        occupied_total_count, not_occupied_total_count, total_count, occupancy_rate
                    ])

                print(f"Data for {movie['movie_name']} saved to {csv_file}.")
                driver.quit()

            except WebDriverException as e:
                print(f"An error occurred with WebDriver: {e}")
                continue  

        #check every 30 seconds
        time.sleep(30)

get_details()