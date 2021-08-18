package Init;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import io.cucumber.testng.AbstractTestNGCucumberTests;
import org.junit.runner.RunWith;
import org.testng.annotations.BeforeSuite;

@RunWith(Cucumber.class)
@CucumberOptions (
        monochrome = true,
        features = "src/main/java/Features",
        glue = {"StepDefs"},
        plugin = {"pretty", "json:target/cucumber-html-report","html:target/test-report.html"},
        tags = "@smoke"
        )

public class TestRunner extends AbstractTestNGCucumberTests {


}
