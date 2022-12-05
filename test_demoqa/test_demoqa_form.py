from selene.support.shared import browser
from selene import have


def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Dmitry')
    browser.element('#lastName').type('Yanyshev')
    browser.element('#userEmail').type('mail@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('1234567891')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="3"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1995"]').click()
    browser.element('.react-datepicker__day--006').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#hobbiesWrapper').element('#hobbies-checkbox-1').double_click()




