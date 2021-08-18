Feature: Redirect to Admin Panel Redirection
  @smoke
  Scenario: Verify user is able to redirect on Admin Panel
    Given the user is in CSOL Dashboard
    When the user clicks on the Admin panel icon on the bottom left
    Then user should be redirected to CSOL Admin panel - listing page

  Scenario: Verify Console Status Page
    Given the user is in Admin panel - listing page
    When the user clicks on any of the menu listing
    Then user should be redirected to the respective menu details