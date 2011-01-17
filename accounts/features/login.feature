Feature: Sign up
  In order to use the site
  As a potential user
  I want to create a user account

  Scenario: Log In
    Given that I have an account
    When I go to the log in page
    And I login with valid credentials
    Then I should see "Hi, test_user"
