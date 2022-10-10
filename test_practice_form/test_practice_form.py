import os

from selene import be, have
from selene.support.shared import browser


def test_submit_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('mail@mail.com')
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2000"]').click()
    browser.element('.react-datepicker__day--028').click()

    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../picture.png'))
    browser.element('#currentAddress').type('Red square, 1\n'
                                            'Africa\n')
    browser.element('#react-select-3-input').type('Har').press_enter()
    browser.element('#react-select-4-input').type('Pan').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').all('tbody tr').should(have.texts(
        'Ivan Ivanov',
        'mail@mail.com',
        'Female',
        '1234567890',
        '28 May,2000',
        'Maths',
        'Sports, Music',
        'picture.png',
        'Red square, 1 Africa',
        'Haryana Panipat'
    ))
    browser.element('#closeLargeModal').press_enter()