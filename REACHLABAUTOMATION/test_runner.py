import pytest



TEST_DIRECTORY = "D:/REACHLABAUTOMATION/TestCases"

def run_tests_from_nodes():
    pytest.main(
        [f'{TEST_DIRECTORY}/test_Brand_App.py::TestBrandApp::test_brand',
         '-s' ,'--html=report.html'
,])

def run_tests_from_modules():
    pytest.main(
        [f'{TEST_DIRECTORY}/test_Brand_App.py',
         '-s' ,'--html=report.html'
,])

def run_tests_from_directory():
    pytest.main(
        [f'{TEST_DIRECTORY}/',
         '-s' ,'--html=report.html'
,])

run_tests_from_directory()
#run_tests_from_modules()
#run_tests_from_nodes()
