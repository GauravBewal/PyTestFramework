package suite.test;

import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.annotations.Test;

import suite.base.TestBase;
import suite.page.ChromeMobilePage;
import suite.page.LivemintMobilePage;
import suite.testdata.LivemintMobileTestData;

/**
 *  
 * @author arth
 *
 */
public class LivemintMobileTest extends TestBase {
private ChromeMobilePage cmp;
private LivemintMobilePage lmp;

	
	public void chromeDefault(WebDriver driver)   {
		
	    cmp = new ChromeMobilePage(driver) ; 
		
		cmp.clkAcceptBtn()
		.clkNextBtn()
		.clkNoThanksBtn()
		.clkChromeSearchBox()
		.enterChromeSearchBoxUrl(LivemintMobileTestData.MOBILE_HOME)
		.clkAllowBtn();

	}

	@Test(description = " Validating Search Result according to search Text ")
	public void testcase1()  {
				chromeDefault(getDriver());
				
				lmp = new LivemintMobilePage(getDriver());
				lmp.clkmenuBtn()
					  .clkSearchIcon()
					  .clkAddCrossBtn()
				      .enterSearchBar(LivemintMobileTestData.SEARCH_KEYWORD);
				  
		
				String actualFirstHeadline = lmp.getFirstHeadline(); 
				Assert.assertTrue(actualFirstHeadline.contains("Corona"));
				
				String actualSecondHeadline = lmp.getSecondHeadline(); 
				Assert.assertTrue(actualSecondHeadline.contains("Corona"));

	}

	@Test(description = "Validating that user can login with facebook",enabled=false)
	public void testcase2()  {
				chromeDefault(getDriver());
				lmp = new LivemintMobilePage(getDriver());
				lmp.clkUserProfileIcon()
			          .clkLoginFb()
			          .enterFbEmailId(LivemintMobileTestData.FB_EMAIL_ID)
					  .enterFbPass(LivemintMobileTestData.FB_PASSWORD)
					  .clkloginBtn()
					  .clkUserLoginProfileIcon();
				
				String actual = lmp.getUserName();
				
				Assert.assertEquals(actual, LivemintMobileTestData.EXPECTED_USER_NAME);
	}

	@Test(description = "Validating that user can see bookmarks in my read section",enabled=false)
	public void testcase3()  {
					chromeDefault(getDriver());
					lmp = new LivemintMobilePage(getDriver());
					lmp.clkUserProfileIcon()
						  .clkLoginFb()
	                      .enterFbEmailId(LivemintMobileTestData.FB_EMAIL_ID)
			              .enterFbPass(LivemintMobileTestData.FB_PASSWORD)
			              .clkloginBtn()
			              .clkSearchIcon()
					      .enterSearchBar(LivemintMobileTestData.SEARCH_BOOKMARK_KEYWORD)
					      .clkSearchBtn()
					      .clkBookmarks()
					      .clkMyReads();
					String actual = lmp.getMyReadHeadline();
					
					Assert.assertEquals(actual, LivemintMobileTestData.EXPECTED_BOOKMARK_HEADLINE); 
	}
}
