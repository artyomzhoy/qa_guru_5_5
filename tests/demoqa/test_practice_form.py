import os
import allure

from selene import browser, have
from allure_commons.types import Severity

from utils import attach


# from selenium.webdriver import Keys


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'artyomzhoy')
@allure.feature('Форма регистрации')
@allure.story('Сохранение данных регистрационной формы')
@allure.link('https://demoqa.com/automation-practice-form', name='Registration form.')
def test_decorator_allure_steps_practice_form():
    open_practice_form('automation-practice-form')
    type_first_name('Orbit')
    type_second_name('Culture')
    type_email('orbitculture@gmail.com')
    type_user_number('79999999999')
    type_subject('Computer Science')
    type_address('Heaven shall burn 666')
    select_state('NCR')
    select_city_from_state('Delhi')
    select_date_of_birth()
    # upload_picture()
    select_gender()
    select_hobbies()
    submit_all()
    check_data()
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)


@allure.step('Открытие формы')
def open_practice_form(page):
    browser.open(page)
    browser.driver.execute_script("$('footer').remove()")
    browser.driver.execute_script("$('#fixedban').remove()")


@allure.step('Ввод имени')
def type_first_name(first_name):
    browser.element('#firstName').type(first_name)


@allure.step('Ввод фамилии')
def type_second_name(second_name):
    browser.element('#lastName').type(second_name)


@allure.step('Ввод email')
def type_email(email):
    browser.element('#userEmail').type(email)


@allure.step('Ввод телефона')
def type_user_number(number):
    browser.element('#userNumber').type(number)


@allure.step('Ввод существующего предмета')
def type_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


@allure.step('Ввод адреса')
def type_address(address):
    browser.element('#currentAddress').type(address)


# Ввод значений в поля выбора штата/города
# browser.element('#react-select-3-input').type('NCR').press_enter()
# browser.element('#react-select-4-input').type('Delhi').press_enter()


# Выбор штата/города
@allure.step('Выбор штата из списка')
def select_state(state):
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').should(have.exact_text(state)).click()


@allure.step('Выбор города из списка')
def select_city_from_state(city):
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.exact_text(city)).click()


# Ввод значений в поле даты
# browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('06 June 1999').press_enter()


# Выбор даты
@allure.step('Выбор даты рождения')
def select_date_of_birth():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1999"]').click()
    browser.element('.react-datepicker__day--006').click()


@allure.step('Загрузка картинки')
def upload_picture():
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/tests/test.png')


@allure.step('Выбор пола')
def select_gender():
    browser.element('[for=gender-radio-3]').click()


@allure.step('Выбор хобби')
def select_hobbies():
    browser.element('[for=hobbies-checkbox-3]').click()


@allure.step('Сохранение данных')
def submit_all():
    browser.element('#submit').press_enter()


@allure.step('Проверка сохранённых данных')
def check_data():
    browser.all('tbody tr').should(have.texts
                                   ('Student Name Orbit Culture',
                                    'Student Email orbitculture@gmail.com',
                                    'Gender Other',
                                    'Mobile 7999999999',
                                    'Date of Birth 06 June,1999',
                                    'Subjects Computer Science',
                                    'Hobbies Music',
                                    'Picture',
                                    'Address Heaven shall burn 666',
                                    'State and City NCR Delhi'))

