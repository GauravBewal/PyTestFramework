package suite.init;

import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;

import io.appium.java_client.android.AndroidDriver;
import suite.constants.WebdriverConstants;

/**
 * This class contains all the browser related features in the automation
 * framework.
 * 
 * @author arth
 *
 */
public class BrowserFactory {
	private static final ThreadLocal<WebDriver> browser = new ThreadLocal<WebDriver>();
	private static OptionsManager op;

	/**
	 * get the web browser instance
	 * 
	 * @return browser invokes the instance of the webbrowser
	 */
	public static WebDriver getBrowser() {
		return browser.get();
	}

	/**
	 * set the web browser instance
	 * 
	 * @param browser sets the instance of the webbrowser
	 */
	public static void setBrowser(String browserDriver) {

		op = new OptionsManager();

		switch (browserDriver) {

		case "chrome-ng":
			browser.set(new ChromeDriver(op.getChromeOptions()));
			break;
			
		case "chrome-headless":
			browser.set(new ChromeDriver(op.getChromeHeadlessOptions()));
			break;

		case "chrome-grid":
			try {
				browser.set(new RemoteWebDriver(new URL(WebdriverConstants.GRID_URL), op.getChromeGridOptions()));
			} catch (MalformedURLException e) {
				e.printStackTrace();
			}
			break;

		case "chrome-android":
			try {
				browser.set(new AndroidDriver(new URL(WebdriverConstants.APPIUM_URL), op.getChromeAndroidOptions()));
			} catch (MalformedURLException e) {
				e.printStackTrace();
			}
			break;

		default:
			browser.set(new ChromeDriver(op.getChromeOptions()));
			break;
		}
	}

	/**
	 * close the web browser
	 * 
	 * @param driver webdriver instance
	 */
	public static void closeBrowser(WebDriver driver) {
		driver.quit();
		browser.remove();
	}
}
