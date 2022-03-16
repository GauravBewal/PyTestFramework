import pytest

from pageObjects.Navigation import Navigation
from pageObjects.OpenApi import OpenApi
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestOpenApi(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_1_Verify_Admin_Open_API_Redirection(self):
        """
            Verify redirection of Open APIs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Cyware Agent")
        nav.click_admin_menu()
        log.info("Click on Open APIs tab from Admin Page")
        openapi.click_open_api_tab()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() == 'Open APIs | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Click_New_Open_Api_btn(self):
        """
        Verify whether user is able on click on new openapi button
        Validation: Based on the create slider title
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on add openapi button")
        openapi.click_new_open_api()
        log.info("Read the slider title")
        slider_title = openapi.get_slider_title()
        log.info("Click on close slider button")
        openapi.click_slider_close()
        assert slider_title == 'New Open API'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on inactive tab")
        openapi.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = openapi.get_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 1. On the basis of tab color
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on All tab")
        openapi.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = openapi.get_all_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    def test_05_Create_new_openapi(self):
        """
        Verify user is able to create a new openapi
        Validation-1: Based on the successful message
                   2: Based on visibility in listing
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        action = Action(self.driver)
        log.info("Click on the open api button")
        openapi.click_new_open_api()
        log.info("Enter the openapi name")
        global openapi_name
        openapi_name = "OpenAPI " + action.get_current_time()
        openapi.put_open_api_title(openapi_name)
        log.info("click on the openapi expiration field")
        openapi.click_on_expiration_field()
        log.info("Select today as the expiry date")
        openapi.select_on_today_in_calendar()
        log.info("click on the bot user field")
        openapi.click_on_bot_user_field()
        log.info("Select the first user in the list as an bot user")
        openapi.click_on_first_bot_user()
        log.info("close the bot user field")
        openapi.click_on_bot_user_field()
        log.info("Click on create button")
        openapi.click_on_create_btn()
        log.info("Read the successful message")
        successful_msg = openapi.get_successfully_created_msg()
        openapi.close_tooltip()
        assert successful_msg in "API configuration created successfully."

    @pytest.mark.regression
    def test_06_Verify_api_url_visibility_and_copy_functionality(self):
        """
        Verify whether user is able to see the api url and copy it
        Validation-1: Based on the api url visibility
                   2: Based on the copied check button visibility
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("check visibility of api url")
        visibility = openapi.visibility_of_api_url()
        log.info("Read api url")
        api_url = openapi.get_api_url()
        assert visibility is True and "/soarapi/openapi/" in api_url
        log.info("Click on api url copy button")
        openapi.click_apiurl_copy_btn()
        assert openapi.visibility_of_copied_check_btn() is True

    @pytest.mark.regression
    def test_07_Verify_secret_key_visibility_and_copy_functionality(self):
        """
            Verify whether user is able to see the secret key and copy it
            Validation-1: Based on the secret key visibility
                       2: Based on the copied check button visibility
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on the eye icon to see the secret key")
        openapi.click_secret_key_show_btn()
        log.info("Check visibility of secret key")
        secret_key_hidden = openapi.visibility_of_secret_key()
        assert secret_key_hidden is False
        log.info("Click on hide button")
        openapi.click_on_hide_btn()
        log.info("Click on secret key copy button")
        openapi.click_secret_key_copy_btn()
        assert openapi.visibility_of_copied_check_btn() is True

    @pytest.mark.regression
    def test_08_Verify_access_id_visibility_and_copy_functionality(self):
        """
        Verify whether user is able to see the access id and copy it
        Validation-1: Based on the access id visibility
                   2: Based on the copied check button visibility
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Click on the eye icon to see the secret key")
        openapi.click_access_id_show_btn()
        log.info("Check visibility of secret key")
        secret_key_hidden = openapi.visibility_of_access_id()
        assert secret_key_hidden is False
        log.info("Click on hide button")
        openapi.click_on_hide_btn()
        log.info("Click on access id copy button")
        openapi.click_access_id_copy_btn()
        assert openapi.visibility_of_copied_check_btn() is True

    @pytest.mark.regression
    def test_09_Check_visibility_of_download_keys_btn(self):
        """
        Verify whether user is able to see the download keys button
        Validation-1 : Based on the button visibility
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Check visibility of download button")
        visibility = openapi.visibility_of_download_keys_btn()
        log.info("Click on close slider button")
        openapi.click_slider_close()
        assert visibility is True

    @pytest.mark.regression
    def test_10_Search_created_openapi(self):
        """
        Verify user is able to search the created openapi
         Validation-1: Based on the search result
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        log.info("Enter openapi name to search")
        openapi.put_string_in_search_bar(openapi_name)
        log.info("Click Enter")
        openapi.click_enter_for_search()
        openapi.visibility_of_first_openapi()
        read_top_search_result = openapi.get_top_1_openapi_name()
        openapi.clear_search()
        log.info("Validating search results")
        assert openapi_name in read_top_search_result

    @pytest.mark.regression
    def test_11_Update_created_openapi(self):
        """
        Verify whether user is able to update the created openapi
        Validation-1: Based on the updated openapi title visibility
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        action = Action(self.driver)
        log.info("Click on the first openapi")
        openapi.click_on_first_openapi()
        log.info("Remove the current openapi title")
        openapi.clear_open_api_title_field()
        log.info("Update the openapi name")
        global updated_openapi_name
        updated_openapi_name = "OpenAPI " + action.get_current_time()
        openapi.put_open_api_title(updated_openapi_name)
        log.info("Click on update button")
        openapi.click_on_update_btn()
        log.info("Click on close tooltip")
        openapi.close_tooltip()
        log.info("check visibility of first openapi")
        openapi.visibility_of_first_openapi()
        top_openapi_name = openapi.get_top_1_openapi_name()
        log.info("Validating the new label name is updated or not ")
        assert top_openapi_name == updated_openapi_name

    @pytest.mark.regression
    def test_12_Deactivate_openapi(self):
        """
        Verify user is able to deactivate the openapi
        Validation-1: Based on the openapi getting listing in inactive tab
        """
        log = self.getlogger()
        openapi = OpenApi(self.driver)
        action = Action(self.driver)
        log.info("Click on the first openapi")
        openapi.click_on_first_openapi()
        log.info("Click on inacive toggle")
        openapi.click_inactive_toggle()
        log.info("Click on update button")
        openapi.click_on_update_btn()
        log.info("Click on close tooltip")
        openapi.close_tooltip()
        log.info("Click on inactive tab")
        openapi.click_inactive_tab()
        log.info("check visibility of first openapi")
        openapi.visibility_of_first_openapi()
        top_openapi_name = openapi.get_top_1_openapi_name()
        log.info("Validating the new label name is updated or not ")
        assert top_openapi_name == updated_openapi_name
