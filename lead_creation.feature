Feature: Salesforce Lead Creation

  Scenario: User creates a new lead in Salesforce
    Given the user navigates to the Salesforce lead creation page
    When the user enters the salutation, first name, last name, and company
    Then the user should be able to save the new lead successfully

  Scenario: User creates a new login user and creates new lead in Salesforce
    Given the user navigates to the Salesforce lead creation page
    Then user logs in to the portal
    When user creates a new lead
    Then the user should be able to save the new lead successfully

  Scenario: User creates a new account
    Given the user navigates to the Salesforce lead creation page
    Then user logs in to the portal
    When user creates a new account
    Then the user should be able to save the new lead successfully
