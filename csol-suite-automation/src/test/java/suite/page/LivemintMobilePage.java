package suite.page;

import java.util.List;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import suite.base.PageBase;

/**
 * Page Object Class for Login Page
 * 
 * @author arth
 *
 */
public class LivemintMobilePage extends PageBase {

	public LivemintMobilePage(WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	public LivemintMobilePage getLivemintPage(String pageURL) {
		NavigateTo(pageURL);
		return this;
	}

	@FindBy(xpath = "//android.view.View[@resource-id='header']/android.view.View/android.view.View/android.view.View[1]")
	private WebElement menuBtn;

	@FindBy(xpath = "//android.view.View[@resource-id='fixedNav_home']")
	private WebElement searchIcon;

	@FindBy(xpath = "//android.view.View[@resource-id='dismiss-button']")
	private WebElement addCrossBtn;

	@FindBy(xpath = "//android.widget.EditText[@resource-id='searchField']")
	private WebElement searchTxt;

	@FindBy(xpath = "//android.view.View[starts-with(@resource-id,'listheadline_')]")
	private List<WebElement> HeadlineTitleList;

	@FindBy(xpath = "//android.view.View[@text='Sign in' and @index='0']")
	private WebElement userProfileIcon;

	@FindBy(xpath = "//android.widget.Image[@resource-id='fbmBtn']")
	private WebElement loginwFbBtn;

	@FindBy(xpath = "//android.widget.EditText[@resource-id='m_login_email']")
	private WebElement fbEmailIdTxt;

	@FindBy(xpath = "//android.widget.EditText[@resource-id='m_login_password']")
	private WebElement FbPassTxt;

	@FindBy(xpath = "//android.view.View[@resource-id='u_0_4']")
	private WebElement loginFbBtn;

	@FindBy(xpath = "//android.view.View[@resource-id='header']/android.view.View/android.view.View/android.view.View[3]")
	private WebElement userLoginProfileIcon;

	@FindBy(xpath = "//android.view.View[@resource-id='uName']/android.view.View[1]")
	private WebElement userName;

	@FindBy(xpath = "//android.view.View[starts-with(@resource-id,'bookmark_')]")
	private List<WebElement> bookmarkBtn;

	@FindBy(xpath = "//android.view.View[@text='MY READS' and @index='3']")
	private WebElement myReadsBtn;

	@FindBy(xpath = "//android.view.View[starts-with(@resource-id,'bm_')]/android.view.View/android.view.View/android.view.View[3]/android.view.View")
	private List<WebElement> myReadHeadline;

	/**
	 * for clicking on menu btn
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkmenuBtn() {
		clickOn(menuBtn);
		return this;
	}

	/**
	 * for clicking on element in search icon
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkSearchIcon() {
		clickOn(searchIcon);
		return this;
	}

	/**
	 * for clicking on add cross btn
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkAddCrossBtn() {
		try {
			clickOn(addCrossBtn);
		} catch (org.openqa.selenium.TimeoutException e) {
			e.printStackTrace();
		}
		return this;
	}

	/**
	 * for searching keyword in search bar
	 * 
	 * @param searchKeywordTxt
	 * @return object of current class
	 */
	public LivemintMobilePage enterSearchBar(String searchKeywordTxt) {
		setText(searchTxt, searchKeywordTxt + "\\n");
		return this;

	}

	/**
	 * for clicking on element in search botton
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkSearchBtn() {
		pressEnterBtn(searchTxt);
		return this;
	}

	/**
	 * for getting first headline
	 * 
	 * @return first headline
	 */
	public String getFirstHeadline() {
		return getText(HeadlineTitleList.get(0));
	}

	/**
	 * for getting second headline
	 * 
	 * @return second headline
	 */
	public String getSecondHeadline() {
		return getText(HeadlineTitleList.get(1));
	}

	/**
	 * for clicking on user profile icon
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkUserProfileIcon() {
		clickOn(userProfileIcon);
		return this;
	}

	/**
	 * for clicking login with facebook button
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkLoginFb() {
		clickOn(loginwFbBtn);
		return this;
	}

	/**
	 * for entering facebook email id
	 * 
	 * @param fbEmailId
	 * @return object of current class
	 */
	public LivemintMobilePage enterFbEmailId(String fbEmailId) {
		setText(fbEmailIdTxt, fbEmailId);
		return this;

	}

	/**
	 * for entering facebook password
	 * 
	 * @param fbPasswordId
	 * @return object of current class
	 */
	public LivemintMobilePage enterFbPass(String fbPasswordId) {
		setText(FbPassTxt, fbPasswordId);
		return this;

	}

	/**
	 * for clicking on login button
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkloginBtn() {
		clickOn(loginFbBtn);
		return this;
	}

	/**
	 * for clicking on user profile login button
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkUserLoginProfileIcon() {
		clickOn(userLoginProfileIcon);
		return this;
	}

	/**
	 * for getting first username on home page
	 * 
	 * @return username
	 */
	public String getUserName() {
		return getText(userName);
	}

	/**
	 * for clicking on bookmark btn
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkBookmarks() {
		clickOn(bookmarkBtn.get(0));
		return this;
	}

	/**
	 * for clicking on my reads button
	 * 
	 * @return object of current class
	 */
	public LivemintMobilePage clkMyReads() {
		clickOn(myReadsBtn);
		return this;
	}

	/**
	 * for getting first username on home page
	 * 
	 * @return my read headline title
	 */
	public String getMyReadHeadline() {
		return getText(myReadHeadline.get(0));
	}
}