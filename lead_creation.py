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

@then('user logs in to the portal')
def login(self):
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("testuser")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

@when('user creates a new lead')
def new_lead(firstname, lastname, company):
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Lead']/one-app-nav-bar-item-dropdown"))
    )

    lead = driver.find_element(By.XPATH,
                               "//one-app-nav-bar-item-root[@data-id='Lead']/one-app-nav-bar-item-dropdown")
    actions.move_to_element(lead).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='New Lead']")))

    new_lead = driver.find_element(By.XPATH, "//span[text()='New Lead']")
    actions.move_to_element(new_lead).click().perform()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='isModal inlinePanel oneRecordActionWrapper']"))
    )
    driver.find_element(By.XPATH, "//span[text()='--None--']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//lightning-base-combobox-item/span/span[text()='Mr.']"))
    )

    driver.find_element(By.XPATH, "//lightning-base-combobox-item/span/span[text()='Mr.']").click()
    driver.find_element(By.XPATH, "//div/input[@placeholder='First Name']").send_keys(firstname)
    driver.find_element(By.XPATH, "//div/input[@placeholder='Last Name']").send_keys(lastname)
    driver.find_element(By.XPATH, "//input[@name='Company']").send_keys(company)
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    fullname = firstname + ' ' + lastname

    driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Lead']/one-app-nav-bar-item-dropdown"))
    )

    lead = driver.find_element(By.XPATH,
                               "//one-app-nav-bar-item-root[@data-id='Lead']/one-app-nav-bar-item-dropdown")
    actions.move_to_element(lead).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[text()='{fullname}']")))

    new_one = driver.find_element(By.XPATH, f"//span[text()='{fullname}']")
    actions.move_to_element(new_one).click().perform()
    print('New Lead name: ',
          driver.find_element(By.XPATH, "//lightning-formatted-name[@data-output-element-id='output-field']").text)
    print('Status: ', driver.find_element(By.XPATH,
                                          "//records-record-layout-item[@field-label='Lead Status']//lightning-formatted-text[@slot='outputField']").text)
    # Converting Lead to account
    driver.find_element(By.XPATH,
                        "//div[@class='windowViewMode-normal oneContent active lafPageHost']//button[text()='Convert']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space(text())='Choose Existing Account']"))
    )
    driver.find_element(By.XPATH, "//span[normalize-space(text())='Choose Existing Account']").click()
    driver.find_element(By.XPATH, "//span[normalize-space(text())='Create New Account']").click()
    driver.find_element(By.XPATH, '//div[@class="modal-footer slds-modal__footer"]/span/button').click()
    time.sleep(3)
    driver.save_screenshot("ss.png")
    driver.find_element(By.XPATH, "//button[@title='Close this window']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Account']/one-app-nav-bar-item-dropdown"))
    )
    action = ActionChains(driver)
    account_dropdown = driver.find_element(By.XPATH,
                                           "//one-app-nav-bar-item-root[@data-id ='Account']/one-app-nav-bar-item-dropdown")
    action.move_to_element(account_dropdown).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[text()='{company}']"))
    )
    new_acc = driver.find_element(By.XPATH, f"//span[text()='{company}']")
    action.move_to_element(new_acc).click().perform()
    print('Account name: ', driver.find_element(By.XPATH, "//lightning-formatted-text[@slot='primaryField']").text)

