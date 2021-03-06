Feature: Sign up
  In order to use the site
  As a potential user
  I want to create a user account

  Scenario: Log In
    Given that I have an account with username "test_user" and password "test_password"
    When I go to the log in page
    And I login with username "test_user" and password "test_password"
    Then I should see "test_user"

  Scenario: Invalid Log In
    Given that I have an account with username "test_user2" and password "test_password"
    When I go to the log in page
    And I login with username "wrong_user" and password "wrong_password"
    Then I should see "Your username and password didn't match. Please try again."
