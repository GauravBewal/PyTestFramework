package suite.page;

import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import suite.base.PageBase;

/**
 * Page Object class for printer page webelements e.g textbox, title, btn,
 * 
 * @author arth
 *
 */
public class MobilePrinterPage extends PageBase {

	public MobilePrinterPage(WebDriver driver) {
		super(driver);
		PageFactory.initElements(driver, this);
	}

	public MobilePrinterPage getMobilePrinterPage(String pageURL) {
		NavigateTo(pageURL);
		return this;
	}

	@FindBy(css = ".janus-printer-series:nth-child(7) .janus-printer-title")
	private WebElement ql800Series;

	@FindBy(css = ".janus-printer-series:nth-child(7) .col-lg-4:nth-child(1) .janus-product-heading:nth-child(2)")
	private WebElement prodTitleOf800Series;

	@FindBy(css = "h1.janus-model-number")
	private WebElement prodNameOnPdp;

	@FindBy(css = ".janus-printer-series:nth-child(7) .col-lg-4:nth-child(1) .btn")
	private WebElement viewProdBtn800Series;

	@FindBy(css = "section.janus-printer-series:nth-child(10) .col-lg-4:nth-child(1) .btn")
	private WebElement viewProdBtn1100Series;

	@FindBy(css = "div.carousel-video>h4")
	private WebElement videosHeading;

	@FindBy(css = ".slick-current > .slide-content-container .video-title")
	private WebElement currentVideoTitleOfVideoFrame;

	@FindBy(css = ".slick-current > .thumbnail .video-title")
	private WebElement CurrentVideoTitleFromList;

	@FindBy(css = "span.glyphicon-chevron-right")
	private WebElement rightArrowIcon;

	@FindBy(css = "div.text-center.janus-btn-group>a")
	private WebElement communityForumTxt;

	@FindBy(css = "h2.category_title>a")
	private WebElement forumTitle;

	@FindBy(css = "button#btnAgree")
	private WebElement ackBtn;

	@FindBy(css = "a[title='View Series']")
	private WebElement viewSeriesBtn;

	@FindBy(css = "div.hero-text-container>h1")
	private WebElement qlLable;

	/**
	 * for getting the title of product of 800 series
	 * 
	 * @return title of product
	 */
	public String getTitleOfQL800() {
		scrollTo(ql800Series);
		return getText(prodTitleOf800Series);
	}

	/**
	 * for clicking on view product button
	 * 
	 * @return object of the current class
	 */
	public MobilePrinterPage clkOnViewProdbtnOf800() {
		clickingElementAction(viewProdBtn800Series);
		return this;
	}

	/**
	 * for waiting for complete page load
	 * 
	 * @param url
	 * @return object of the current class
	 */
	public MobilePrinterPage waitForPageLoad(String url) {
		closePreviousTab();
		waitForUrl(url);
		return this;
	}

	/**
	 * for getting text of product
	 * 
	 * @return product name
	 */
	public String getProdNameOnPdp() {
		return getText(prodNameOnPdp);
	}

	/**
	 * for getting the title of product of 1100 series
	 * 
	 * @return title of product
	 */
	public String getTitleOfQL1100() {
		scrollTo(ql800Series);
		return getText(prodTitleOf800Series);
	}

	/**
	 * for clicking on view product button
	 * 
	 * @return object of the current class
	 */
	public MobilePrinterPage clkOnViewProdbtnOf1100() {
		clickingElementAction(viewProdBtn1100Series);
		return this;
	}

	/**
	 * for scrolling to the Videos section
	 * 
	 * @return object of the current class
	 */
	public MobilePrinterPage scrollToVideos() {
		scrollTo(videosHeading);
		return this;
	}

	/**
	 * for getting title of video from video frame
	 * 
	 * @return title of video
	 */
	public String getTitleOfVideoFromVideoFrame() {
		return getText(currentVideoTitleOfVideoFrame);
	}

	/**
	 * for getting the title txt of highlighted video
	 * 
	 * @return video title
	 */
	public String getCurrentItemOfVideoList() {
		return getText(CurrentVideoTitleFromList);
	}

	/**
	 * for clicking on right arrow
	 * 
	 * @return object of the current class
	 */
	public MobilePrinterPage clkOnArrow() {
		clickOn(rightArrowIcon);
		return this;

	}

	/**
	 * for clicking on community forum text
	 * 
	 * @return object of the current class
	 */
	public MobilePrinterPage clkOnCommunityForumSection() {
		scrollTo(communityForumTxt);
		clickOn(communityForumTxt);
		return this;

	}

	/**
	 * for getting title from forum page
	 * 
	 * @return title of forum page
	 */
	public String getTitleOnForumPage() {
		closePreviousTab();
		return getText(forumTitle);
	}

	/**
	 * for clicking on Acknowledge button
	 * 
	 * @return object of the current class
	 */
	public MobilePrinterPage clkOnAckBtn() {
		waitForPageLoadComplete();
		try {
			clickOn(ackBtn);
		} catch (TimeoutException e) {
			clickOn(ackBtn);
			e.getMessage();
		}
		return this;
	}

	/**
	 * for clicking on view series button
	 * 
	 * @return object of the current class
	 */
	public MobilePrinterPage clkOnViewSeriesBtn() {
		scrollTo(viewSeriesBtn);
		clickOn(viewSeriesBtn);
		return this;
	}

	/**
	 * for getting Title of the current Page
	 * 
	 * @return page title
	 */
	public String getTitleQlLable() {
		closePreviousTab();
		return getPagetitle();
	}

}
