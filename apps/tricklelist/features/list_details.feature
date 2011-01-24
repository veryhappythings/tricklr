Feature: List Details
  In order to see what I need to do
  As a user
  I want to see the items contained in my list

  Scenario: View list
    Given that I am logged in
    And I have a list called "test list"
    And the list "test list" contains the item "test item 1"
    And the list "test list" contains the item "test item 2"
    And I go to the list details page for "test list"
    Then I should see the items "test item 1" and "test item 2"

