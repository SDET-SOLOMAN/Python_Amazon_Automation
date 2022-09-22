# Created by Buywi at 9/21/2022
Feature: Test Scenarios for Amazon Home Page

  Scenario Outline: User can search for items and verify user search results
    Given Go to Amazon Home page
    When Navigate to the Search Bar and input <search_query>
    And Click on Amazon Search Icon
    Then Verify <search_result> is on Amazon Page
    Then Verify url contains <search_query>
    And Verify Cart has <num> items in it
    Examples:
      |search_query | search_result | num |
      | Watches     | "Watches"     |  0  |
      | Glasses     | "Glasses"     |  0  |
      | Rolex       | "Rolex"       |  0  |