package suite.test;

import org.testng.Assert;
import org.testng.annotations.Test;

import suite.base.TestBase;
import suite.page.HomePage;
import suite.testdata.HomeTestData;

/**
 * This class contains the automation test cases for home
 * 
 * @author arth
 *
 */
public class HomeTest extends TestBase {

	private HomePage ht;

	/**
	 * create page url
	 * 
	 * @return home page page url
	 */
	private String getPageURL() {
		return getEnv().concat(HomeTestData.LOGIN_PAGE);
	}

	@Test(description = "For verifying if login icon redirect to login page.", groups = {"demo", "home" })

	public void home_1() {
			
		ht = new HomePage(getDriver());
		
		String actual = ht.getHomePage(getPageURL())
								   .clkLoginIcon()
								   .getLoginPageTitle();
		
		Assert.assertEquals(actual, HomeTestData.LOGIN_PAGE_TITLE);
		
	}
	
	@Test(description = "For verifying functionality of Contact us Tab.", groups = {"demo", "home" })

	public void home_2() {
			
		ht = new HomePage(getDriver());
		
		
		  String actual = ht.getHomePage(getPageURL()) 
				  					 .clkCommunityForumTab()
				  					 .getcommunityForumTitleTxt();
		  
		  Assert.assertEquals(actual, HomeTestData.POP_UP_TEXT);
		 
		
	}
	
	/*Test Case 3,4,5,6 are included in home_3 for checking link.*/
	
	@Test(description = "For Checking Links of Get Started with Brothers Section", groups = {"demo", "home" })

	public void home_3() {
			
		ht = new HomePage(getDriver());
		
		boolean actual = ht.getHomePage(getPageURL())
								        .getGetStartedLinks();
		
		Assert.assertTrue(actual);
		
	}
	
	@Test(description = "For verifying Membership Header in Benifits of becoming Member", groups = {"demo", "home" })

	public void home_7() {
			
		ht = new HomePage(getDriver());
		
		String actual = ht.getHomePage(getPageURL())
								   .getSapphireTxt();
		
		Assert.assertEquals(actual, HomeTestData.SAPPHIRE_TITLE);
		
	}
	
	@Test(description = "For Verifying the link in Latest news Release ", groups = {"demo", "home" })

	public void home_8() {
			
		ht = new HomePage(getDriver());
		
		Boolean actual = ht.getHomePage(getPageURL())
								      .getLatestNewsLinks();
		
		Assert.assertTrue(actual);
		
	}
	
	@Test(description = "For verifying the functionlity of the sign up Button ", groups = {"demo", "home" })

	public void home_10() {
			
		ht = new HomePage(getDriver());
		
		String actual = ht.getHomePage(getPageURL())
								   .clkSignUpBtn()
								   .getSignUpTitle();
		
		Assert.assertEquals(actual, HomeTestData.SIGN_UP_PAGE_TITLE);
		
	}
	
	@Test(description = "For checking the fuctionality of member center when logged in  ", groups = {"demo", "home" })

	public void home_11() {
			
		ht = new HomePage(getDriver());
		
		String actual = ht.getHomePage(getPageURL())
								   .clkUserProfileIcon()
								   .enterUname(HomeTestData.VALID_UNAME)
								   .enterPass(HomeTestData.VALID_PASS)
								   .clkLoginBtn()
								   .clkMemberCenterLink()
								   .getMemberCenterTitle();
		
		Assert.assertEquals(actual, HomeTestData.MEMBER_CENTER_PAGE_TITLE);
		
	}
	
	/*Test Case 12,13,14 are included in home_12 for checking link.*/
	
	@Test(description = "For checking the  links redirection in getting started section ", groups = {"demo", "home" })

	public void home_12() {
			
		ht = new HomePage(getDriver());
		
		Boolean actual = ht.getHomePage(getPageURL())
								      .getImageLinks();
		
		Assert.assertTrue(actual);
		
	}
	
	@Test(description = "For checking functionality of case study button.", groups = { "demo","home" })

	public void home_15() {
			
		ht = new HomePage(getDriver());
		
		boolean actual = ht.getHomePage(getPageURL())
								        .clkCaseStudyBtn();
								  
		Assert.assertTrue(actual);
		
	}
	
	/*Test Case 16,17,18 are included in home_16 for checking link.*/
	
	@Test(description = "For checking the Image links redirection in getting started section ", groups = {"demo", "home" })

	public void home_16() {
			
		ht = new HomePage(getDriver());
		
		Boolean actual = ht.getHomePage(getPageURL())
								      .getGetStartedImageLinks();
		
		Assert.assertTrue(actual);
		
	}
	
	}
