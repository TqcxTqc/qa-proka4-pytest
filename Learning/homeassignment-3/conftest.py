import pytest
import requests
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture()
def get_joke():
    response = requests.get("https://geek-jokes.sameerkumar.website/api")
    assert response.status_code == 200, "Failed to fetch joke"
    return response.text
