# Created by mikesoloman at 10/5/22
Feature: Testing Amazon Best Seller Page, looping through window handling,
  verifying correct window swtiches
  # Enter feature description here

  Scenario Outline: User can open different links on Best Seller page and navigate through windows
    Given Open Amazon Best Seller Page
    Then Verify <text1> is on page
    When Loop through links and verify
    Examples:
    |     text1   |
    | Best Sellers|

