# Created by mikesoloman at 10/5/22
Feature: Testing Amazon 404 pages, window handling, waiting for windows to open, switch, close, go back
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store all the original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened t&c window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
    Then Verify Amazon T&C page is reopened