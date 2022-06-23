from conftest import *


def test_true(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_false(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
