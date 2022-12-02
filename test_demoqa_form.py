import pytest
from selene.support.shared import browser
from selene import be, have


def test_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
    browser.element('#firstName').type('Dmitry')
    browser.element('#lastName').type('Yanyshev')
    browser.element('#userEmail').type('mail@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('1234567891')
