import requests
from bs4 import BeautifulSoup
import os

def main_menu():
    os.system('cls')
    print('Изберете сайт: ')
    print()
    print('1. jobs.bg')
    print('2. it.jobs.bg')
    print()
    print()
    menu_choice = input("Избери: ")
    if menu_choice == "1":
        os.system('cls')
        menu_jobsbg()
        menu_choice = input("Избери: ")
    elif(menu_choice == "2"):
        os.system('cls')
        menu_it_jobsbg()
        menu_choice = input("Избери: ")
  
def menu_jobsbg():
    os.system('cls')
    
    print('Изберете категория:')
    print()
    print('0. Главно меню')
    print('1. Всички')
    print('2. Търговия и Продажби')
    print('3. Производство')
    print('4. Ресторанти, Заведения, Хотели, Туризъм')
    print('5. Административни, Офис и Бизнес дейности')
    print('6. Шофьри, Куриери')
    print('7. Инженери и Техници')
    print('8. Архитектура, Строителство')
    print('9. Физически/Ръчен труд')
    print('10. Логистика, Спедиция')
    print('11. Ремонти и Монтажни дейности')
    print('12. Здравеопазване и Фармация')
    print('13. Счетоводство, Одит, Финанси')
    print('14. Автомобили, Автосервизи, Бензиностанции')
    print('15. Банки, Кредитиране, Застраховане')
    print('16. Центрове за обслужване на клиенти и бизнес услуги')
    print('17. Забавление, Промоции, Спорт, Салони за красота')
    print('18. Почистване, Градинарство, Услуги за домакинство')
    print('19. Маркетинг, Реклама, ПР')
    print('20. Сигурност и Охрана')
    print('21. Енергетика, ВиК, Комунални услуги')
    print('22. Телекоми')
    print('23. Образование, Курсове, Преводи')
    print('24. Мениджмънт')
    print('25. Дизайн, Криейтив, Изкуство')
    print('26. Човешки ресурси(HR)')
    print('27. Селско и горско стопанство, Рибовъдство')
    print('28. Изследователска и Развойна дейност(R&D)')
    print('29. Недвижими имоти')
    print('30. Държавна администрация, Институции')
    print('31. Право, Юридически услуги')
    print('32. Медии, Издателсто')
    print('33. Морски и Речен транспорт')
    print('34. Организации с нестопанска цел')
    print('35. Авиация, Летища и Авиолинии')
    
    menu_choice = input("Избери: ")
    if menu_choice == "0":
        main_menu()
        menu_choice = input("Избери: ")
        print(menu_choice)
    elif menu_choice == "1":
        url = "https://www.jobs.bg/front_job_search.php?subm=1"
        main_code()
        
        
    
def menu_it_jobsbg():
    os.system('cls')
    
    print('Изберете категория:')
    print()
    print('0. Главно меню')
    print('1. Всички')
    print('2. Front End')
    print('3. Back End')
    print('4. Full Stack')
    print('5. Mobile')
    print('6. Web')
    print('7. Desktop, Enterprise')
    print('8. Gaming')
    print('9. Cloud')
    print('10. Embedded')
    print('11. Test, QA')
    print('12. System Administration')
    print('13. Network Administration')
    print('14. DevOps')
    print('15. Security')
    print('16. DBA, Big Data')
    print('17. Data Science, AI, ML')
    print('18. BI, ERP, CRM')
    print('19. PM, PO, BA')
    print('20. UI, UX, Creative')
    print('21. Hardware and Technicians')
    print('22. Technical Support')
    print('23. Customer Support')
    print('24. Sales, Biz Dev')
    print('25. Marketing, SEO')
    print('26. IT Recruitment / HR')
    print('27. IT Architecture')
    print('28. Team Lead')
    print('29. IT Senior Management')
    
    menu_choice = input("Избери: ")
    if menu_choice == "0":
            
        main_menu()
        menu_choice = input("Избери: ")
        print(menu_choice)
    



def main_code():
    
    url = "https://www.jobs.bg/front_job_search.php?subm=1"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="listContainer")

    job_elements = results.find_all("div", class_="mdc-layout-grid__inner")

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    for job_element in job_elements:
        title_element = job_element.find("div", class_="left")
        company_element = job_element.find("div", class_="secondary-text")
        location_element = job_element.find("div", class_="card-info card__subtitle")
        print()
        print("Позиция: ", )
        print("Компания: ", company_element.text)
        print("Детаили: ", location_element.text.strip())
        
main_menu()