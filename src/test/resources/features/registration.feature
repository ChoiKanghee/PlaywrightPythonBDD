Feature: Registration Feature

  Scenario Outline: Validating the Registration feature

    Given I navigate to qa.way2automation.com
    When I enter the name as "<name>"
    Then I enter the phone number as "<phonenumber>"
    And I enter the email as "<email>"
    And I enter the country as "<country>"
    And I enter the city as "<city>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    And I click on the submit button

    Examples:
      | name        | phonenumber | email                      | country | city   | username       | password  |
      | Rahul Arora | 9711111558   | trainer@way2automation.com | India   | Delhi  | rahularora1985 | ssdfsdfsf |
      | Raman Arora | 9999994664   | info@way2automation.com    | Germany | Berlin | ramanarora1986 | dsfsfds   |


    Scenario: Login
      Given i login to page