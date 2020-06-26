@api
Feature: Endpoint listing stock market data
  As a stock broker
  I need an api containing historical stock market data
  In order to prepare accurate reports

  Scenario: Endpoint is built as per initial from/to dates
    Given API is created
    When viewing the endpoint
    Then first available date is the initial From date
    And last available date is the initial To date

  Scenario Outline: Data order
    Given API is up and running
    When observing a stock
    Then <key> should show on position <order>

    Examples: Keys order
      | key          | order |
      | date           | 0     |
      | open           | 1     |
      | high           | 2     |
      | low            | 3     |
      | close          | 4     |
      | adjusted_close | 5     |
      | volume         | 6     |


  Scenario: No ‘close’ prices can be zero or negative
    #Given API is up and running
    When observing close price
    Then price must be greater than 0

  Scenario: The ‘high’ price must always be greater than or equal to the ‘close’ price
    #Given API is up and running
    When observing high price
    Then price must be greater than or equal to close price

  Scenario: The ‘low’ price must always be less than or equal to the ‘close’ price
    #Given API is up and running
    When observing low price
    Then price must be less than or equal to close price

  Scenario: The ‘low’ price must always be less than or equal to the ‘close’ price
    #Given API is up and running
    When observing low price
    Then price must be less than or equal to close price


