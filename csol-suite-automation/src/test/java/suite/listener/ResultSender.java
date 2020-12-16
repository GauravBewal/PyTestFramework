package suite.listener;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mashape.unirest.http.Unirest;

import suite.model.TestStatus;

public class ResultSender {

	private static final ObjectMapper OM = new ObjectMapper();
	private static final String CONTENT_TYPE = "Content-Type";
	private static final String CONTENT_TYPE_VALUE = "application/json";
	private static final String ELASTICSEARCH_URL = "http://localhost:9200/app/suite";

	/**
	 * for converting in to json
	 * 
	 * @param testStatus
	 */
	public static void send(final TestStatus testStatus) {
		try {
			Unirest.post(ELASTICSEARCH_URL).header(CONTENT_TYPE, CONTENT_TYPE_VALUE)
					.body(OM.writeValueAsString(testStatus)).asJson();
			System.out.println();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}