Feature: Salesforce Lead Creation

  Scenario: User creates a new lead in Salesforce
    Given the user navigates to the Salesforce lead creation page
    When the user enters the salutation, first name, last name, and company
    Then the user should be able to save the new lead successfully