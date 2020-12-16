package suite.stepDefination;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import suite.page.LoginPage;


/**
 * Login Step Defination Class contains all the concrete methods for the steps
 * defined on the LoginTest.feature file
 *
 * @author arth
 *
 */

public class LoginStepDef {

    private LoginPage lp;
   // LoginPage lp = new LoginPage();

    @Given("the user launches the application")
    public void the_user_launches_the_application() {
        lp = new LoginPage();
    }

    @When("the user is on cyware login page")
    public void the_user_is_on_cyware_login_page() {
        lp.getLoginPage();
    }

    @Then("the user will enter \"(.*)\" and \"(.*)\"")
    public void user_enters_email_and_password(String EmailID, String Password ){
        lp.enterUserName(EmailID);
        lp.enterPassword(Password);
    }

    @Then("the user will click login button")
    public void user_click_login_button() {
        lp.clickLoginBtn();
    }

    @Then("the user on Dashboard")
    public void user_redirect_dashboard() throws InterruptedException {
        Thread.sleep(2000);
        String Dashboard = lp.getPageTitle();
        System.out.println(Dashboard);
    }

    @Then("Close browser")
    public void close_browser() throws InterruptedException {
        Thread.sleep(2000);
        lp.quit();
    }

}
