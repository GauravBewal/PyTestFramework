package suite.listener;

import java.time.LocalDateTime;

import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

import suite.model.TestStatus;

public class ExecutionListener implements ITestListener {

	private TestStatus testStatus;

	public void onTestStart(ITestResult iTestResult) {
		this.testStatus = new TestStatus();
	}

	/**
	 * Sending Status for Pass
	 */
	public void onTestSuccess(ITestResult iTestResult) {
		this.sendStatus(iTestResult, "PASS");
	}

	/**
	 * Sending Status for fail
	 */
	public void onTestFailure(ITestResult iTestResult) {
		this.sendStatus(iTestResult, "FAIL");
	}

	/**
	 * Sending Status for skipped
	 */
	public void onTestSkipped(ITestResult iTestResult) {
		this.sendStatus(iTestResult, "SKIPPED");
	}

	public void onTestFailedButWithinSuccessPercentage(ITestResult iTestResult) {
		// skip
	}

	/**
	 * for printing the test status
	 * 
	 * @param iTestResult
	 * @param status
	 */
	private void sendStatus(ITestResult iTestResult, String status) {
		this.testStatus.setTestClass(iTestResult.getTestClass().getName());
		this.testStatus.setDescription(iTestResult.getMethod().getDescription());
		this.testStatus.setStatus(status);
		this.testStatus.setExecutionDate(LocalDateTime.now().toString());
		/*
		 * System.out.println("*********************************");
		 * System.out.println(this.testStatus);
		 * System.out.println("*********************************");
		 */
	}

	@Override
	public void onFinish(ITestContext arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void onStart(ITestContext arg0) {
		// TODO Auto-generated method stub

	}

}