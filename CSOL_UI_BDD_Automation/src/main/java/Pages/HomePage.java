package Pages;

import Init.CommonMethods;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import java.io.IOException;

public class HomePage extends CommonMethods {

    public HomePage(WebDriver driver) throws IOException {
        super(driver);
    }

    public By HamburgerMenu = By.cssSelector("i.cyicon-menu");
    public By Dashboard = By.xpath("//*[@href='/soar/dashboard']");
    public By Playbooks = By.xpath("//*[@href='/soar/playbook']");
    public By SourceEvents = By.xpath("//*[@href='/soar/event']");
    public By Runlogs = By.xpath("//*[@href='/soar/result']");
    public By CSOLAgentTasks = By.xpath("//*[@href='/soar/csol-lite-commands']");
    public By Lables = By.xpath("//*[@href='/soar/label']");
    public By ConfigureEvents = By.xpath("//*[@href='/soar/event-label']");
    public By Apps = By.xpath("//*[@href='/soar/app']");
    public By DataSync = By.xpath("//*[@href='/soar/data-sync']");


}
