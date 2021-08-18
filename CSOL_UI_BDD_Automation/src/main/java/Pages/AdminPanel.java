package Pages;

import Init.CommonMethods;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import java.io.IOException;

public class AdminPanel extends CommonMethods {

    public AdminPanel(WebDriver driver) throws IOException {
        super(driver);
    }

    public By AdminPanel = By.xpath("//*[@href='/soar/admin']");
    public By AdminPanelHeader = By.xpath("//h1[contains(text(),'Admin Panel')]");
    public By Configuration = By.xpath("//p[contains(text(),'Configuration')]");
    public By Authentication = By.xpath("//p[contains(text(),'Authentication')]");
    public By LicenseManagement= By.xpath("//p[contains(text(),'License Management')]");
    public By TenantManagement = By.xpath("//p[contains(text(),'Tenant Management')]");
    public By UserManagement = By.xpath("//p[contains(text(),'User Management')]");
    public By UserGroupManagement = By.xpath("//p[contains(text(),'User Group Management')]");
    public By CSOLAgent = By.xpath("//p[contains(text(),'CSOL Agent')]");
    public By OpenAPI = By.xpath("//p[contains(text(),'Open API')]");
    public By Webhooks = By.xpath("//p[contains(text(),'Webhooks')]");
    public By Syslogs = By.xpath("//p[contains(text(),'Syslogs')]");
    public By ConsoleStatus = By.xpath("//p[contains(text(),'Console Status')]");
    public By PlaybookTags = By.xpath("//p[contains(text(),'Playbook Tags')]");

}
