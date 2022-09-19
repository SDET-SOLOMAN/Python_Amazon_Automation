# Created by mikesoloman at 9/19/22
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Watches into search field
    And Click on search icon
    Then Product results for Watches are shown
    And First result contains Watches