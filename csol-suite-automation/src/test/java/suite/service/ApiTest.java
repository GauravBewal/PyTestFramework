package suite.service;

import static io.restassured.RestAssured.baseURI;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.emptyOrNullString;
import static org.hamcrest.Matchers.is;

import suite.constants.Endpoint;
import org.apache.http.HttpStatus;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import suite.util.ResponseSpecs;

/**
 * Api Tests for https://api.publicapis.org/
 * 
 * @author arth
 *
 */
public class ApiTest {

	@BeforeClass
	public void setUp() {

		baseURI = Endpoint.BASE_URL;
	}

	@Test(description = "Verify that there are 642 entries are returned when user makes requests for entries.")
	public void tcID01() {

		given().when().get(Endpoint.ENTRIES).then().assertThat().spec(ResponseSpecs.expectedGetResponse()).and()
				.body("count", is(642));
	}

	@Test(description = "Verify that empty or null string is returned when user makes a requests for a random entry with auth type as null.")
	public void tcID02() {

		given().queryParam("auth", "null").when().get(Endpoint.RANDOM).then().assertThat().body("auth",
				emptyOrNullString());
	}

	@Test(description = "Verify that Books category is present in the returned response when the user makes requests for all categories.")
	public void tcID03() {

		given().when().get(Endpoint.CATEGORIES).then().assertThat().body(containsString("Books"));
	}

	@Test(description = "Verify that the service returns okay response when user makes a health request.")
	public void tcID04() {

		given().when().get(Endpoint.HEALTH).then().assertThat().statusCode(HttpStatus.SC_OK);
	}

	@Test(description = "Verify that only single entry is returned when user makes a requests for a random entry.")
	public void tcID05() {

		given().when().get(Endpoint.RANDOM).then().assertThat().spec(ResponseSpecs.expectedGetResponse()).and()
				.body("count", is(1));
	}

	@Test(description = "Verify that all 45 categories are returned when the user makes requests for categories.")
	public void tcID06() {

		given().when().get(Endpoint.CATEGORIES).then().assertThat().body(containsString("Books")).and()
				.statusCode(HttpStatus.SC_OK);
	}

	@Test(description = "Verify that there are 548 entries are returned when user makes requests for entries with https as true.")
	public void tcID07() {

		given().queryParam("https", "true").when().get(Endpoint.ENTRIES).then().assertThat().body("entries.size()",
				is(548));
	}

	@Test(description = "Verify that true is returned when when user makes a health request.")
	public void tcID08() {

		String actual = given().when().get(Endpoint.HEALTH).then().assertThat().extract().body().asString();

		Assert.assertTrue(actual.contains("true"));
	}

}
