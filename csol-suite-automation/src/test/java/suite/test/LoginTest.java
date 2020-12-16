package suite.test;

import org.apache.commons.io.filefilter.FalseFileFilter;
import org.testng.Assert;
import org.testng.annotations.Test;

import suite.base.TestBase;
import suite.page.LoginPage;
import suite.testdata.LoginTestData;

/**
 * Contain all the tests related to login feature
 * 
 * @author arth
 *
 */
public class LoginTest extends TestBase {

	private LoginPage lp;

	/**
	 * create page url
	 * 
	 * @return home page page url
	 */
	private String getPageURL() {
		return getEnv().concat(LoginTestData.PAGE_URL);
	}

	@Test(description = "Verify successfully login with invalid credentials", groups = { "done", "LoginTest" })
	public void tcID_01() {
		lp = new LoginPage();

		// Modular way
		// fluent PO
		String actual = lp.getLoginPage()// loading the webpage
				.enterUserName(LoginTestData.USERNAME)// entering uname
				.enterPassword(LoginTestData.PASSWORD)// entering password
				.clickLoginBtn()// click on login btn
				.getValidationMessage();// getting from webpage/application

		Assert.assertTrue(actual.trim().contains(LoginTestData.EXPECTED_VALIDATION_MESSAGE));
	}

	@Test(enabled = false, description = "Verify successfully login with invalid credentials", groups = { "done",
			"LoginTest" })
	public void tcID_02() {
		lp = new LoginPage();

		// Traditional way
		lp.getLoginPage();// loading the webpage
		lp.enterUserName(LoginTestData.USERNAME);// entering uname
		lp.enterPassword(LoginTestData.PASSWORD);// entering password
		lp.clickLoginBtn();// click on login btn

		String actual = lp.getValidationMessage();// getting from webpage/application
		Assert.assertTrue(actual.trim().contains(LoginTestData.EXPECTED_VALIDATION_MESSAGE));
	}

}