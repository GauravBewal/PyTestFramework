package suite.page;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import suite.base.PageBase;

/**
 * Page Object class for Home page 
 * webelements e.g textbox, title, btn, 
 * 
 * @author arth
 *
 */
public class HomePage extends PageBase {

	private WebDriver driver;

	@FindBy(css = ".br-user")
	private WebElement loginIcon;

	@FindBy(css = ".janus-ban-heading.white-color")
	private WebElement loginPageTitleTxt;

	@FindBy(css = "li:nth-child(6) > a.forum-link")
	private WebElement communityForumTab;

	@FindBy(css = ".resultTopFilter.n.selected")
	private WebElement communityForumTitleTxt;

	@FindBy(css = ".janus-member-accordian:nth-child(2) .janus-accordian-heading")
	private WebElement sapphireTxt;

	@FindBy(css = "h2.janus-sec-title-1")
	private WebElement gettingStartedTitle;

	@FindBy(css = ".service-text > a[href]") // .service-text > a[href]
	private List<WebElement> gettingStartedLinks;

	@FindBy(css = "h2.janus-news-heading")
	private WebElement latestNewsTitle;

	@FindBy(css = ".janus-news-col-2 > a[href]")
	private List<WebElement> latestNewsLinks;

	@FindBy(css = ".janus-ragister-wrapp > a")
	private WebElement signUpBtn;

	@FindBy(css = ".container > h2")
	private WebElement signUpTitleTxt;

	@FindBy(css = ".br-user")
	private WebElement userProfileIcon;

	@FindBy(id = "LoginEmail")
	private WebElement unameTxt;

	@FindBy(id = "LoginPassword")
	private WebElement passTxt;

	@FindBy(id = "loginbtn")
	private WebElement loginBtn;

	@FindBy(css = ".janus-service-box:nth-child(5) h4.service-text > a:nth-child(1)")
	private WebElement memberCenterLink;

	@FindBy(css = ".janus-ban-heading.white-color")
	private WebElement memberCenterTitle;

	@FindBy(css = ".janus-program-text")
	private List<WebElement> getStartedLinks;

	@FindBy(css = "h2.janus-insp-title1.text-uppercase.mb30")
	private WebElement inspiratiobTitle;

	@FindBy(css = ".slick-slide.slick-current.slick-active > a[href]")
	private List<WebElement> caseStudyBtn;

	@FindBy(css = ".janus-ban-heading.white-color")
	private WebElement caseStudyTitle;

	@FindBy(css = ".janus-program-img > a > img[src]")
	private List<WebElement> getStartedImageLinks;

	public HomePage(WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	/**
	 * for getting page url of home page
	 * 
	 * @param pageURL
	 * @return page url of the home page
	 */
	public HomePage getHomePage(String pageURL) {
		NavigateTo(pageURL);
		return this;
	}

	/**
	 * for clicking on login icon
	 * 
	 * @return object of current class
	 */
	public HomePage clkLoginIcon() {
		clickOn(loginIcon);
		return this;
	}

	/**
	 * for getting title of login page
	 * 
	 * @return titlte of login page
	 */
	public String getLoginPageTitle() {
		return getText(loginPageTitleTxt);
	}

	/**
	 * for clicking on community forum tab
	 * 
	 * @return object of current class
	 */
	public HomePage clkCommunityForumTab() {
		clickOn(communityForumTab);
		return this;
	}

	/**
	 * for getting page title of community forum page
	 * 
	 * @return title of community forum page
	 */
	public String getcommunityForumTitleTxt() {
		Set<String> handlesSet = driver.getWindowHandles();
		List<String> handlesList = new ArrayList<String>(handlesSet);
		driver.switchTo().window(handlesList.get(0));
		driver.close();
		driver.switchTo().window(handlesList.get(1));
		return getText(communityForumTitleTxt);
	}

	/**
	 * for getting sapphire title text
	 * 
	 * @return sapphire text
	 */
	public String getSapphireTxt() {
		scrollTo(sapphireTxt);
		return getText(sapphireTxt);
	}

	/**
	 * for checking broken link in getting started section
	 * 
	 * @return return true if no broken link found , false if broken link present
	 */
	public Boolean getGetStartedLinks() {
		return areLinksBroken(gettingStartedLinks);
	}

	/**
	 * for checking broken link in Latest News section
	 * 
	 * @return if no broken link found , false if broken link present
	 */
	public Boolean getLatestNewsLinks() {
		scrollTo(getWebElement(latestNewsTitle));
		return areLinksBroken(latestNewsLinks);
	}

	/**
	 * for clicking on signup button
	 * 
	 * @return object of current class
	 */
	public HomePage clkSignUpBtn() {
		clickOn(signUpBtn);
		return this;
	}

	/**
	 * for getting title signup page
	 * 
	 * @return signup page title
	 */
	public String getSignUpTitle() {
		return getText(signUpTitleTxt);
	}

	/**
	 * for clicking on user profile icon from home page
	 * 
	 * @return object of current class
	 */
	public HomePage clkUserProfileIcon() {
		clickOn(userProfileIcon);
		return this;
	}

	/**
	 * for entering username on login page
	 * 
	 * @param uname
	 * @return object of current class
	 */
	public HomePage enterUname(String uname) {
		setText(unameTxt, uname);
		return this;
	}

	/**
	 * for entering password on login page
	 * 
	 * @param pass
	 * @return object of current class
	 */
	public HomePage enterPass(String pass) {
		setText(passTxt, pass);
		return this;
	}

	/**
	 * for clicking on login button
	 * 
	 * @return object of current class
	 */
	public HomePage clkLoginBtn() {
		clickOn(loginBtn);
		return this;
	}

	/**
	 * for clicking on member center link
	 * 
	 * @return object of current class
	 */
	public HomePage clkMemberCenterLink() {
		clickOn(memberCenterLink);
		return this;
	}

	/**
	 * for getting member center title
	 * 
	 * @return member center title
	 */
	public String getMemberCenterTitle() {
		return getText(memberCenterTitle);
	}

	/**
	 * for checking Image broken link in getting started section
	 * 
	 * @return return true if no broken link found , false if broken link present
	 */
	public Boolean getImageLinks() {
		scrollTo(getWebElement(gettingStartedTitle));
		return areLinksBroken(getStartedLinks);
	}

	/**
	 * for clicking on case study button
	 * 
	 * @return object of current class
	 */
	public Boolean clkCaseStudyBtn() {
		scrollTo(inspiratiobTitle);
		return areLinksBroken(caseStudyBtn);
	}

	/**
	 * for checking the if the image link is broken in getting started section
	 * 
	 * @return true if no broken image found , false if broken link present
	 */
	public Boolean getGetStartedImageLinks() {
		scrollTo(getWebElement(gettingStartedTitle));
		return areImagesBroken(getStartedImageLinks);
	}
}
