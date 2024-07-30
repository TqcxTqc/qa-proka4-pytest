from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestNewsFeed:

    USERNAME_FIELD_LOCATOR = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")
    HEADER_TEXT_LOCATOR = ("xpath", "//h6[text()='Dashboard']")
    RIGHT_SIDE_MENU_BUZZ_LOCATOR = ("xpath", "//span[text()='Buzz']")
    TEXT_AREA_LOCATOR = ("xpath", "//textarea[@placeholder=\"What\'s on your mind?\"]")
    SUBMIT_POST_BUTTON_LOCATOR = ("xpath", "//div[@class='oxd-buzz-post-slot']")

    USERNAME = "Admin"
    PASSWORD = "admin123"
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @property
    def wait(self):
        return WebDriverWait(driver=self.driver, timeout=15, poll_frequency=2)

    def verify_joke(self, joke):
        posted_jokes = self.wait.until(EC.visibility_of_all_elements_located(("xpath", "//p[contains(@class,'post-body-text')]")))
        joke_found = False

        for post in posted_jokes:
            if joke.strip() == post.text.strip():
                joke_found = True
                break

        assert joke_found, "Joke was not posted successfully"

    def setup_method(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD_LOCATOR)).send_keys(self.USERNAME)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD_LOCATOR)).send_keys(self.PASSWORD)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON_LOCATOR)).click()
        assert self.wait.until(EC.visibility_of_element_located(self.HEADER_TEXT_LOCATOR)).is_displayed(), "User is not logged in"

    def test_login(self, get_joke):
        joke = get_joke
        self.driver.find_element(*self.RIGHT_SIDE_MENU_BUZZ_LOCATOR).click()
        self.wait.until(EC.presence_of_element_located(self.TEXT_AREA_LOCATOR))
        textarea = self.driver.find_element(*self.TEXT_AREA_LOCATOR)
        textarea.send_keys(joke)
        self.driver.find_element(*self.SUBMIT_POST_BUTTON_LOCATOR).click()
        self.verify_joke(joke)
