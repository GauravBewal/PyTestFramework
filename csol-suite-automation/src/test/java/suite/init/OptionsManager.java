package suite.init;

import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.Platform;
import org.openqa.selenium.UnexpectedAlertBehaviour;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.github.bonigarcia.wdm.WebDriverManager;
import suite.constants.WebdriverConstants;

/**
 * This class contains all the browser configurations for the automation suite
 * 
 * @author arth
 *
 */
public class OptionsManager {

	private ChromeOptions option;
	private DesiredCapabilities caps;

	public ChromeOptions getChromeOptions() {
		option = new ChromeOptions();
		Map<String, Object> prefs = new HashMap<String, Object>();
		Map<String, Object> profile = new HashMap<String, Object>();
		Map<String, Object> contentSettings = new HashMap<String, Object>();

		contentSettings.put("geolocation", 1);
		profile.put("managed_default_content_settings", contentSettings);
		prefs.put("profile", profile);
		option.setExperimentalOption("prefs", prefs);
		option.addArguments("--incognito");
		option.addArguments("disable-infobars");
		option.addArguments("--disable-extensions"); 
		option.addArguments("--disable-gpu"); 
		option.addArguments("--disable-dev-shm-usage"); 
		option.addArguments("--no-sandbox"); 
		option.addArguments("--disable-notifications");
		option.addArguments("--disable-popup-blocking");
		option.addArguments("start-maximized");
		option.addArguments("enable-automation");
		option.setCapability(CapabilityType.UNEXPECTED_ALERT_BEHAVIOUR, UnexpectedAlertBehaviour.ACCEPT);
		option.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
		option.setCapability(CapabilityType.SUPPORTS_JAVASCRIPT, true);
		WebDriverManager.chromedriver().setup();
		//System.setProperty("webdriver.chrome.driver", WebdriverConstants.DRIVER_PATH);
		return option;
	}
	
	public DesiredCapabilities getChromeAndroidOptions() {

		caps = new DesiredCapabilities();
		caps.setCapability("BROWSER_NAME", WebdriverConstants.BROWSER_NAME);
		caps.setCapability("VERSION", WebdriverConstants.ANDROID_VERSION);
		caps.setCapability("deviceName", WebdriverConstants.DEVICE_NAME);
		caps.setCapability("platformName", WebdriverConstants.PLATFORM_NAME);
		caps.setCapability("avd", WebdriverConstants.SIMULATOR_ID);
		caps.setCapability("appPackage", WebdriverConstants.APP_PACKAGE);
		caps.setCapability("appActivity", WebdriverConstants.APP_ACTIVITY);
		return caps;
	}

	public ChromeOptions getChromeHeadlessOptions() {

		option = new ChromeOptions();
		Map<String, Object> prefs = new HashMap<String, Object>();
		Map<String, Object> profile = new HashMap<String, Object>();
		Map<String, Object> contentSettings = new HashMap<String, Object>();

		contentSettings.put("geolocation", 1);
		profile.put("managed_default_content_settings", contentSettings);
		prefs.put("profile", profile);
		option.setExperimentalOption("prefs", prefs);
		option.addArguments("--incognito");
		option.addArguments("disable-infobars"); 
		option.addArguments("--disable-extensions"); 
		option.addArguments("--disable-gpu"); 
		option.addArguments("--disable-dev-shm-usage"); 
		option.addArguments("--no-sandbox"); 
		option.addArguments("--disable-notifications");
		option.addArguments("--disable-popup-blocking");
		option.addArguments("enable-automation");
		option.addArguments("--headless");
		option.setCapability(CapabilityType.UNEXPECTED_ALERT_BEHAVIOUR, UnexpectedAlertBehaviour.ACCEPT);
		option.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
		option.setCapability(CapabilityType.SUPPORTS_JAVASCRIPT, true);
		WebDriverManager.chromedriver().setup();
		return option;
	}

	public ChromeOptions getChromeGridOptions() {
		option = new ChromeOptions();
		option.addArguments("--incognito");
		option.addArguments("lang=en_GB");
		option.setCapability(CapabilityType.UNEXPECTED_ALERT_BEHAVIOUR, UnexpectedAlertBehaviour.ACCEPT);
		option.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
		option.setCapability(CapabilityType.SUPPORTS_JAVASCRIPT, true);
		option.setCapability(CapabilityType.PLATFORM_NAME, Platform.LINUX);
		option.setCapability("screenResolution", "1280x720");
		option.setCapability("tz", "Asia/Kolkata");
		option.setCapability("idleTimeout", 150);
		option.setCapability("recordVideo", false);
		return option;
	}

}