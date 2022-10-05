# Created by mikesoloman at 10/3/22
Feature: Test Scenarios using explicit waits as well as expected conditions, using loops to count items.

  Scenario Outline: Verify Dresses and Colors
    Given Amazon Home Page
    Then Verify Sign_IN is clickable
    When Verify SIGN_IN Popup is still there for <seconds>
#    Then Verify Sign_IN is clickable
    Then Verify Sign_in disappears
    When Navigate to the given <Dress Page>
    Then Verify <Expected Colors> matching Actual Colors for the item
    Examples:
      | seconds  |                Dress Page                            | Expected Colors |
      |    1    |     https://www.amazon.com/gp/product/B07BJKRR25/    | Black; Blue, Over Dye; Bright White; Dark Blue Vintage; Dark Indigo/Rinsed; Dark Khaki Brown; Dark Wash; Indigo Wash; Light Blue Vintage; Light Khaki Brown; Light Wash; Medium Blue, Vintage; Medium Wash; Olive; Rinsed; Sage Green; Vintage Wash; Washed Black; Washed Grey |
      |    1    |          https://www.amazon.com/dp/B081YS2F7N        | Army Green; Black; Blue; Brown; Burgundy; Caramel; Dark Blue; Denim Blue; Gray; Green; Khaki; Light-green; Orange; Pink; Purple; Red; Rose Red; White; Yellow |

    Scenario Outline: Amazon Whole Foods, Closing popups, verifying items have word Regular, and items have Product Name
    Given Whole Foods Amazon Deals
    When If there is a popup, Close the Whole Foods is not available for this location popup
    Then Verify items have <expected_word> and item has a Name/Description
    Examples:
      | expected_word |
      |    Regular    |