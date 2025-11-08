import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup
from pages.base_page import BasePage

class TestSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSetup.get_driver()
        self.driver.get("https://www.drmax.ro/")
        self.page = BasePage(self.driver)
        yield
        self.driver.quit()
    
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
