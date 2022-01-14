import pytest

from pageObjects.AdminPage import Admin
from pageObjects.ConsoleStatus import ConsoleStatus
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestAdminPanel(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_console_status_overview_page_listing(self):
        """
            Verify all the servers listed on this page
            Validation - 1. On the basis of list of the server's name listing
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        admin = Admin(self.driver)
        console = ConsoleStatus(self.driver)
        action.click(nav.click_Admin_Menu())
        log.info("Click on Admin Menu")
        action.click(admin.click_Console_Status())
        log.info("Click on Console Status and check Overview page listing of servers")
        assert action.getText(console.get_overview_elastic_search_text()) == 'Elasticsearch'
        assert action.getText(console.get_overview_my_sql_text()) == 'My SQL'
        assert action.getText(console.get_overview_redis_text()) == 'Redis'
        assert action.getText(console.get_overview_celery_text()) == 'Celery'
        assert action.getText(console.get_overview_gunicorn_text()) == 'Gunicorn'
        assert action.getText(console.get_overview_ngnix_text()) == 'Nginx'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_elastic_search_server_status(self):
        """
            Verify ElasticSearch server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        action = Action(self.driver)
        console = ConsoleStatus(self.driver)
        action.click(console.click_elastic_search())
        log.info("Click on Elastic Search from left panel")
        assert action.getText(console.get_server_status()) == 'Active'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_my_sql_server_status(self):
        """
            Verify My SQL server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        action = Action(self.driver)
        console = ConsoleStatus(self.driver)
        action.click(console.click_my_sql())
        log.info("Click on My SQL from left panel")
        assert action.getText(console.get_server_status()) == 'Active'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_redis_server_status(self):
        """
            Verify redis server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        action = Action(self.driver)
        console = ConsoleStatus(self.driver)
        action.click(console.click_redis())
        log.info("Click on redis from left panel")
        assert action.getText(console.get_server_status()) == 'Active'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_celery_server_status(self):
        """
            Verify celery server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        action = Action(self.driver)
        console = ConsoleStatus(self.driver)
        action.click(console.click_celery())
        log.info("Click on Celery from left panel")
        assert action.getText(console.get_server_status()) == 'Active'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_06_gunicorn_server_status(self):
        """
            Verify gunicorn server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        action = Action(self.driver)
        console = ConsoleStatus(self.driver)
        action.click(console.click_gunicorn())
        log.info("Click on Gunicorn from left panel")
        assert action.getText(console.get_server_status()) == 'Active'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_07_ngnix_server_status(self):
        """
            Verify Ngnix server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        action = Action(self.driver)
        console = ConsoleStatus(self.driver)
        action.click(console.click_gunicorn())
        log.info("Click on Ngnix from left panel")
        assert action.getText(console.get_server_status()) == 'Active'
