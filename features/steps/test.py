from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *
import os

print(os.getcwd())
driver = webdriver.Chrome('features/chromedriver') 

@given('we have behave installed')
def step_impl(context):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False