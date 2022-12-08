from selene.support.shared import browser
from selene import have
from pathlib import Path


def test_form():

    # open url
    browser.open('/automation-practice-form')

    # User Data
    browser.element('#firstName').type('Dmitry')
    browser.element('#lastName').type('Yanyshev')
    browser.element('#userEmail').type('mail@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('1234567891')

    # User Birth Day
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="3"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1995"]').click()
    browser.element('.react-datepicker__day--006').click()

    # User Subjects
    browser.element('#subjectsInput').type('Maths').press_enter()

    # User Hobbies
    browser.element('#hobbiesWrapper').element(
        '#hobbies-checkbox-1').double_click()

    # Upload file
    browser.element('#uploadPicture').set_value(
        Path.cwd().parent / 'upload' / 'logo.png')

    # User address
    browser.element('#currentAddress').type("Победы")
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()

    # Finally
    browser.element('#submit').press_enter()

    # Check finally form
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form'))

    # Check results
    browser.element('.table').should(have.text(
        'Dmitry Yanyshev' and
        'mail@mail.ru' and
        'Male' and
        '1234567891' and
        '06 April,1995' and
        'Maths' and
        'Sports' and
        'logo.png' and
        'Победы' and
        'NCR Gurgaon'
    ))
