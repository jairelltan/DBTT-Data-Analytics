from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime


cService = webdriver.ChromeService(executable_path=r'C:\Users\jai\Desktop\DBTT\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get('https://www.cathaycineplexes.com.sg/ticketing/1114/5797')

# Find all seat elements
seats = driver.find_elements(By.CLASS_NAME, 'cell')

# Initialize counters
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

# URLs for different seat types
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


# Loop through each seat and check the background image URL and status
for seat in seats:
    style = seat.get_attribute('style')  # Get the inline style that includes the background image URL
    status = seat.get_attribute('status')  # Get the status attribute
    
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



# Output the results
print(f'Occupied regular seats: {occupied_regular_count}')
print(f'Not occupied regular seats: {not_occupied_regular_count}')
print(f'Occupied couple seats: {occupied_couple_count}')
print(f'Not occupied couple seats: {not_occupied_couple_count}')
print(f'Occupied wheelchair seats: {occupied_wheelchair_count}')
print(f'Not occupied wheelchair seats: {not_occupied_wheelchair_count}')
print(f'Occupied wave seats: {occupied_wave_count}')
print(f'Not occupied wave seats: {not_occupied_wave_count}')




# Output the overall count for all seats (regular, couple, and wheelchair)
print(f'Total occupied seats: {occupied_total_count}')
print(f'Total not occupied seats: {not_occupied_total_count}')

# Close the browser window
driver.quit()
