# Created by mikesoloman at 9/23/22

Feature: Test Scenarios for Amazon Today's Deals

  Scenario Outline: User can navigate from main Page to Today's Deals and Search for Products
    Given Open Home Page of Amazon
    When Select: Today's Deals Link
    Then Verify: <search_result> is shown on the Page
    When Search for <query_item> on Search Bar
    And Verify <search_text> is in First Item
    When Get the first item from the Search result
    And Add the item to the cart
    And Open Cart Page
    Then Verify item in the cart matches <search_text>

    Examples:
      | search_result   | query_item |   search_text   |
      | Today's Deals   | Watches    |   watch         |
      | Today's Deals   | Glasses    |   glasses       |