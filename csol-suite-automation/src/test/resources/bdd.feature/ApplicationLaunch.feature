Feature: Cyware CSOL Application Launch

  @UITest
  Scenario: Verify Page Title
    Given the user launch the application
    When the user is on cyware csol login page
    Then the page title should be "Login | Cyware Security Orchestration Layer"
    And the application should be closed
