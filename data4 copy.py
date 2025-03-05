from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from getallmovies import getallmovies
from getallmovietimings import obtain_all_moviedates

# movie_timings = obtain_all_moviedates()
movie_timings = [{'location': 'Causeway Point', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T14:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154475'}, {'location': 'JEM', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T14:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201569'}, {'location': 'Causeway Point', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T14:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/153995'}, {'location': 'Century Square', 'movie_name': 'Number-2-NC16', 'timing': '2025-03-05T14:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13105'}, {'location': 'Clementi 321', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T14:50:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5805'}, {'location': 'Causeway Point', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T15:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154089'}, {'location': 'Causeway Point', 'movie_name': 'Number-2-NC16', 'timing': '2025-03-05T15:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/153991'}, {'location': 'Clementi 321', 'movie_name': 'I-Want-To-Be-Boss-PG13', 'timing': '2025-03-05T15:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5788'}, {'location': 'JEM', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T15:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201557'}, {'location': 'Clementi 321', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T15:20:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5792'}, {'location': 'Century Square', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T15:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13097'}, {'location': 'Causeway Point', 'movie_name': 'Officer-On-Duty-Malayalam-M18', 'timing': '2025-03-05T15:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154489'}, {'location': 'Century Square', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T15:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13112'}, {'location': 'Downtown East', 'movie_name': 'Officer-On-Duty-Malayalam-M18', 'timing': '2025-03-05T15:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117934'}, {'location': 'JEM', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T15:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201577'}, {'location': 'Clementi 321', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T16:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5801'}, {'location': 'Century Square', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T16:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13109'}, {'location': 'JEM', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T16:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201513'}, {'location': 'Clementi 321', 'movie_name': 'Detective-Chinatown-1900-NC16', 'timing': '2025-03-05T16:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5776'}, {'location': 'Causeway Point', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T16:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154470'}, {'location': 'Clementi 321', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T16:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5782'}, {'location': 'Downtown East', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T16:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117889'}, {'location': 'Causeway Point', 'movie_name': 'Detective-Chinatown-1900-NC16', 'timing': '2025-03-05T16:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154494'}, {'location': 'Downtown East', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T16:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117882'}, {'location': 'Clementi 321', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T16:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5785'}, {'location': 'JEM', 'movie_name': 'Detective-Chinatown-1900-NC16', 'timing': '2025-03-05T16:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201565'}, {'location': 'Clementi 321', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T16:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5773'}, {'location': 'Downtown East', 'movie_name': 'Detective-Chinatown-1900-NC16', 'timing': '2025-03-05T16:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117947'}, {'location': 'Downtown East', 'movie_name': 'Number-2-NC16', 'timing': '2025-03-05T16:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117876'}, {'location': 'Downtown East', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T17:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117879'}, {'location': 'Century Square', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T17:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13302'}, {'location': 'JEM', 'movie_name': 'Officer-On-Duty-Malayalam-M18', 'timing': '2025-03-05T17:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201574'}, {'location': 'JEM', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T17:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201562'}, {'location': 'Clementi 321', 'movie_name': 'Dark-Nuns-NC16', 'timing': '2025-03-05T17:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5779'}, {'location': 'Century Square', 'movie_name': 'Creation-of-the-Gods-II-Demon-Force-PG13', 'timing': '2025-03-05T17:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13106'}, {'location': 'Causeway Point', 'movie_name': 'Creation-of-the-Gods-II-Demon-Force-PG13', 'timing': '2025-03-05T17:10:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/153992'}, {'location': 'JEM', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T17:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201515'}, {'location': 'Century Square', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T17:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13094'}, {'location': 'JEM', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T17:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201550'}, {'location': 'Clementi 321', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T17:20:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5793'}, {'location': 'JEM', 'movie_name': 'Dark-Nuns-NC16', 'timing': '2025-03-05T17:20:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201554'}, {'location': 'Century Square', 'movie_name': '1-Imam-2-Makmum-PG', 'timing': '2025-03-05T17:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13098'}, {'location': 'Causeway Point', 'movie_name': 'Aghathiyaa-Tamil-PG13', 'timing': '2025-03-05T17:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154476'}, {'location': 'Clementi 321', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T17:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5806'}, {'location': 'Clementi 321', 'movie_name': 'Nilavuku-En-Mel-Ennadi-Kobam-Tamil-PG13', 'timing': '2025-03-05T17:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5798'}, {'location': 'JEM', 'movie_name': 'Nocturnal-NC16', 'timing': '2025-03-05T17:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201558'}, {'location': 'Clementi 321', 'movie_name': 'Anak-Kunti-NC16', 'timing': '2025-03-05T17:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5789'}, {'location': 'Causeway Point', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T18:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/153996'}, {'location': 'Causeway Point', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T18:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154087'}, {'location': 'Causeway Point', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T18:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154490'}, {'location': 'Clementi 321', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T18:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5802'}, {'location': 'Downtown East', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T18:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117887'}, {'location': 'JEM', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T18:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201571'}, {'location': 'Century Square', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T19:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13113'}, {'location': 'JEM', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T19:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201578'}, {'location': 'Century Square', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T19:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13110'}, {'location': 'JEM', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T19:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201514'}, {'location': 'Clementi 321', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T19:20:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5794'}, {'location': 'Causeway Point', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T19:20:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154495'}, {'location': 'Downtown East', 'movie_name': 'Officer-On-Duty-Malayalam-M18', 'timing': '2025-03-05T19:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117949'}, {'location': 'Clementi 321', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T19:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5783'}, {'location': 'Clementi 321', 'movie_name': 'Detective-Chinatown-1900-NC16', 'timing': '2025-03-05T19:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5777'}, {'location': 'Causeway Point', 'movie_name': 'Officer-On-Duty-Malayalam-M18', 'timing': '2025-03-05T19:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154471'}, {'location': 'Clementi 321', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T19:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5774'}, {'location': 'Century Square', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T19:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13103'}, {'location': 'Clementi 321', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T19:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5786'}, {'location': 'Downtown East', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T19:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117890'}, {'location': 'JEM', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T19:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201962'}, {'location': 'Downtown East', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T20:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117883'}, {'location': 'JEM', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T20:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201575'}, {'location': 'Downtown East', 'movie_name': 'Sabdham-Tamil-PG13', 'timing': '2025-03-05T20:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117960'}, {'location': 'Century Square', 'movie_name': 'Aghathiyaa-Tamil-PG13', 'timing': '2025-03-05T20:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13099'}, {'location': 'Clementi 321', 'movie_name': 'Aghathiyaa-Tamil-PG13', 'timing': '2025-03-05T20:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5790'}, {'location': 'Clementi 321', 'movie_name': 'Creation-of-the-Gods-II-Demon-Force-PG13', 'timing': '2025-03-05T20:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5780'}, {'location': 'JEM', 'movie_name': 'Creation-of-the-Gods-II-Demon-Force-PG13', 'timing': '2025-03-05T20:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201960'}, {'location': 'JEM', 'movie_name': 'Officer-On-Duty-Malayalam-M18', 'timing': '2025-03-05T20:10:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201563'}, {'location': 'Century Square', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T20:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13107'}, {'location': 'JEM', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T20:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201559'}, {'location': 'Causeway Point', 'movie_name': 'Dragon-Tamil-PG13', 'timing': '2025-03-05T20:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/153993'}, {'location': 'JEM', 'movie_name': 'Legends-of-the-Condor-Heroes-The-Gallants-PG13', 'timing': '2025-03-05T20:15:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201516'}, {'location': 'Downtown East', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T20:20:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117880'}, {'location': 'Causeway Point', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T20:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154477'}, {'location': 'Clementi 321', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T20:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5807'}, {'location': 'JEM', 'movie_name': 'Nosferatu-M18', 'timing': '2025-03-05T20:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201551'}, {'location': 'Century Square', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T20:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1113/13095'}, {'location': 'Clementi 321', 'movie_name': '1-Imam-2-Makmum-PG', 'timing': '2025-03-05T20:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5833'}, {'location': 'Causeway Point', 'movie_name': 'Officer-On-Duty-Malayalam-M18', 'timing': '2025-03-05T20:30:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154491'}, {'location': 'JEM', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T20:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1110/201572'}, {'location': 'Downtown East', 'movie_name': '1-Imam-2-Makmum-PG', 'timing': '2025-03-05T20:40:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1106/117886'}, {'location': 'Causeway Point', 'movie_name': '1-Imam-2-Makmum-PG', 'timing': '2025-03-05T20:45:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/154107'}, {'location': 'Clementi 321', 'movie_name': 'Close-Ur-Kopitiam-PG13', 'timing': '2025-03-05T21:00:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5803'}, {'location': 'Causeway Point', 'movie_name': 'Nocturnal-NC16', 'timing': '2025-03-05T21:10:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1102/153997'}, {'location': 'Clementi 321', 'movie_name': 'Mobile-Suit-Gundam-GQuuuuuuX--Beginning-PG13', 'timing': '2025-03-05T21:20:00', 'href': 'https://www.cathaycineplexes.com.sg/ticketing/1114/5795'}]

def get_details():


    for movie_timing in movie_timings:

        cService = webdriver.ChromeService(executable_path=r'C:\Users\jai\Desktop\DBTT\DBTT\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=cService)

        driver.get(movie_timing['href'])

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

get_details()