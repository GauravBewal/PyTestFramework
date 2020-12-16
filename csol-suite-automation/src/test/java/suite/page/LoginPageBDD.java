package suite.page;

/**
 * Page Object class for Login page
 * 
 * @author arth
 *
 */
import org.aeonbits.owner.ConfigFactory;
import org.openqa.selenium.support.PageFactory;

import suite.base.PageBase;
import suite.base.TestBase;
import suite.config.Configuration;
import suite.testdata.LoginTestData;

public class LoginPageBDD extends TestBase {

	private final PageBase driver;
	private static Configuration configProperty;


	public LoginPageBDD() {
		configProperty = ConfigFactory.create(Configuration.class);
		setDriver(configProperty.getBrowser());
		setEnv(configProperty.getEnv());
		this.driver = new PageBase(getDriver());
		PageFactory.initElements(getDriver(), this);
	}

	/**
	 * for getting page url of demo page
	 * 
	 * @param //pageURL
	 * @return page url of the demo page
	 */
	public LoginPageBDD getLoginPage() {
		driver.NavigateTo(getEnv().concat(LoginTestData.PAGE_URL));
		return this;
	}

	/**
	 * for getting the page title
	 * 
	 * @return page title
	 */
	public String getPageTitle() {

		return driver.getPagetitle();
	}



	/**
	 * Terminate the webdriver instance
	 */
	public void quit() {
		tearDown();
	}

}
