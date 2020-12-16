package suite.model;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Model Class for serialsing the data for elastic search
 * @author arth
 *
 */
public class TestStatus {

	@JsonProperty("testClass")
	private String testClass;

	@JsonProperty("description")
	private String description;

	@JsonProperty("status")
	private String status;

	@JsonProperty("executionTime")
	private String executionTime;

	/**
	 * for setting description
	 * 
	 * @param description
	 */
	public void setDescription(String description) {
		this.description = description;
	}

	/**
	 * for setting execution date
	 * 
	 * @param executionTime
	 */
	public void setExecutionDate(String executionTime) {
		this.executionTime = executionTime;
	}

	/**
	 * for setting status
	 * 
	 * @param status
	 */
	public void setStatus(String status) {
		this.status = status;
	}

	/**
	 * for setting test class
	 * 
	 * @param testClass
	 */
	public void setTestClass(String testClass) {
		this.testClass = testClass;
	}

}
