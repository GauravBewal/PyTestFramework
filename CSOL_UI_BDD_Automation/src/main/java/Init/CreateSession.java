package Init;

import io.cucumber.java.Scenario;
import io.github.bonigarcia.wdm.WebDriverManager;
import logger.Log;
import org.apache.commons.io.FileUtils;
import org.junit.After;
import org.junit.Before;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.Platform;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.phantomjs.PhantomJSDriver;
import org.openqa.selenium.phantomjs.PhantomJSDriverService;
import org.openqa.selenium.remote.DesiredCapabilities;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.GregorianCalendar;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

/**
     * This class contains web driver create and teardown methods. These are required while
     * running each and every scenario. Methods are defined under @Before and @After annotations
     * to get initialized at start and end of the test.
     * @Author Sandeep
    */

public class CreateSession {

    private static final ThreadLocal<WebDriver> webDriver = new ThreadLocal<WebDriver>();

    @Before
    public static void createDriver(){
        String browserName = System.getProperty("browser");
        String headless = System.getProperty("headless");
        DesiredCapabilities capabilities = new DesiredCapabilities();
        loadConfigProperties();

        if(browserName == null){
            browserName = "chrome";
        }

        if(headless != null && headless.equalsIgnoreCase("yes")){
            System.setProperty("phantom.binary.path", "libs/phantomjs");
            String user_agent = "Chrome";
            DesiredCapabilities cap = DesiredCapabilities.phantomjs();
            cap.setCapability(PhantomJSDriverService.PHANTOMJS_PAGE_SETTINGS_PREFIX +"userAgent", user_agent);
            cap.setCapability(PhantomJSDriverService.PHANTOMJS_PAGE_SETTINGS_PREFIX +"loadImages", true);
            cap.setCapability(PhantomJSDriverService.PHANTOMJS_PAGE_SETTINGS_PREFIX +"javascriptEnabled", true);

            webDriver.set(new PhantomJSDriver(cap));
        }

        else if (browserName.equalsIgnoreCase("FireFox")){
            WebDriverManager.firefoxdriver().setup();
            capabilities.setBrowserName("Firefox");
            webDriver.set(new FirefoxDriver());
        }

        else if (browserName.equalsIgnoreCase("chrome")){
            String OS = System.getProperty("os.name");
            if (OS.contains("Windows")){
                WebDriverManager.chromedriver().setup();
                capabilities.setBrowserName("Chrome");
                capabilities.setPlatform(Platform.WIN10);
                webDriver.set(new ChromeDriver());
            }

            else if(OS.contains("Linux")){
                WebDriverManager.chromedriver().setup();
                capabilities.setBrowserName("Chrome");
                capabilities.setPlatform(Platform.LINUX);
                webDriver.set(new ChromeDriver());
            }

            else if(OS.contains("Mac")){
                WebDriverManager.chromedriver().setup();
                capabilities.setBrowserName("Chrome");
                capabilities.setPlatform(Platform.MAC);
                webDriver.set(new ChromeDriver());
            }
        }
        getWebDriver().manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
        getWebDriver().manage().window().maximize();
    }

    public static WebDriver getWebDriver(){
        System.out.println("WebDriver: " + webDriver.get());
        return webDriver.get();
    }

    @After
    public void teardown(Scenario scenario){
        if(scenario.isFailed()){
            try{
                TakesScreenshot ts = (TakesScreenshot)getWebDriver();
                File source = ts.getScreenshotAs(OutputType.FILE);
                FileUtils.copyFile(source, new File(".//src//main//java//OutputFailures//"+"FailedScreenshot"+
                        new SimpleDateFormat("MM-dd-yyyy-HH-mm-ss")
                                .format(new GregorianCalendar().getTime())+".png"));
                Log.info("Scenario failed and Screenshot saved in OutputFailure folder");
            } catch (IOException e) {
               Log.info("Exception while taking screenshot" + e.getMessage());
            }
        }
    }


    public static void loadConfigProperties(){
        Properties properties = System.getProperties();
        try {
            properties.load(new FileInputStream("src/test/resources/config.properties"));
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }
}
