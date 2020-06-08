import pytest

from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome()

    # Wait implicitly for elements interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_basic_search(browser):
    # Set up test case data
    word = 'dolphin'

    # Search for the word
    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search(word)

    # Verify that results appear
    result_page = GoogleResultPage(browser)
    assert result_page.search_input_value() == word

    # Verify that total link results appear
    result_page = GoogleResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.word_result_count() > 0




