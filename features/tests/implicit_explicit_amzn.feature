# Created by mikesoloman at 9/30/22
Feature: Test Scenarios for Amazon Products

  Scenario Outline: User can go through Amazon products, verify colors, sizes
    # using combo of implicit and explicit waits
    Given Go to Amazon Main Page
    When Search for <item> in Search Bar
    Then Verify <item> is in Current Url


    Examples: