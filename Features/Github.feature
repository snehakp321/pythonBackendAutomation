Feature: Github API Validation

  Scenario: Session management check
    Given I have github auth credentials
    When I hit getrepo API of github
    Then status code of the response should be 401