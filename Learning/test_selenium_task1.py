from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLoginPage:
    LOGIN_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")
    USERNAME_FIELD_LOCATOR = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@name='password']")
    DASHBOARD_TITLE_LOCATOR = ("xpath", "//h6[contains(normalize-space(),'Dashboard')]")

    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(driver=self.driver, timeout=15, poll_frequency=2)

    def test_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON_LOCATOR))
        self.driver.find_element(*self.USERNAME_FIELD_LOCATOR).send_keys("Admin")
        self.driver.find_element(*self.PASSWORD_FIELD_LOCATOR).send_keys("admin123")
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()
        self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_TITLE_LOCATOR))
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def teardown_method(self):
        self.driver.quit()
