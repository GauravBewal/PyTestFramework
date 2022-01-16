import pytest

from pageObjects.TenantManagement import TenantManagement
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestOpenApi(Base):

    @pytest.mark.smoke
    def test_1_admin_Open_APIs(self):
        """
            Verify redirection of Open APIs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        admin = (self.driver)
        action = Action(self.driver)
        log.info("Click on back button from Cyware Agent")
        log.info("Click on Open APIs tab from Admin Page")
        action.click(admin.click_Open_API())
        assert action.getTitle() in 'Open APIs | Cyware Orchestrate'
