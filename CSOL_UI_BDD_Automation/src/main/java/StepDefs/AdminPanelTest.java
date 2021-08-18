package StepDefs;

import Init.CreateSession;
import Pages.AdminPanel;
import Pages.HomePage;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.WebDriver;

import java.io.IOException;

public class AdminPanelTest {
        AdminPanel adminPanel;
        WebDriver driver;
        HomePage homePage;

        public AdminPanelTest() throws IOException {
            driver = CreateSession.getWebDriver();
            adminPanel = new AdminPanel(driver);
            homePage = new HomePage(driver);
        }

        @Given("^the user is in CSOL Dashboard$")
        public void User_is_in_CSOL_Dashboard(){
            adminPanel.findElement(homePage.HamburgerMenu).click();
            adminPanel.findElement(homePage.Dashboard).click();
        }

        @When("^the user clicks on the Admin panel icon on the bottom left$")
        public void user_on_admin_panel_page(){
            adminPanel.findElement(adminPanel.AdminPanel).click();
        }

        @Then("^user should be redirected to CSOL Admin panel - listing page$")
        public void user_redirect_to_CSol_admin(){
            String header = adminPanel.findElement(adminPanel.AdminPanelHeader).getText();
            System.out.println(header);
        }


        @Given("^the user is in Admin panel - listing page$")
        public void user_is_in_Admin_Panel(){

        }

        @When("^the user clicks on any of the menu listing$")
        public void user_clicks_on_any_of_menu_listing(){

        }
}