@when('user creates a new account')
def new_acc(account, opportunity_name, closedate, stage, contact_name):
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Account']/one-app-nav-bar-item-dropdown"))
    )
    account_dropdown = driver.find_element(By.XPATH,
                                           "//one-app-nav-bar-item-root[@data-id ='Account']/one-app-nav-bar-item-dropdown")
    action.move_to_element(account_dropdown).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='New Account']"))
    )
    new_acc = driver.find_element(By.XPATH, "//span[text()='New Account']")
    action.move_to_element(new_acc).click().perform()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//div[@class='isModal inlinePanel oneRecordActionWrapper']//div/input[@class='slds-input' and @name='Name']"))
    )

    driver.find_element(By.XPATH, "//div/input[@class='slds-input' and @name='Name']").send_keys(account)
    driver.find_element(By.XPATH, "//button[text()='Save']").click()

    driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")

    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Account']/one-app-nav-bar-item-dropdown"))
    )
    account_dropdown = driver.find_element(By.XPATH,
                                           "//one-app-nav-bar-item-root[@data-id ='Account']/one-app-nav-bar-item-dropdown")
    action.move_to_element(account_dropdown).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[text()='{account}']"))
    )
    new_acc = driver.find_element(By.XPATH, f"//span[text()='{account}']")
    action.move_to_element(new_acc).click().perform()
    assert driver.find_element(By.XPATH,
                               "//lightning-formatted-text[@slot='primaryField']").text == account, "Name different"
    print('New Account : ', driver.find_element(By.XPATH, "//lightning-formatted-text[@slot='primaryField']").text)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Opportunity']/one-app-nav-bar-item-dropdown"))
    )

    oppdropdown = driver.find_element(By.XPATH,
                                      "//one-app-nav-bar-item-root[@data-id='Opportunity']/one-app-nav-bar-item-dropdown")
    action.move_to_element(oppdropdown).click().perform()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='New Opportunity']"))
    )
    new_opp = driver.find_element(By.XPATH, "//span[text()='New Opportunity']")
    action.move_to_element(new_opp).click().perform()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div/input[@name='Name']"))
    )
    driver.find_element(By.XPATH, "//div/input[@name='Name']").send_keys(opportunity_name)
    driver.find_element(By.XPATH, "//input[@aria-haspopup='listbox']").send_keys(account)
    accounts_list = driver.find_elements(By.XPATH, "//ul/li//lightning-base-combobox-formatted-text")
    for acc in accounts_list:
        if acc.text == account:
            acc.click()
            break

    driver.find_element(By.XPATH, "//div/input[@name='CloseDate']").send_keys(closedate)  # "31/12/2025"
    element = driver.find_element("xpath", "//div/button[@aria-label='Stage']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.find_element(By.XPATH, "//div/button[@aria-label='Stage']").click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, f"//lightning-base-combobox-item//span[text()='{stage}']"))
    ).click()
    driver.find_element(By.XPATH, "//div[@class='footer-full-width']//button[text()='Save']").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Opportunity']/one-app-nav-bar-item-dropdown"))
    )
    oppdropdown = driver.find_element(By.XPATH,
                                      "//one-app-nav-bar-item-root[@data-id='Opportunity']/one-app-nav-bar-item-dropdown")
    action.move_to_element(oppdropdown).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//span[text()='{opportunity_name}']"))
    )
    new_opp = driver.find_element(By.XPATH, f"//span[text()='{opportunity_name}']")
    action.move_to_element(new_opp).click().perform()
    print('Opportunity name: ', driver.find_element(By.XPATH,
                                                    "//records-record-layout-item[@field-label='Opportunity Name']//lightning-formatted-text").text)
    acc_name = driver.find_element(By.XPATH,
                                   "//records-record-layout-item[@field-label='Account Name']//records-hoverable-link//slot//slot")
    print('Oppor Attached Account: ', acc_name.text)

    # Contact attachment#
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Contact']/one-app-nav-bar-item-dropdown"))
    )

    contact_dropdown = driver.find_element(By.XPATH,
                                           "//one-app-nav-bar-item-root[@data-id ='Contact']/one-app-nav-bar-item-dropdown")
    action.move_to_element(contact_dropdown).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='New Contact']"))
    )
    new_contact = driver.find_element(By.XPATH, "//span[text()='New Contact']")

    action.move_to_element(new_contact).click().perform()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@name='salutation']")
    ))
    driver.find_element(By.XPATH, "//button[@name='salutation']").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//div/lightning-base-combobox-item/span/span[text()='Mr.']")
    ))
    driver.find_element(By.XPATH, "//div/lightning-base-combobox-item/span/span[text()='Mr.']").click()
    driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(contact_name)
    driver.find_element(By.XPATH, "//input[@placeholder='Search Accounts...']").send_keys(account)
    account_lis = driver.find_elements(By.XPATH, "//ul[@role='group']/li")
    for acc in account_lis:
        if acc.text == account:
            acc.click()
            break

    driver.find_element(By.XPATH,
                        "//runtime_platform_actions-action-renderer//button[text()='Save']").click()

    time.sleep(1)  # load Contact

    # Contact Check#
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//one-app-nav-bar-item-root[@data-id ='Contact']/one-app-nav-bar-item-dropdown"))
    )

    contact_dropdown = driver.find_element(By.XPATH,
                                           "//one-app-nav-bar-item-root[@data-id ='Contact']/one-app-nav-bar-item-dropdown")
    action.move_to_element(contact_dropdown).click().perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[text()='{contact_name}']"))
    )
    new_contact = driver.find_element(By.XPATH, f"//span[text()='{contact_name}']")

    action.move_to_element(new_contact).click().perform()

    acc_name = driver.find_element(By.XPATH,
                                   "//records-record-layout-item[@field-label='Account Name']//records-hoverable-link//slot//slot")
    print('Created Contact: ',
          driver.find_element(By.XPATH, "//slot[@name='outputField']/lightning-formatted-name").text)
    print('Contact Attached Account: ', acc_name.text)

    time.sleep(3)


