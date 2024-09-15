#Here we are installing Mircrosoft tool Playwright
# it is much faster the selenium and other
# 1. To install: pip3 install playwright
# 2. then need to install pytest playwright: pip3 install pytest-playwright
# 3. Then it has unique approch for testing is using chromium,firefox and all: playwright install

import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.acme_bank

def test_acme_bank_login(page: Page):

    #Arrange
    page.goto('https://demo.applitools.com')

    #Act
    page.locator('id=username').fill('andy')
    page.locator('id=password').fill('i<3pandas')
    page.locator('id=log-in').click()

    #Assert
    #using except the element should be ready before checking them and called Web-first assertions
    #we are doing examples here
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('ul.main-menu')).to_be_visible()
    expect(page.get_by_text('Make payment')).to_be_visible()
    expect(page.get_by_text('View Statement')).to_be_visible()
    expect(page.get_by_text('Request Increase')).to_be_visible()
    expect(page.get_by_text('Pay now')).to_be_visible()

    #need to check applittools tutorial for Testing web apps in python using playwright


