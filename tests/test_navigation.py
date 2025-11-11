import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup
from pages.base_page import BasePage

class TestProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSetup.get_driver()
        self.driver.get("https://www.drmax.ro")
        self.page = BasePage(self.driver)
        yield
        self.driver.quit()

    def test_footer_links(self):
        despre_link_locator = (By.CSS_SELECTOR, 'li.fast-links__item')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        self.page.click(despre_link_locator)

        assert "despre" in self.driver.current_url.lower()
        print(f"✓ Footer links tests passed! Current URL: {self.driver.current_url}")
    
    def test_category_menu_appears(self):
        category_menu_locator = (By.ID, 'submenu-1')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        category_menu = self.page.find_element(category_menu_locator)
        category_count = category_menu.find_elements('tag name', 'li')

        assert category_menu is not None
        assert len(category_count) > 0
        print(f"✓ Category menu appears! Number of categories: {len(category_count)}")

    def test_homepage_loads(self):
        banner_locator = (By.CLASS_NAME, "header__middle")
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        banner = self.page.find_element(banner_locator)

        assert banner is not None
        print("✓ Homepage loads test passed!")