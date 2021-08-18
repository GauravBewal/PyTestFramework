package Init;

import logger.Log;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.Reporter;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.GregorianCalendar;

public class Assertions {
    public boolean testCaseStatus = true;
    private final WebDriver driver;
    private final File file;
    private final String testScreenshotDir;
    boolean testStatus;


    public Assertions(WebDriver driver){
        file = new File(" ");
        testScreenshotDir = file.getAbsoluteFile()
                + "src/main/java/OutputFailures";
        this.driver = driver;
    }



    public String screenShot(){
        String screenshotPath = "screenshot" + new SimpleDateFormat("MM-dd-yyyy-HH-mm-ss")
                .format(new GregorianCalendar().getTime())
                +".png";
        System.out.println(screenshotPath);
        File scrFile = ((TakesScreenshot)driver)
                .getScreenshotAs(OutputType.FILE);
        try{
            FileUtils.copyFile(scrFile, new File(testScreenshotDir + screenshotPath));

        } catch (IOException exception) {
            exception.printStackTrace();
            screenshotPath = " ";
        }
        return screenshotPath;
    }



    public void screenShot(String message){
        String screenshotPath = message + "screenshot" + new SimpleDateFormat("MM-dd-yyyy-HH-mm-ss")
                .format(new GregorianCalendar().getTime())
                +".png";

        System.out.println(screenshotPath);
        File scrFile = ((TakesScreenshot)driver)
                .getScreenshotAs(OutputType.FILE);
        try{
            FileUtils.copyFile(scrFile, new File(testScreenshotDir + screenshotPath));
        } catch (IOException exception) {
            exception.printStackTrace();
        }
    }



    public boolean verifyEquals(Object actual, Object expected, String message, boolean screenshotOnFailure, boolean exitOnFailure){
        testStatus = true;
        Reporter.log("<br>");
        try {
            Assert.assertEquals(actual, expected, message);
            Reporter.log("<Font Color=#008000> PASS </Font>" + message);
        } catch (AssertionError e){
            testStatus = false;
            if(screenshotOnFailure){
                Reporter.log("<Font Color=red> FAIL </Font>" + message + "Actual: " +actual + "Expected: " +
                        expected + " Please check the screenshot " + "<a href ='"+screenShot()
                        + "'> <Font Color=red> here </Font> </a>");
            }
            if(exitOnFailure){
                Reporter.log("<br>");
                Reporter.log("Exiting this functionality as exitOnFail flag is set to True. Will move to next test");
                throw e;
            }
            Reporter.log("<Font Color=red> FAIL </Font>" + message + "Actual: " + actual + "Expected: " + expected);
        }
        return testStatus;
    }



    public boolean verifyTrue(boolean condition, String message, boolean screenshotOnFailure,
                              boolean exitOnFailure){
        Reporter.log("<br>");
        try{
            Assert.assertTrue(condition,message);
            Reporter.log("<Font Color=#008000> PASS </Font>" + message );
        } catch (AssertionError e) {
            Log.info(message);
            this.testCaseStatus = false;

            if(screenshotOnFailure) {
                Reporter.log("<Font Color=red> FAIL </Font>" + message + "Actual: FALSE Expected : TRUE."
                        + " Please check the screenshot "
                        + "<a href ='" +screenShot()+"'> <Font Color=red> here </Font> </a>");
            } else {
                Reporter.log("<Font Color=red> FAIL </Font>"+ message);
            }
            if(exitOnFailure) {
                Reporter.log("<br>");
                Reporter.log("Exiting this function as exitOnFail flag is set to True.");
                throw e;
            }
        }
        return this.testCaseStatus;
    }

}
