Feature: List index
  In order to find the list I want
  As a user
  I want to see a list of all my lists

  Scenario: View list
    Given that I am logged in
    And I have 1 list
    And I go to the list index
    Then I should see 1 list
