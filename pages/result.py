from selenium.webdriver.common.by import By


class GoogleResultPage:
    LINK_DIVS = (By.TAG_NAME, 'a')
    SEARCH_INPUT = (By.NAME, 'q')

    @classmethod
    def WORD_RESULTS(cls, word):
        xpath = f"//div[contains(text(),{word})]"
        return [(By.XPATH, xpath)]

    def __init__(self, browser):
        self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def word_result_count(self, word):
        word_results = self.browser.find_elements(*self.WORD_RESULTS(word))
        return len(word_results)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
