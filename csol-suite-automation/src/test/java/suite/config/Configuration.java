package suite.config;

/**
 * This Class contains the Test Configuration Parameters
 *
 * @author Arth Kumar
 */

import org.aeonbits.owner.Config;
import org.aeonbits.owner.Config.Sources;

@Sources({
//		"file:src/test/resources/environment/${env}.properties"
		"file:src/test/resources/TestConfig.properties" })
public interface Configuration extends Config {

	@Key("env")
	String getEnv();

	@Key("browser")
	String getBrowser();
}
