import os

from selene import browser, have
# from selenium.webdriver import Keys


def test_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Hello')
    browser.element('#lastName').type('World')
    browser.element('#userEmail').type('helloworld@gmail.com')
    browser.element('#userNumber').type('79999999999')
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('#currentAddress').type('Heaven shall burn 666')

    # Ввод значений в поля выбора штата/города
    # browser.element('#react-select-3-input').type('NCR').press_enter()
    # browser.element('#react-select-4-input').type('Delhi').press_enter()

    # Выбор штата/города
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').should(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.exact_text('Delhi')).click()

    # Ввод значений в поле даты
    # browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('06 June 1999').press_enter()

    # Выбор даты
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1999"]').click()
    browser.element('.react-datepicker__day--006').click()

    browser.element('#uploadPicture').send_keys(os.getcwd() + '/test.png')

    browser.element('[for=gender-radio-3]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#submit').press_enter()

    browser.all('tbody tr').should(have.texts
                                   ('Hello World',
                                    'helloworld@gmail.com',
                                    'Other',
                                    '7999999999',
                                    '06 June,1999',
                                    'Computer Science',
                                    'Music',
                                    'test.png',
                                    'Heaven shall burn 666',
                                    'NCR Delhi'))
