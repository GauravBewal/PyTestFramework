package Init;

import logger.Log;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.*;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CommonMethods extends Assertions {

    WebDriver driver = null;
    public final int timeOut = 45;
    protected File file = new File("");

    public CommonMethods(WebDriver driver) throws IOException {
        super(driver);
        this.driver = driver;
    }

    public void get(String url){
        driver.get(url);
    }

    public void clickOnElementUsingActions(By element){
        Actions actions = new Actions(driver);
        actions.moveToElement(driver.findElement(element));
        actions.click().perform();
    }

    public void clickOnElementUSingJS(By element){
        JavascriptExecutor js = (JavascriptExecutor) driver;
        WebElement webElement = driver.findElement(element);
        js.executeScript("arguments[0].click();",webElement);
    }

    public int getIntValue(String getInt){
        Pattern intsOnly = Pattern.compile("\\d");
        Matcher makeMatch = intsOnly.matcher(getInt);
        makeMatch.find();
        String inputInt = makeMatch.group();
        return Integer.parseInt(inputInt);
    }

    public String getTitle(){
        return driver.getTitle();
    }

    public void waitForPageToLoad(String PageName){
        String pageLoadStatus;
        JavascriptExecutor js;
        do {
            js = (JavascriptExecutor) driver;
            pageLoadStatus = (String) js.executeScript("return document.readyState");
            Log.info(".");
        } while (!pageLoadStatus.equals("complete"));
        Log.info(PageName + "page loaded successfully");
    }

    public Boolean isElementPresent(By targetElement) throws InterruptedException{
        Boolean isPresent = driver.findElements(targetElement).size() > 0;
        return isPresent ;
    }


    public Boolean isElementNotPresent(By targetElement) throws InterruptedException{
        Boolean isPresent = driver.findElements(targetElement).size() == 0;
        return isPresent ;
    }

    public boolean waitForVisibility(By targetElement){
        try{
            WebDriverWait wait = new WebDriverWait(driver, timeOut);
            wait.until(ExpectedConditions.visibilityOfElementLocated(targetElement));
            return true;
        } catch (TimeoutException e) {
            System.out.println("Element is not visible: " + targetElement);
            System.out.println();
            System.out.println(e.getMessage());
            throw new TimeoutException();
        }
    }

    public boolean waitForElementToBeClickable(By targetElement){
        try{
            WebDriverWait wait = new WebDriverWait(driver, timeOut);
            wait.until(ExpectedConditions.elementToBeClickable(targetElement));
            return true;
        } catch (TimeoutException e){
            System.out.println("Element is not clickable: " + targetElement);
            System.out.println();
            System.out.println(e.getMessage());
            throw new TimeoutException();
        }
    }

    public boolean waitForInvisibility(By targetElement){
        try{
            WebDriverWait wait = new WebDriverWait(driver, timeOut);
            wait.until(ExpectedConditions.invisibilityOfElementLocated(targetElement));
            return true;
        } catch (TimeoutException e) {
            System.out.println("Element is still visible: " + targetElement);
            System.out.println();
            System.out.println(e.getMessage());
            throw new TimeoutException();
        }
    }

    public WebElement findElement(By locator) {
        try {
            WebElement element = driver.findElement(locator);
            return element;
        } catch (NoSuchElementException e){
            Log.logError(this.getClass().getName(), "findElement",
                    "Element not found" + locator);
            throw new NoSuchElementException(e.getMessage());
        }
    }

    public List<WebElement> findElements(By locator){
        try {
            List<WebElement> element = driver.findElements(locator);
            return element;
        } catch (NoSuchElementException e){
            Log.logError(this.getClass().getName(), "findElements", "Element not found" + locator);
            throw new NoSuchElementException(e.getMessage());
        }
    }

    public void clickOnMatchingValue(List<WebElement> fetchedListElements, String valueToBeMatched){
        for(WebElement element : fetchedListElements) {
            if(element.getText().equalsIgnoreCase(valueToBeMatched)){
                element.click();
                return;
            }
        }
    }

    public void clickOnContainingValue(List<WebElement> fetchedListElements, String valueToBeContained){
        for(WebElement element : fetchedListElements) {
            if(element.getText().contains(valueToBeContained.toLowerCase())){
                element.click();
                return;
            }
        }
    }

    public static void runningShellCommand(String command) throws IOException, InterruptedException{
        Runtime run = Runtime.getRuntime();
        Process pr = run.exec(command);
        pr.waitFor();
        BufferedReader buf = new BufferedReader(new InputStreamReader(pr.getInputStream()));
        String line = "";
        while((line= buf.readLine()) != null){
            Log.info(line);
        }
    }

    public void acceptAlert(){
        try{
            Alert alert = driver.switchTo().alert();
            alert.accept();
        } catch(NoAlertPresentException e) {
            throw new NoAlertPresentException();
        }
    }

    public String getAlertText(){
        try{
            Alert alert = driver.switchTo().alert();
            String alerttext = alert.getText();
            return alerttext;
        } catch (NoAlertPresentException e){
            throw new NoAlertPresentException();
        }
    }

    public boolean isAlertPresent(){
        try{
            WebDriverWait wait = new WebDriverWait(driver, timeOut);
            wait.until(ExpectedConditions.alertIsPresent());
            driver.switchTo().alert();
            return true;
        } catch (NoAlertPresentException e) {
            throw new NoAlertPresentException();
        }
    }

    public void selectValuefromDropDownViaIndex(By selectLocator, int valueTobeSelectIndex){
        Select selectFromDropdown = new Select(findElement(selectLocator));
        selectFromDropdown.selectByIndex(valueTobeSelectIndex);
    }

    public String getCurrentURL(){
        return driver.getCurrentUrl();
    }

}
