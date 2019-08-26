"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
  
  # Locators

  SEARCH_INPUT = (By.ID, 'search_form_input')

  @staticmethod
  def PHRASE_RESULTS(phrase):
    xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
    return (By.XPATH, xpath)
  
  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods
  
  def result_count_for_phrase(self, phrase):
    # TODO
    return 0
  
  def search_input_value(self):
    # TODO
    return ""

  def title(self):
    # TODO
    return ""
