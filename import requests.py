import requests
from bs4 import BeautifulSoup

url = "https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&domains%5B%5D=2"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="listContainer")

job_elements = results.find_all("div", class_="mdc-layout-grid__inner")

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

external_span = soup.find("i", class_="material-icons")
external_span.extract

for job_element in job_elements:
    title_element = job_element.find("div", class_="left")
    company_element = job_element.find("alt", class_="card_logo")
    location_element = job_element.find("div", class_="card-info card__subtitle")
    print(title_element.span)
    print(company_element)
    print(location_element)
