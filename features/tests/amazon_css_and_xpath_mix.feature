# Created by mikesoloman at 9/28/22
Feature: Test Scenarios for Search Bar in Different Pages

  Scenario Outline: User can search for items in different web pages of Amazon
    Given Navigate to <website>
    When Locate The Search Bar
    And Search for <search_item> and click Search Icon
    Then Verify <search_item> is in url
    Then Verify <search_result> is in Page Description
    And Verify at least <num> of items in the page search result
    Examples:
      |                         website                     | search_item  | search_result | num |
      |           https://www.amazon.com/music/             | watches      | "watches"     | 55  |
      |       https://www.amazon.com/gp/bestsellers/        | rolex        | "rolex"       | 25  |
      |https://www.amazon.com/gp/help/customer/display.html | advil        | "advil"       | 15  |