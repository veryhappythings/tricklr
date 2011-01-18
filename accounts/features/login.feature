Feature: Sign up
  In order to use the site
  As a potential user
  I want to create a user account

  Scenario: Log In
    Given that I have an account with username "test_user" and password "test_password"
    When I go to the log in page
    And I login with valid credentials
    Then I should be redirected
