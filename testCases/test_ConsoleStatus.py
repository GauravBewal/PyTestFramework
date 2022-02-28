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
    def test_01_Check_Console_Status_Overview_Page_listing(self):
        """
            Verify all the servers listed on this page
            Validation - 1. On the basis of list of the server's name listing
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        admin = Admin(self.driver)
        console = ConsoleStatus(self.driver)
        nav.click_Admin_Menu()
        log.info("Click on Admin Menu")
        admin.click_Console_Status()
        log.info("Click on Console Status and check Overview page listing of servers")
        assert console.get_overview_elastic_search_text() == 'Elasticsearch'
        assert console.get_overview_my_sql_text() == 'My SQL'
        assert console.get_overview_redis_text() == 'Redis'
        assert console.get_overview_celery_text() == 'Celery'
        assert console.get_overview_gunicorn_text() == 'Gunicorn'
        assert console.get_overview_ngnix_text() == 'Nginx'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Check_Elastic_Search_Server_Status(self):
        """
            Verify ElasticSearch server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        console = ConsoleStatus(self.driver)
        console.click_elastic_search()
        log.info("Click on Elastic Search from left panel")
        page_heading = console.get_server_page_heading()
        assert console.get_server_status() == 'Active' and page_heading == 'Elasticsearch'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Check_My_SQL_Server_Status(self):
        """
            Verify My SQL server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        console = ConsoleStatus(self.driver)
        console.click_my_sql()
        log.info("Click on My SQL from left panel")
        page_heading = console.get_server_page_heading()
        assert console.get_server_status() == 'Active' and page_heading == 'MySQL'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Check_Redis_Server_Status(self):
        """
            Verify redis server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        console = ConsoleStatus(self.driver)
        console.click_redis()
        log.info("Click on redis from left panel")
        page_heading = console.get_server_page_heading()
        assert console.get_server_status() == 'Active' and page_heading == 'Redis'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_Check_Celery_Server_Status(self):
        """
            Verify celery server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        console = ConsoleStatus(self.driver)
        console.click_celery()
        log.info("Click on Celery from left panel")
        page_heading = console.get_server_page_heading()
        assert console.get_server_status() == 'Active' and page_heading == 'Celery'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_06_Check_Gunicorn_Server_Status(self):
        """
            Verify gunicorn server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        console = ConsoleStatus(self.driver)
        console.click_gunicorn()
        log.info("Click on Gunicorn from left panel")
        page_heading = console.get_server_page_heading()
        assert console.get_server_status() == 'Active' and page_heading == 'Gunicorn'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_07_Check_Ngnix_Server_Status(self):
        """
            Verify Ngnix server status
            Validation - 1. On the basis of Active text of status
        """
        log = self.getlogger()
        console = ConsoleStatus(self.driver)
        console.click_ngnix()
        log.info("Click on Ngnix from left panel")
        page_heading = console.get_server_page_heading()
        assert console.get_server_status() == 'Active' and page_heading == 'Nginx'
