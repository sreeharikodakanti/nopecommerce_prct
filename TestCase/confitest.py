from selenium import webdriver
import pytest

PATH = "C:\Program Files (x86)\chromedriver.exe"


@pytest.fixture()
def setup(driver):
    if browser == "chrome":
        driver = webdriver.Chrome(PATH)
    return driver

def pytest_addoption(parser):
    return parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



def configure(config):
    config._metadata["projectName"]="nop-Ecommerce"
    config._metadata['module'] = "Customers"
    config._metadata['Tester'] = "Tester"

@pytest.mark.optionalhook
    def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME",None)
        metadata.pop("plugins",None)

