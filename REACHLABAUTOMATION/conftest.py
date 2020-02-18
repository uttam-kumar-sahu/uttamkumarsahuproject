import pytest
from DriverFile import Driver
from UserData import Data
import logging
from selenium import webdriver
import time
wbdriver = None


"""
Adds screenshot if tests fails
"""

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
           
            if file_name:
                html = '<div><img src="file:/D:/REACHLABAUTOMATION/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

"""
function to capture screenshots
"""

def _capture_screenshot(name):
    try:
        wbdriver.instance.save_screenshot(name)
        logging.info("Screenshot of error page taken and stored")
        
    except Exception as e:
        logging.info("Unable to take screenshot of error page")
        raise e


"""
SETUP-Driver creation ,navigation to url,login to the Dashboard
TEARDOWN-Logout,Closing the driver
"""

@pytest.fixture(scope='class', autouse = True)
def test_set_up_tear_down(request):
    global wbdriver
    if wbdriver is None:
        wbdriver=Driver()
    wbdriver.navigate(Data.base_url,Data.page_title)
    wbdriver.login_to_brand()
    request.cls.driver = wbdriver
    yield
    wbdriver.logout_from_brand()
    logging.info("Closing the Browser")
    wbdriver.instance.close()
    