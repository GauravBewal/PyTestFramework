package suite.testRunner;

import cucumber.api.CucumberOptions;
import cucumber.api.testng.AbstractTestNGCucumberTests;

/**
 * Test Runner for BDD Features
 * @author arth
 *
 */
@CucumberOptions(
//		plugin = "com.aventstack.extentreports.cucumber.adapter.ExtentCucumberAdapter:",
	    features = "src/test/resources/bdd.feature/",
        glue = "suite.stepDefination",
        monochrome = true,
     	plugin = { "json:target/cucumber.json", "pretty","html:target/cucumber-reports" },
        tags = {}
)
public class TestRunner extends AbstractTestNGCucumberTests {

}