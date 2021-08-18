Feature: Verify Successful Login on CSOL

  @smoke
  Scenario: Validate Login
    Given the user is on CSOL Login page
    When the user enters UserName and Password
    And user clicks on login button
    Then User is on dashboard page