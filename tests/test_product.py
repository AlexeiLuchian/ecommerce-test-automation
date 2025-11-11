import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup
from pages.base_page import BasePage

class TestProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSetup.get_driver()
        self.driver.get("https://www.drmax.ro/sampon-anti-matreata-severa-kelual-ds-100ml-ducray")
        self.page = BasePage(self.driver)
        yield
        self.driver.quit()

    def test_add_to_cart_button(self):
        add_to_cart_btn_locator = (By.CSS_SELECTOR, 'div.add-to-basket button')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        add_to_cart_btn = self.page.find_element(add_to_cart_btn_locator)

        assert add_to_cart_btn is not None
        print(f"✓ 'Add to cart' button exists!")

    def test_product_price_is_visible(self):
        price_locator = (By.CLASS_NAME, 'price-text')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        price = self.page.find_visible_element(price_locator).text.split()[0]

        assert price is not None
        print(f"✓ Product price is visible! Product price: {price}")

    def test_product_image_display(self):
        images_locator = (By.CLASS_NAME, 'lazy-image')
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        images = self.page.find_elements(images_locator)

        assert len(images) > 0
        for image in images:
            assert image.is_displayed()
        print(f"✓ Product images display! Number of images displayed: {len(images)}")

    def test_product_page_loads(self):
        title_locator = (By.CSS_SELECTOR, "h1.pr-detail__title")
        accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        
        self.page.click(accept_cookies)
        title_first_word = self.page.find_element(title_locator).text.split()[0]

        assert title_first_word.lower() in self.driver.current_url.lower()
        print("✓ Product page load test passed!")