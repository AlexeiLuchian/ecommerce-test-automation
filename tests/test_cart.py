import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup
from pages.base_page import BasePage

class TestProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSetup.get_driver()
        self.driver.get("https://www.drmax.ro/checkout/1")
        self.page = BasePage(self.driver)
        yield
        self.driver.quit()

    def test_footer_contacts(self):
        footer_contacts_locator = (By.CLASS_NAME, 'footer-contacts')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        footer_contacts = self.page.find_visible_element(footer_contacts_locator)

        assert footer_contacts is not None
        print(f"✓ Footer contacts appear! Test passed")

    def test_continue_shopping(self):
        continue_shopping_locator = (By.CSS_SELECTOR, 'a.btn-link')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        continue_shopping_btn = self.page.find_visible_element(continue_shopping_locator)

        assert continue_shopping_btn is not None
        assert len(continue_shopping_btn.text) > 0
        print(f"✓ Continue Shopping Button appears! Button text: {continue_shopping_btn.text.strip()}")

    def test_checkout_instructions(self):
        checkout_instructions_locator = (By.CSS_SELECTOR, 'div ul.desktop-stepper')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        checkout_instructions = self.page.find_element(checkout_instructions_locator)
        checkout_instructions_count = checkout_instructions.find_elements('tag name', 'li')

        assert checkout_instructions is not None
        assert len(checkout_instructions_count) > 0
        print(f"✓ Checkout instructions appear! Number of steps: {len(checkout_instructions_count)}")
