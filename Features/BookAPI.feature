Feature: Verify if Books are added and deleted using Library API

  @smoke @Library
  Scenario: Verify AddBook API functionality
    Given the book details which needs to be added to library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of the response should be 200

  @regression @Library
  Scenario Outline: Verify AddBook API functionality
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of the response should be 200
    Examples:
      | isbn   | aisle  |
      | 37423  | 323674 |
      | 374233 | 34674  |