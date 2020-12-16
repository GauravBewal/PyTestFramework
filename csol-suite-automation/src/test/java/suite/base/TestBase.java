package suite.base;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Optional;
import org.testng.annotations.Parameters;

import suite.init.SessionInit;
import suite.listener.WebDriverListener;
import suite.testdata.AppData;

/**
 * This is Test Base class for automation framework contains all the common test
 * prerequisites for automation
 * 
 * @author arth
 *
 */
public class TestBase extends EnvBase {

	private WebDriver driver;
	private EventFiringWebDriver eventHandler;
	private WebDriverListener ecapture;
	private String browser;
	private String env;

	/**
	 * Initiate the enviroment url
	 * 
	 * @param env
	 */
	@Parameters({ "env" })
	@BeforeClass
	public void setUpEnv(@Optional("qa") String env) {
		setEnv(env);
		this.env = env;
	}

	/**
	 * Setting the browser
	 * 
	 * @param browser
	 */
	@Parameters({ "browser" })
	@BeforeMethod
	public void setDriver(@Optional("chrome-ng") String browser) {

		SessionInit.getDriverSession().initiateBrowserSession(browser);
		this.driver = SessionInit.getDriverSession().getBrowserSession();

		this.eventHandler = new EventFiringWebDriver(driver);
		this.ecapture = new WebDriverListener();
		this.eventHandler.register(ecapture);
		this.browser = browser;
	}

	/**
	 * for closing the browser
	 */
	@AfterMethod
	public void tearDown() {
		this.eventHandler.unregister(ecapture);
		SessionInit.getDriverSession().terminateBrowserSession(driver);
	}

	/**
	 * Loading browser instance
	 * 
	 * @return driver instance
	 */
	public EventFiringWebDriver getDriver() {
		return this.eventHandler;
	}

	@Override
	public String getEnv() {
		return super.getEnv();
	}

	public String getBrowserLang() {
		return browser;
	}

	public String getAppLang() {
		return env;
	}

	public XSSFWorkbook getTestData() throws IOException {
		return new XSSFWorkbook(new FileInputStream(new File(AppData.TEST_DATA)));
	}
}
