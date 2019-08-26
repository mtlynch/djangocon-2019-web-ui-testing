"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:

  # Locators

  SEARCH_INPUT = (By.NAME, 'q')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods
  
  def load(self):
    # TODO
    pass

  def search(self, phrase):
    # TODO
    pass
