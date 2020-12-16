package suite.stepDefination;

import org.testng.Assert;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import suite.page.LoginPage;
import suite.page.LoginPageBDD;

/**
 * Application Launch Step Defination Class contains all the concrete methods for the steps
 * defined on the ApplicationLaunch.feature file
 * 
 * @author arth
 *
 */
public class ApplicationLaunchDef {

	private LoginPage lp;

	@Given("the user launch the application")
	public void the_user_launch_the_application() {
		lp = new LoginPage();
	}

	@When("the user is on cyware csol login page")
	public void the_user_is_on_cyware_csol_login_page() {
		lp.getLoginPage();
	}

	@Then("the page title should be {string}")
	public void the_page_title_should_be(String pageTitle) {
		Assert.assertEquals(lp.getPageTitle(), pageTitle);
	}

	@Then("the application should be closed")
	public void the_application_should_be_closed() throws InterruptedException {
		//Thread.sleep(1000);
		lp.quit();
	}
}