package suite.util;

import org.apache.http.HttpStatus;

import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.specification.ResponseSpecification;

public class ResponseSpecs {

	/**
	 * @return response specification for get request 
	 * 
	 * 1. Checks whether the request returns 200 status code or not.
	 * 2. Checks whether the returned response is JSON or not.
	 */
	public static ResponseSpecification expectedGetResponse() {
		return new ResponseSpecBuilder()
				.expectStatusCode(HttpStatus.SC_OK)
				.expectContentType(ContentType.JSON)
				.build();
				
	}
	
}
