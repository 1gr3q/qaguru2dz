import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope='session', autouse='True')
def browser_size():
    browser.config.window_height = 800
    browser.config.window_width = 600