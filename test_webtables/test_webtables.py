import os

from selene import have
from selene.support.shared import browser

firstName = 'Ivan'
lastName = 'Ivanov'
userEmail = 'mail@mail.com'
age = '88'
salary = '88000'
department = 'mba'

def test_webtables_added():
    browser.open('https://demoqa.com/webtables')
    browser.element('#addNewRecordButton').click()

    browser.element('#firstName').type(firstName)
    browser.element('#lastName').type(lastName)
    browser.element('#userEmail').type(userEmail)
    browser.element('#age').type(age)
    browser.element('#salary').type(salary)
    browser.element('#department').type(department)
    browser.element('#submit').press_enter()

    browser.element('.rt-tbody').should(have.text(firstName))
    browser.element('.rt-tbody').should(have.text(lastName))
    browser.element('.rt-tbody').should(have.text(userEmail))
    browser.element('.rt-tbody').should(have.text(age))
    browser.element('.rt-tbody').should(have.text(salary))
    browser.element('.rt-tbody').should(have.text(department))

def test_webtables_changed():
    browser.open('https://demoqa.com/webtables')
    browser.element('#edit-record-2').click()

    browser.element('#firstName').clear().type(firstName)
    browser.element('#lastName').clear().type(lastName)
    browser.element('#userEmail').clear().type(userEmail)
    browser.element('#age').clear().type(age)
    browser.element('#salary').clear().type(salary)
    browser.element('#department').clear().type(department)
    browser.element('#submit').press_enter()

    browser.element('.rt-tbody').should(have.text(firstName))
    browser.element('.rt-tbody').should(have.text(lastName))
    browser.element('.rt-tbody').should(have.text(userEmail))
    browser.element('.rt-tbody').should(have.text(age))
    browser.element('.rt-tbody').should(have.text(salary))
    browser.element('.rt-tbody').should(have.text(department))

def test_webtables_deleted():
    browser.open('https://demoqa.com/webtables')
    browser.element('#delete-record-3').click()

    browser.element('.rt-tbody').should(have.no.text('Kierra'))
    browser.element('.rt-tbody').should(have.no.text('Gentry'))
    browser.element('.rt-tbody').should(have.no.text('kierra@example.com'))
    browser.element('.rt-tbody').should(have.no.value('29'))
    browser.element('.rt-tbody').should(have.no.value('2000'))
    browser.element('.rt-tbody').should(have.no.text('Legal'))
