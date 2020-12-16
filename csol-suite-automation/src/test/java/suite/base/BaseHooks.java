/*
 * package suite.base;
 * 
 * import org.aeonbits.owner.ConfigFactory; import
 * org.openqa.selenium.WebDriver; import
 * org.openqa.selenium.support.events.EventFiringWebDriver;
 * 
 * import cucumber.api.java.After; import cucumber.api.java.Before; import
 * suite.config.Configuration; import suite.init.SessionInit; import
 * suite.listener.WebDriverListener;
 * 
 * public class BaseHooks extends EnvBase { private WebDriver driver; private
 * EventFiringWebDriver eventHandler; private WebDriverListener ecapture;
 * private static Configuration configProperty;
 * 
 * @Before("UITest") public void setup() {
 * 
 * configProperty = ConfigFactory.create(Configuration.class);
 * setEnv(configProperty.getEnv());
 * SessionInit.getDriverSession().initiateBrowserSession(configProperty.
 * getBrowser());
 * //SessionInit.getDriverSession().initiateBrowserSession(LoadProp.getproperty(
 * "Browser")); this.driver =
 * SessionInit.getDriverSession().getBrowserSession(); this.eventHandler = new
 * EventFiringWebDriver(driver); this.ecapture = new WebDriverListener();
 * this.eventHandler.register(ecapture); }
 * 
 * @After("UITest") public void teardown() {
 * 
 * this.eventHandler.unregister(ecapture);
 * SessionInit.getDriverSession().terminateBrowserSession(driver); }
 * 
 * public EventFiringWebDriver getDriver() { return this.eventHandler; }
 * 
 * @Override public String getEnv() { return super.getEnv(); }
 * 
 * 
 * }
 */