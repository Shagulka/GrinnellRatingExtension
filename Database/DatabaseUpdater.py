import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Professor:
    def __init__(self, name, rating, num_ratings, would_take_again, difficulty, link, RMP_name):
        self.name = name
        self.rating = rating
        self.num_ratings = num_ratings
        self.would_take_again = would_take_again
        self.difficulty = difficulty
        self.link = link
        self.RMP_name = RMP_name

    def __str__(self):
        return f"Name: {self.name}\nRating: {self.rating}\nNumber of ratings: {self.num_ratings}\nWould take again: {self.would_take_again}\nDifficulty: {self.difficulty}\nLink: {self.link}"


def get_professor_info(prof_name):
    link = 'https://www.ratemyprofessors.com/search/professors/383?q='
    prof_name = prof_name.replace(" ", "+")
    url = link + prof_name

    # get the page
    page = requests.get(url)

    # check if the page is accessible
    if page.status_code != 200:
        return None
    if 'No professors' in page.text:
        return None
    if '"resultCount":0' in page.text:
        return None

    # find window.__RELAY_STORE__ in the page
    start = page.text.find('window.__RELAY_STORE__')
    end = page.text.find('};', start)
    data = page.text[start:end + 1]

    # find avgRating in the data
    start = data.find('avgRating')
    end = data.find(',', start)
    avg_rating = float(data[start + 11:end])

    # find numRatings in the data
    start = data.find('numRatings')
    end = data.find(',', start)
    num_ratings = float(data[start + 12:end])

    # find wouldTakeAgainPercent in the data
    start = data.find('wouldTakeAgainPercent')
    end = data.find(',', start)
    would_take_again_percent = float(data[start + 23:end])

    # find avgDifficulty in the data
    start = data.find('avgDifficulty')
    end = data.find(',', start)
    avg_difficulty = float(data[start + 15:end])

    # find legacyId in the data
    start = data.find('legacyId')
    end = data.find(',', start)
    legacy_id = data[start + 10:end]
    link = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + legacy_id

    # find names in the data
    start = data.find('lastName')
    end = data.find(',', start)
    last_name = data[start + 11:end]
    start = data.find('firstName')
    end = data.find(',', start)
    first_name = data[start + 12:end]
    RMP_name = first_name + ' ' + last_name

    prof = Professor(prof_name, avg_rating, num_ratings, would_take_again_percent, avg_difficulty, link, RMP_name)
    return prof


def get_all_professors_names():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://colss-prod.ec.grinnell.edu/Student/Courses'
    driver.get(url)

    time.sleep(5)

    search_button = driver.find_element(By.ID, 'submit-search-form')
    search_button.click()

    time.sleep(5)

    professor_names = []
    for i in range(62):
        elements = driver.find_elements(By.XPATH, '//*[@title="Show Office Hours"]')
        office_hours_contents = [element.text for element in elements]
        professor_names = professor_names + office_hours_contents
        next_page_button = driver.find_element(By.ID, 'course-results-next-page')
        next_page_button.click()
        time.sleep(3)

    professor_names = list(set(professor_names))
    return professor_names


def get_all_professors_info(names):
    professors = []
    for name in names:
        prof = get_professor_info(name)
        if prof is not None:
            professors.append(prof)
    return professors


def generate_json(professors):
    json = dict()
    for prof in professors:
        print(prof)
        correct = input('is this correct? (y/n)')
        if correct == 'y':
            json[prof.name] = {
                "rating": prof.rating,
                "num_ratings": prof.num_ratings,
                "would_take_again": prof.would_take_again,
                "difficulty": prof.difficulty,
                "link": prof.link
            }
    return json


def update_database():
    names = get_all_professors_names()
    professors = get_all_professors_info(names)
    json = generate_json(professors)
    print(json)
    json = str(json)
    with open('professors.json', 'w') as file:
        file.write(json)
    return

if __name__ == '__main__':
    update_database()