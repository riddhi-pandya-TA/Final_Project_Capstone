from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()

# Step Definitions

@given('the user navigates to the Salesforce lead creation page')
def step_impl(context):
    context.driver.get("https://speed-efficiency-7600.lightning.force.com/lightning/o/Lead/new?count=1&nooverride=1&useRecordTypeCheck=1&navigationLocation=LIST_VIEW&uid=173858982780414974&backgroundContext=%2Flightning%2Fo%2FLead%2Flist%3FfilterName%3DAllOpenLead")
    context.driver.implicitly_wait(10)

@when('the user enters the salutation, first name, last name, and company')
def step_impl(context):
    # Click on 'New' button
    new_button = context.driver.find_element(By.XPATH, "//div[text()='New']")
    new_button.click()

    # Enter Salutation
    salutation = context.driver.find_element(By.XPATH, "//div[text()='Mr']")
    salutation.click()

    # Enter First Name
    first_name = context.driver.find_element(By.XPATH, "//input[@name='firstName']")
    first_name.send_keys("John")

    # Enter Last Name
    last_name = context.driver.find_element(By.XPATH, "//input[@name='lastName']")
    last_name.send_keys("Doe")

    # Enter Company
    company = context.driver.find_element(By.XPATH, "//input[@name='Company']")
    company.send_keys("TechCorp")

@then('the user should be able to save the new lead successfully')
def step_impl(context):
    # Click on the Save button
    save_button = context.driver.find_element(By.XPATH, "//button[text()='Save']")
    save_button.click()

    # Add validation here (optional)
    # For example, check if the lead is saved by verifying the title or a confirmation message
    success_message = context.driver.find_element(By.XPATH, "//span[text()='Lead created successfully']")
    assert success_message.is_displayed()
