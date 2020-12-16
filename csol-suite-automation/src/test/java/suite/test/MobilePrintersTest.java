package suite.test;

import org.testng.Assert;
import org.testng.annotations.Test;
import suite.base.TestBase;
import suite.page.MobilePrinterPage;
import suite.testdata.MobilePrinterTestData;
/**
 * this contains the automation test cases for Mobile and printers 
 * @author arth
 *
 */

public class MobilePrintersTest extends TestBase {

	private MobilePrinterPage mp;

	/**
	 * create page url
	 * 
	 * @return mobile printer page url
	 */
	private String getPageURL() {
		return getEnv().concat(MobilePrinterTestData.MOBILE_PRINTERS_PAGE);
	}

	@Test(description = "Verifying the content in QL - 800 SERIES PRINTER", groups = { "done","mob_printer" })

	public void mobile_1() {

		mp = new MobilePrinterPage(getDriver());

		String actual = mp.getMobilePrinterPage(getPageURL())
				          .getTitleOfQL800();

		Assert.assertEquals(actual, MobilePrinterTestData.EXPECTED_PRODUCT_TITLE_800_SERIES);
	}

	@Test(description = "Verifying the functionality of view product button in QL - 800 SERIES PRINTER", groups = {"done","mob_printer" })

	public void mobile_2() {

		mp = new MobilePrinterPage(getDriver());

		String actual = mp.getMobilePrinterPage(getPageURL())
		                  .clkOnViewProdbtnOf800()
				          .waitForPageLoad(MobilePrinterTestData.PDP_PAGE_URL_FOR_QL800)
				          .getProdNameOnPdp();

		Assert.assertEquals(actual, MobilePrinterTestData.EXPECTED_PRODUCT_PDP_800_SERIES);

	}

	@Test(description = "Verifying the content in QL - 1100 SERIES PRINTER", groups = { "done","mob_printer" })

	public void mobile_3() {

		mp = new MobilePrinterPage(getDriver());

		String actual = mp.getMobilePrinterPage(getPageURL())
				          .getTitleOfQL1100();

		Assert.assertEquals(actual, MobilePrinterTestData.EXPECTED_PRODUCT_TITLE_800_SERIES);

	}

	@Test(description = "Verifying the functionality of view product button in QL - 1100 SERIES PRINTER", groups = {"done","mob_printer" })

	public void mobile_4() {

		mp = new MobilePrinterPage(getDriver());
		
		String actual = mp.getMobilePrinterPage(getPageURL())
				          .clkOnViewProdbtnOf1100()
				          .waitForPageLoad(MobilePrinterTestData.PDP_PAGE_URL_FOR_QL1100)
				          .getProdNameOnPdp();
	 
		Assert.assertEquals(actual, MobilePrinterTestData.EXPECTED_PRODUCT_PDP_1100_SERIES);

	}

	@Test(description = "Verifying the content in Tutorial video section ", groups = { "done","mob_printer" })

	public void mobile_5() {

		mp = new MobilePrinterPage(getDriver());
		
		String actual = mp.getMobilePrinterPage(getPageURL())
				          .scrollToVideos()
				          .getCurrentItemOfVideoList();
		
		Assert.assertEquals(actual, mp.getTitleOfVideoFromVideoFrame());

	}

	@Test(description = "Verifying the functionality of > symbol in Tutorial section", groups = { "done","mob_printer" })

	public void mobile_6() {

		mp = new MobilePrinterPage(getDriver());
		
		String actual = mp.getMobilePrinterPage(getPageURL())
				          .scrollToVideos()
				          .clkOnArrow()
				          .getCurrentItemOfVideoList();
		
		Assert.assertEquals(actual, mp.getTitleOfVideoFromVideoFrame());
	}

	@Test(description = "Verifying the link in Recent Discussion section", groups = { "done","mob_printer" })

	public void mobile_7() {

		mp = new MobilePrinterPage(getDriver());
		
		String actual = mp.getMobilePrinterPage(getPageURL())
				          .clkOnCommunityForumSection()
				          .clkOnAckBtn()
				          .getTitleOnForumPage();
	 
		Assert.assertEquals(actual, MobilePrinterTestData.EXPECTED_TITLE_ON_FORUM_PAGE);

	}

	@Test(description = "Verifying the functionality of view series button in Introduction the new ql series printers", groups = {"done","mob_printer" })

	public void mobile_8() {

		mp = new MobilePrinterPage(getDriver());
		
		String actual = mp.getMobilePrinterPage(getPageURL())
				          .clkOnViewSeriesBtn()
				          .getTitleQlLable();
		 
		Assert.assertEquals(actual, MobilePrinterTestData.EXPECTED_TITLE_ON_VIEW_SERIES_PAGE);

	}
}
