# Created by mikesoloman at 9/28/22
Feature: Test Scenarios for Best Seller Box count

  Scenario Outline: Verify 5 Boxes in Best Seller Page
    Given Go to Best Seller's Page
    When Count Best Sellers Nav Boxes
    Then Verify there are <num> boxes
    Examples:
      | num  |
      |  5   |

  Scenario Outline: Verify All The boxes and Fields Are Present in Customer Service's UI Page
    Given Go to Customer Service Page
    Then Verify <greeting_text> is present
    And Verify <num> amount of boxes underneath of Greeting text
    And Confirm <library_text> is about Library Search Box
    Then Verify Library Search Bar is there
    Then Verify <num_lib> boxes are there
    And Verify <help> text
    Examples:
    |         greeting_text             | num |         library_text      | num_lib |     help         |
    |Welcome to Amazon Customer Service |  9  |  Search our help library  |    7    | All help topics  |