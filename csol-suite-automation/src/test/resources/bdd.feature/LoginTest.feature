Feature: Cyware CSOL Login

  @UITest
  Scenario Outline: Verify Successful Login
    Given the user launches the application
    When the user is on cyware login page
    Then the user will enter "<EmailID>" and "<Password>"
    Then the user will click login button
    Then the user on Dashboard
    Then Close browser

    Examples:
      | EmailID | Password |
      | system.default@tld.com | system@7*9 |