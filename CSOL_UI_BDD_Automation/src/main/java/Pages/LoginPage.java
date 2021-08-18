package Pages;

import Init.CommonMethods;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import java.io.IOException;

public class LoginPage extends CommonMethods {

    public LoginPage(WebDriver driver) throws IOException {
        super(driver);
    }

    public By username = By.xpath("//input[@type='text']");
    public By password = By.xpath("//input[@type='password']");
    public By loginButton = By.xpath("//button[@type='button']");

}
