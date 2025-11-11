import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup
from pages.base_page import BasePage
from urllib.parse import quote

class TestSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSetup.get_driver()
        self.driver.get("https://www.drmax.ro/")
        self.page = BasePage(self.driver)
        yield
        self.driver.quit()

    def test_search_result_count(self):
        search_query = "pastile"
        result_count_locator = (By.CSS_SELECTOR, "div.mb-3 span.flex-shrink-0")
        search_box_locator = (By.ID, "header-search-input")
        search_button_locator = (By.ID, "header-search__button-submit")
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        self.page.type_text(search_box_locator, search_query)
        self.page.click(search_button_locator)
        self.page.find_element(result_count_locator)
        result_count = self.page.find_element(result_count_locator).text.strip('()').split()[0]

        assert result_count.isnumeric()
        print(f"✓ Result count: {result_count}")

    def test_search_suggestions(self):
        '''
        Tests if suggestions appear after typing something into the search box.
        The length of the search query should be 2 characters long or more.
        '''
        search_query = "pa"
        search_box_locator = (By.ID, "header-search-input")
        suggestions_locator = (By.CSS_SELECTOR, "div.aa-suggestion")
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        self.page.type_text(search_box_locator, search_query)

        assert self.page.find_element(suggestions_locator)
        print("✓ Search suggestions test passed!")


    def test_search_functionality(self):
        search_query = "sampon"
        search_box_locator = (By.ID, "header-search-input")
        search_button_locator = (By.ID, "header-search__button-submit")
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        self.page.type_text(search_box_locator, search_query)
        self.page.click(search_button_locator)

        self.page.wait_for_url_contains(search_query)
        assert search_query.lower() in self.driver.current_url.lower()
        print("✓ Search test passed!")

    def test_empty_box_shows_placeholder(self):
        search_box_locator = (By.ID, "header-search-input")
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        search_box = self.page.find_element(search_box_locator)
        placeholder = search_box.get_attribute("placeholder")

        assert placeholder is not None  
        assert len(placeholder) > 0
        print(f"✓ Placeholder text: '{placeholder}'")

    def test_special_characters_search(self):
        search_query = "șampon"
        search_box_locator = (By.ID, "header-search-input")
        search_button_locator = (By.ID, "header-search__button-submit")
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")

        self.page.click(accept_cookies)
        self.page.type_text(search_box_locator, search_query)
        self.page.click(search_button_locator)

        search_query_url = quote(search_query)
        self.page.wait_for_url_contains(search_query_url)
        assert search_query_url.lower() in self.driver.current_url.lower()
        print("✓ Special characters search test passed!")