package StepDefs;

import Init.CreateSession;
import Pages.LoginPage;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.WebDriver;

import java.io.IOException;

public class LoginPageTest {

    LoginPage loginPage;
    WebDriver driver;

    public LoginPageTest() throws IOException {
        CreateSession.createDriver();
        driver = CreateSession.getWebDriver();
        loginPage = new LoginPage(driver);
    }

    @Given("^the user is on CSOL Login page$")
    public void user_is_on_CSOL_Login_page() throws Throwable {
        loginPage.get(System.getProperty("url"));
    }

    @When("^the user enters UserName and Password$")
    public void the_user_enters_username_and_password() throws Throwable {
        loginPage.findElement(loginPage.username).sendKeys(System.getProperty("emailId"));
        loginPage.findElement(loginPage.password).sendKeys(System.getProperty("Password"));
    }

    @And("^user clicks on login button$")
    public void user_click_on_login_button(){
        loginPage.findElement(loginPage.loginButton).click();
    }

    @Then("^User is on dashboard page$")
    public void user_should_be_validated_redirected(){
       boolean validate = loginPage.getCurrentURL().contains("dashboard");
       System.out.println(validate);
    }

}
