package suite.page;

import org.aeonbits.owner.ConfigFactory;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import suite.base.PageBase;
import suite.base.TestBase;
import suite.config.Configuration;
import suite.testdata.LoginTestData;

/**
 * Page Object class for Login page
 * 
 * @author arth
 *
 */
public class LoginPage extends TestBase {

	private final PageBase driver;
	private static Configuration configProperty;


	@FindBy(xpath="//input[@type='text']")
	private WebElement userNameTxtBox;

	@FindBy(xpath="//input[@type='password']")
	private WebElement passwordTxtBox;

	@FindBy(xpath = "//button/span")
	private WebElement loginBtn;

	@FindBy(css = "span.text-uppercase")
	private WebElement welcomeMessage;

	@FindBy(css = "p.cy-error")
	private WebElement validationMessage;


	public LoginPage() {
		configProperty = ConfigFactory.create(Configuration.class);
		setDriver(configProperty.getBrowser());
		setEnv(configProperty.getEnv());
		this.driver = new PageBase(getDriver());
		PageFactory.initElements(getDriver(), this);
	}

	/**
	 * for getting page url of demo page
	 * 
	 * @return page url of the demo page
	 */
	public LoginPage getLoginPage() {
		driver.NavigateTo(getEnv().concat(LoginTestData.PAGE_URL));
		return this;
	}

	/**
	 * for entering the user name
	 * 
	 * @param username
	 * @return ob
	 */
	public LoginPage enterUserName(String username) {
		driver.setText(userNameTxtBox, username);
		return this;
	}

	/**
	 * for entering the password
	 * 
	 * @param password
	 * @return object of current class
	 */
	public LoginPage enterPassword(String password) {
		driver.setText(passwordTxtBox, password);
		return this;
	}

	/**
	 * for clicking on login button
	 * 
	 * @return object of current class
	 */
	public LoginPage clickLoginBtn() {
		driver.clickOn(loginBtn);
		return this;

	}

	/**
	 * for getting the authentication validation message
	 * 
	 * @return validation message
	 */
	public String getValidationMessage() {

		return driver.getText(validationMessage);
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
